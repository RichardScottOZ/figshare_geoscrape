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


class AccountCreate(object):
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
        'email': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'group_id': 'int',
        'institution_user_id': 'str',
        'symplectic_user_id': 'str',
        'quota': 'int',
        'is_active': 'bool'
    }

    attribute_map = {
        'email': 'email',
        'first_name': 'first_name',
        'last_name': 'last_name',
        'group_id': 'group_id',
        'institution_user_id': 'institution_user_id',
        'symplectic_user_id': 'symplectic_user_id',
        'quota': 'quota',
        'is_active': 'is_active'
    }

    def __init__(self, email=None, first_name='', last_name='', group_id=None, institution_user_id='', symplectic_user_id='', quota=None, is_active=None):  # noqa: E501
        """AccountCreate - a model defined in Swagger"""  # noqa: E501

        self._email = None
        self._first_name = None
        self._last_name = None
        self._group_id = None
        self._institution_user_id = None
        self._symplectic_user_id = None
        self._quota = None
        self._is_active = None
        self.discriminator = None

        self.email = email
        if first_name is not None:
            self.first_name = first_name
        self.last_name = last_name
        if group_id is not None:
            self.group_id = group_id
        if institution_user_id is not None:
            self.institution_user_id = institution_user_id
        if symplectic_user_id is not None:
            self.symplectic_user_id = symplectic_user_id
        if quota is not None:
            self.quota = quota
        if is_active is not None:
            self.is_active = is_active

    @property
    def email(self):
        """Gets the email of this AccountCreate.  # noqa: E501

        Email of account  # noqa: E501

        :return: The email of this AccountCreate.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this AccountCreate.

        Email of account  # noqa: E501

        :param email: The email of this AccountCreate.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501
        if email is not None and len(email) > 150:
            raise ValueError("Invalid value for `email`, length must be less than or equal to `150`")  # noqa: E501
        if email is not None and len(email) < 3:
            raise ValueError("Invalid value for `email`, length must be greater than or equal to `3`")  # noqa: E501

        self._email = email

    @property
    def first_name(self):
        """Gets the first_name of this AccountCreate.  # noqa: E501

        First Name  # noqa: E501

        :return: The first_name of this AccountCreate.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this AccountCreate.

        First Name  # noqa: E501

        :param first_name: The first_name of this AccountCreate.  # noqa: E501
        :type: str
        """
        if first_name is not None and len(first_name) > 30:
            raise ValueError("Invalid value for `first_name`, length must be less than or equal to `30`")  # noqa: E501

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this AccountCreate.  # noqa: E501

        Last Name  # noqa: E501

        :return: The last_name of this AccountCreate.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this AccountCreate.

        Last Name  # noqa: E501

        :param last_name: The last_name of this AccountCreate.  # noqa: E501
        :type: str
        """
        if last_name is None:
            raise ValueError("Invalid value for `last_name`, must not be `None`")  # noqa: E501
        if last_name is not None and len(last_name) > 30:
            raise ValueError("Invalid value for `last_name`, length must be less than or equal to `30`")  # noqa: E501

        self._last_name = last_name

    @property
    def group_id(self):
        """Gets the group_id of this AccountCreate.  # noqa: E501

        Not applicable to regular users. This field is reserved to institutions/publishers with access to assign to specific groups  # noqa: E501

        :return: The group_id of this AccountCreate.  # noqa: E501
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this AccountCreate.

        Not applicable to regular users. This field is reserved to institutions/publishers with access to assign to specific groups  # noqa: E501

        :param group_id: The group_id of this AccountCreate.  # noqa: E501
        :type: int
        """

        self._group_id = group_id

    @property
    def institution_user_id(self):
        """Gets the institution_user_id of this AccountCreate.  # noqa: E501

        Institution user id  # noqa: E501

        :return: The institution_user_id of this AccountCreate.  # noqa: E501
        :rtype: str
        """
        return self._institution_user_id

    @institution_user_id.setter
    def institution_user_id(self, institution_user_id):
        """Sets the institution_user_id of this AccountCreate.

        Institution user id  # noqa: E501

        :param institution_user_id: The institution_user_id of this AccountCreate.  # noqa: E501
        :type: str
        """
        if institution_user_id is not None and len(institution_user_id) > 50:
            raise ValueError("Invalid value for `institution_user_id`, length must be less than or equal to `50`")  # noqa: E501

        self._institution_user_id = institution_user_id

    @property
    def symplectic_user_id(self):
        """Gets the symplectic_user_id of this AccountCreate.  # noqa: E501

        Symplectic user id  # noqa: E501

        :return: The symplectic_user_id of this AccountCreate.  # noqa: E501
        :rtype: str
        """
        return self._symplectic_user_id

    @symplectic_user_id.setter
    def symplectic_user_id(self, symplectic_user_id):
        """Sets the symplectic_user_id of this AccountCreate.

        Symplectic user id  # noqa: E501

        :param symplectic_user_id: The symplectic_user_id of this AccountCreate.  # noqa: E501
        :type: str
        """
        if symplectic_user_id is not None and len(symplectic_user_id) > 50:
            raise ValueError("Invalid value for `symplectic_user_id`, length must be less than or equal to `50`")  # noqa: E501

        self._symplectic_user_id = symplectic_user_id

    @property
    def quota(self):
        """Gets the quota of this AccountCreate.  # noqa: E501

        Account quota  # noqa: E501

        :return: The quota of this AccountCreate.  # noqa: E501
        :rtype: int
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        """Sets the quota of this AccountCreate.

        Account quota  # noqa: E501

        :param quota: The quota of this AccountCreate.  # noqa: E501
        :type: int
        """

        self._quota = quota

    @property
    def is_active(self):
        """Gets the is_active of this AccountCreate.  # noqa: E501

        Is account active  # noqa: E501

        :return: The is_active of this AccountCreate.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this AccountCreate.

        Is account active  # noqa: E501

        :param is_active: The is_active of this AccountCreate.  # noqa: E501
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
        if issubclass(AccountCreate, dict):
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
        if not isinstance(other, AccountCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
