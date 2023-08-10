import asyncio
import logging
from typing import Dict, Optional, Text, Union

import requests_async as requests
from requests_async import Response

from v1.apps import APIConfig

logger = logging.getLogger(__name__)


class WebClient:
    description_msg = 'Error get request.'
    connection_error_msg = 'URL - "%s" return "%s" code'
    empty_json_error_msg = 'URL - "%s" return emtpy json'
    timeout = APIConfig.REQUEST_TIMEOUT

    def validator(self, response) -> Dict:
        """Перевіряє чи коректно отриманий запит"""
        msg = '%s ' % (self.description_msg,)
        if not (status_code := response.status_code) == 200:
            msg += self.connection_error_msg % (response.request.url, status_code)
            logger.error(
                msg
            )
            raise ConnectionError(msg)

        json_response = response
        if not json_response:
            msg += self.empty_json_error_msg % (response.request.url,)
            logger.error(
                msg
            )
            raise ValueError(msg)

        return json_response

    @staticmethod
    async def _get_time_url_request(func) -> Response:
        """Обраховує час запиту"""
        start_time = asyncio.get_event_loop().time()
        request = await func
        end_time = asyncio.get_event_loop().time()

        execution_time = end_time - start_time
        logger.debug('Execution time request %s: %s s' % ('url', execution_time,))
        return request

    async def _worker(self, func, url: str, output_json: bool = True, **kwargs) -> dict | Response:
        """Основна логіка обробки запиту"""
        kwargs['timeout'] = kwargs.get('timeout', self.timeout)

        response = await self._get_time_url_request(
            func(url, verify=False, **kwargs)
        )

        if output_json:
            try:
                return response.json()
            except Exception as error:
                logger.error("Error: %s\n Request: %s" % (error, response.content))
                return response.json()
        return response

    async def get_request(self, url: str, output_json: bool = True, **kwargs):
        return await self._worker(requests.get, url, output_json, **kwargs)

    async def post_request(self, url: str, output_json: bool = True, **kwargs) -> dict | Response:
        return await self._worker(requests.post, url, output_json, **kwargs)
