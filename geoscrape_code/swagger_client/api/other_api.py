# coding: utf-8

"""
    Figshare API

    Figshare apiv2. Using Swagger 2.0  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class OtherApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def categories_list(self, **kwargs):  # noqa: E501
        """Public Categories  # noqa: E501

        Returns a list of public categories  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.categories_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[Category]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.categories_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.categories_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def categories_list_with_http_info(self, **kwargs):  # noqa: E501
        """Public Categories  # noqa: E501

        Returns a list of public categories  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.categories_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[Category]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method categories_list" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/categories', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Category]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def file_download(self, file_id, **kwargs):  # noqa: E501
        """Public File Download  # noqa: E501

        Starts the download of a file  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.file_download(file_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int file_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.file_download_with_http_info(file_id, **kwargs)  # noqa: E501
        else:
            (data) = self.file_download_with_http_info(file_id, **kwargs)  # noqa: E501
            return data

    def file_download_with_http_info(self, file_id, **kwargs):  # noqa: E501
        """Public File Download  # noqa: E501

        Starts the download of a file  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.file_download_with_http_info(file_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int file_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method file_download" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_id' is set
        if ('file_id' not in params or
                params['file_id'] is None):
            raise ValueError("Missing the required parameter `file_id` when calling `file_download`")  # noqa: E501

        if 'file_id' in params and params['file_id'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `file_id` when calling `file_download`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'file_id' in params:
            path_params['file_id'] = params['file_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/force-download'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/file/download/{file_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def licenses_list(self, **kwargs):  # noqa: E501
        """Public Licenses  # noqa: E501

        Returns a list of public licenses  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.licenses_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[License]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.licenses_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.licenses_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def licenses_list_with_http_info(self, **kwargs):  # noqa: E501
        """Public Licenses  # noqa: E501

        Returns a list of public licenses  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.licenses_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[License]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method licenses_list" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/licenses', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[License]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def private_account(self, **kwargs):  # noqa: E501
        """Private Account information  # noqa: E501

        Account information for token/personal token  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_account(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Account
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.private_account_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.private_account_with_http_info(**kwargs)  # noqa: E501
            return data

    def private_account_with_http_info(self, **kwargs):  # noqa: E501
        """Private Account information  # noqa: E501

        Account information for token/personal token  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_account_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Account
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method private_account" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/account', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Account',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def private_funding_search(self, **kwargs):  # noqa: E501
        """Search Funding  # noqa: E501

        Search for fundings  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_funding_search(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FundingSearch search: Search Parameters
        :return: list[FundingInformation]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.private_funding_search_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.private_funding_search_with_http_info(**kwargs)  # noqa: E501
            return data

    def private_funding_search_with_http_info(self, **kwargs):  # noqa: E501
        """Search Funding  # noqa: E501

        Search for fundings  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_funding_search_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FundingSearch search: Search Parameters
        :return: list[FundingInformation]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['search']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method private_funding_search" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'search' in params:
            body_params = params['search']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/account/funding/search', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[FundingInformation]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def private_licenses_list(self, **kwargs):  # noqa: E501
        """Private Account Licenses  # noqa: E501

        This is a private endpoint that requires OAuth. It will return a list with figshare public licenses AND licenses defined for account's institution.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_licenses_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[License]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.private_licenses_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.private_licenses_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def private_licenses_list_with_http_info(self, **kwargs):  # noqa: E501
        """Private Account Licenses  # noqa: E501

        This is a private endpoint that requires OAuth. It will return a list with figshare public licenses AND licenses defined for account's institution.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.private_licenses_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[License]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method private_licenses_list" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/account/licenses', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[License]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
