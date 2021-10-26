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


class AccountUpdate(object):
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
        'group_id': 'int',
        'is_active': 'bool'
    }

    attribute_map = {
        'group_id': 'group_id',
        'is_active': 'is_active'
    }

    def __init__(self, group_id=None, is_active=None):  # noqa: E501
        """AccountUpdate - a model defined in Swagger"""  # noqa: E501

        self._group_id = None
        self._is_active = None
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id
        if is_active is not None:
            self.is_active = is_active

    @property
    def group_id(self):
        """Gets the group_id of this AccountUpdate.  # noqa: E501

        Not applicable to regular users. This field is reserved to institutions/publishers with access to assign to specific groups  # noqa: E501

        :return: The group_id of this AccountUpdate.  # noqa: E501
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this AccountUpdate.

        Not applicable to regular users. This field is reserved to institutions/publishers with access to assign to specific groups  # noqa: E501

        :param group_id: The group_id of this AccountUpdate.  # noqa: E501
        :type: int
        """

        self._group_id = group_id

    @property
    def is_active(self):
        """Gets the is_active of this AccountUpdate.  # noqa: E501

        Is account active  # noqa: E501

        :return: The is_active of this AccountUpdate.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this AccountUpdate.

        Is account active  # noqa: E501

        :param is_active: The is_active of this AccountUpdate.  # noqa: E501
        :type: bool
        """

        self._is_active = is_active

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
        if issubclass(AccountUpdate, dict):
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
        if not isinstance(other, AccountUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
