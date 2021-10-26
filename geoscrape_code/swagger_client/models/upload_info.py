# coding: utf-8

"""
    Figshare API

    Figshare apiv2. Using Swagger 2.0  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class UploadInfo(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'token': 'str',
        'md5': 'str',
        'size': 'int',
        'name': 'str',
        'status': 'str',
        'parts': 'list[UploadFilePart]'
    }

    attribute_map = {
        'token': 'token',
        'md5': 'md5',
        'size': 'size',
        'name': 'name',
        'status': 'status',
        'parts': 'parts'
    }

    def __init__(self, token=None, md5=None, size=None, name=None, status=None, parts=None):  # noqa: E501
        """UploadInfo - a model defined in Swagger"""  # noqa: E501

        self._token = None
        self._md5 = None
        self._size = None
        self._name = None
        self._status = None
        self._parts = None
        self.discriminator = None

        if token is not None:
            self.token = token
        if md5 is not None:
            self.md5 = md5
        if size is not None:
            self.size = size
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if parts is not None:
            self.parts = parts

    @property
    def token(self):
        """Gets the token of this UploadInfo.  # noqa: E501

        token received after initializing a file upload  # noqa: E501

        :return: The token of this UploadInfo.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this UploadInfo.

        token received after initializing a file upload  # noqa: E501

        :param token: The token of this UploadInfo.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def md5(self):
        """Gets the md5 of this UploadInfo.  # noqa: E501

        md5 provided on upload initialization  # noqa: E501

        :return: The md5 of this UploadInfo.  # noqa: E501
        :rtype: str
        """
        return self._md5

    @md5.setter
    def md5(self, md5):
        """Sets the md5 of this UploadInfo.

        md5 provided on upload initialization  # noqa: E501

        :param md5: The md5 of this UploadInfo.  # noqa: E501
        :type: str
        """

        self._md5 = md5

    @property
    def size(self):
        """Gets the size of this UploadInfo.  # noqa: E501

        size of file in bytes  # noqa: E501

        :return: The size of this UploadInfo.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this UploadInfo.

        size of file in bytes  # noqa: E501

        :param size: The size of this UploadInfo.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def name(self):
        """Gets the name of this UploadInfo.  # noqa: E501

        name of file on upload server  # noqa: E501

        :return: The name of this UploadInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UploadInfo.

        name of file on upload server  # noqa: E501

        :param name: The name of this UploadInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def status(self):
        """Gets the status of this UploadInfo.  # noqa: E501

        Upload status  # noqa: E501

        :return: The status of this UploadInfo.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UploadInfo.

        Upload status  # noqa: E501

        :param status: The status of this UploadInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["PENDING", "COMPLETED", "ABORTED"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def parts(self):
        """Gets the parts of this UploadInfo.  # noqa: E501

        Uploads parts  # noqa: E501

        :return: The parts of this UploadInfo.  # noqa: E501
        :rtype: list[UploadFilePart]
        """
        return self._parts

    @parts.setter
    def parts(self, parts):
        """Sets the parts of this UploadInfo.

        Uploads parts  # noqa: E501

        :param parts: The parts of this UploadInfo.  # noqa: E501
        :type: list[UploadFilePart]
        """

        self._parts = parts

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(UploadInfo, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UploadInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
