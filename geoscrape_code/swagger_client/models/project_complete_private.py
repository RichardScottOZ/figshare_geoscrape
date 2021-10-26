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


class ProjectCompletePrivate(object):
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
        'funding': 'str',
        'funding_list': 'list[FundingInformation]',
        'description': 'str',
        'collaborators': 'list[Collaborator]',
        'quota': 'int',
        'used_quota': 'int',
        'created_date': 'str',
        'modified_date': 'str',
        'used_quota_private': 'int',
        'used_quota_public': 'int',
        'group_id': 'int'
    }

    attribute_map = {
        'funding': 'funding',
        'funding_list': 'funding_list',
        'description': 'description',
        'collaborators': 'collaborators',
        'quota': 'quota',
        'used_quota': 'used_quota',
        'created_date': 'created_date',
        'modified_date': 'modified_date',
        'used_quota_private': 'used_quota_private',
        'used_quota_public': 'used_quota_public',
        'group_id': 'group_id'
    }

    def __init__(self, funding=None, funding_list=None, description=None, collaborators=None, quota=None, used_quota=None, created_date=None, modified_date=None, used_quota_private=None, used_quota_public=None, group_id=None):  # noqa: E501
        """ProjectCompletePrivate - a model defined in Swagger"""  # noqa: E501

        self._funding = None
        self._funding_list = None
        self._description = None
        self._collaborators = None
        self._quota = None
        self._used_quota = None
        self._created_date = None
        self._modified_date = None
        self._used_quota_private = None
        self._used_quota_public = None
        self._group_id = None
        self.discriminator = None

        if funding is not None:
            self.funding = funding
        if funding_list is not None:
            self.funding_list = funding_list
        if description is not None:
            self.description = description
        if collaborators is not None:
            self.collaborators = collaborators
        if quota is not None:
            self.quota = quota
        if used_quota is not None:
            self.used_quota = used_quota
        if created_date is not None:
            self.created_date = created_date
        if modified_date is not None:
            self.modified_date = modified_date
        if used_quota_private is not None:
            self.used_quota_private = used_quota_private
        if used_quota_public is not None:
            self.used_quota_public = used_quota_public
        if group_id is not None:
            self.group_id = group_id

    @property
    def funding(self):
        """Gets the funding of this ProjectCompletePrivate.  # noqa: E501

        Project funding  # noqa: E501

        :return: The funding of this ProjectCompletePrivate.  # noqa: E501
        :rtype: str
        """
        return self._funding

    @funding.setter
    def funding(self, funding):
        """Sets the funding of this ProjectCompletePrivate.

        Project funding  # noqa: E501

        :param funding: The funding of this ProjectCompletePrivate.  # noqa: E501
        :type: str
        """

        self._funding = funding

    @property
    def funding_list(self):
        """Gets the funding_list of this ProjectCompletePrivate.  # noqa: E501

        Full Project funding information  # noqa: E501

        :return: The funding_list of this ProjectCompletePrivate.  # noqa: E501
        :rtype: list[FundingInformation]
        """
        return self._funding_list

    @funding_list.setter
    def funding_list(self, funding_list):
        """Sets the funding_list of this ProjectCompletePrivate.

        Full Project funding information  # noqa: E501

        :param funding_list: The funding_list of this ProjectCompletePrivate.  # noqa: E501
        :type: list[FundingInformation]
        """

        self._funding_list = funding_list

    @property
    def description(self):
        """Gets the description of this ProjectCompletePrivate.  # noqa: E501

        Project description  # noqa: E501

        :return: The description of this ProjectCompletePrivate.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProjectCompletePrivate.

        Project description  # noqa: E501

        :param description: The description of this ProjectCompletePrivate.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def collaborators(self):
        """Gets the collaborators of this ProjectCompletePrivate.  # noqa: E501

        List of project collaborators  # noqa: E501

        :return: The collaborators of this ProjectCompletePrivate.  # noqa: E501
        :rtype: list[Collaborator]
        """
        return self._collaborators

    @collaborators.setter
    def collaborators(self, collaborators):
        """Sets the collaborators of this ProjectCompletePrivate.

        List of project collaborators  # noqa: E501

        :param collaborators: The collaborators of this ProjectCompletePrivate.  # noqa: E501
        :type: list[Collaborator]
        """

        self._collaborators = collaborators

    @property
    def quota(self):
        """Gets the quota of this ProjectCompletePrivate.  # noqa: E501

        Project quota  # noqa: E501

        :return: The quota of this ProjectCompletePrivate.  # noqa: E501
        :rtype: int
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        """Sets the quota of this ProjectCompletePrivate.

        Project quota  # noqa: E501

        :param quota: The quota of this ProjectCompletePrivate.  # noqa: E501
        :type: int
        """

        self._quota = quota

    @property
    def used_quota(self):
        """Gets the used_quota of this ProjectCompletePrivate.  # noqa: E501

        Project used quota  # noqa: E501

        :return: The used_quota of this ProjectCompletePrivate.  # noqa: E501
        :rtype: int
        """
        return self._used_quota

    @used_quota.setter
    def used_quota(self, used_quota):
        """Sets the used_quota of this ProjectCompletePrivate.

        Project used quota  # noqa: E501

        :param used_quota: The used_quota of this ProjectCompletePrivate.  # noqa: E501
        :type: int
        """

        self._used_quota = used_quota

    @property
    def created_date(self):
        """Gets the created_date of this ProjectCompletePrivate.  # noqa: E501

        Date when project was created  # noqa: E501

        :return: The created_date of this ProjectCompletePrivate.  # noqa: E501
        :rtype: str
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this ProjectCompletePrivate.

        Date when project was created  # noqa: E501

        :param created_date: The created_date of this ProjectCompletePrivate.  # noqa: E501
        :type: str
        """

        self._created_date = created_date

    @property
    def modified_date(self):
        """Gets the modified_date of this ProjectCompletePrivate.  # noqa: E501

        Date when project was last modified  # noqa: E501

        :return: The modified_date of this ProjectCompletePrivate.  # noqa: E501
        :rtype: str
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        """Sets the modified_date of this ProjectCompletePrivate.

        Date when project was last modified  # noqa: E501

        :param modified_date: The modified_date of this ProjectCompletePrivate.  # noqa: E501
        :type: str
        """

        self._modified_date = modified_date

    @property
    def used_quota_private(self):
        """Gets the used_quota_private of this ProjectCompletePrivate.  # noqa: E501

        Project private quota used  # noqa: E501

        :return: The used_quota_private of this ProjectCompletePrivate.  # noqa: E501
        :rtype: int
        """
        return self._used_quota_private

    @used_quota_private.setter
    def used_quota_private(self, used_quota_private):
        """Sets the used_quota_private of this ProjectCompletePrivate.

        Project private quota used  # noqa: E501

        :param used_quota_private: The used_quota_private of this ProjectCompletePrivate.  # noqa: E501
        :type: int
        """

        self._used_quota_private = used_quota_private

    @property
    def used_quota_public(self):
        """Gets the used_quota_public of this ProjectCompletePrivate.  # noqa: E501

        Project public quota used  # noqa: E501

        :return: The used_quota_public of this ProjectCompletePrivate.  # noqa: E501
        :rtype: int
        """
        return self._used_quota_public

    @used_quota_public.setter
    def used_quota_public(self, used_quota_public):
        """Sets the used_quota_public of this ProjectCompletePrivate.

        Project public quota used  # noqa: E501

        :param used_quota_public: The used_quota_public of this ProjectCompletePrivate.  # noqa: E501
        :type: int
        """

        self._used_quota_public = used_quota_public

    @property
    def group_id(self):
        """Gets the group_id of this ProjectCompletePrivate.  # noqa: E501

        Group of project if any  # noqa: E501

        :return: The group_id of this ProjectCompletePrivate.  # noqa: E501
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ProjectCompletePrivate.

        Group of project if any  # noqa: E501

        :param group_id: The group_id of this ProjectCompletePrivate.  # noqa: E501
        :type: int
        """

        self._group_id = group_id

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
        if issubclass(ProjectCompletePrivate, dict):
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
        if not isinstance(other, ProjectCompletePrivate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
