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


class ProjectComplete(object):
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
        'collaborators': 'list[Collaborator]'
    }

    attribute_map = {
        'funding': 'funding',
        'funding_list': 'funding_list',
        'description': 'description',
        'collaborators': 'collaborators'
    }

    def __init__(self, funding=None, funding_list=None, description=None, collaborators=None):  # noqa: E501
        """ProjectComplete - a model defined in Swagger"""  # noqa: E501

        self._funding = None
        self._funding_list = None
        self._description = None
        self._collaborators = None
        self.discriminator = None

        if funding is not None:
            self.funding = funding
        if funding_list is not None:
            self.funding_list = funding_list
        if description is not None:
            self.description = description
        if collaborators is not None:
            self.collaborators = collaborators

    @property
    def funding(self):
        """Gets the funding of this ProjectComplete.  # noqa: E501

        Project funding  # noqa: E501

        :return: The funding of this ProjectComplete.  # noqa: E501
        :rtype: str
        """
        return self._funding

    @funding.setter
    def funding(self, funding):
        """Sets the funding of this ProjectComplete.

        Project funding  # noqa: E501

        :param funding: The funding of this ProjectComplete.  # noqa: E501
        :type: str
        """

        self._funding = funding

    @property
    def funding_list(self):
        """Gets the funding_list of this ProjectComplete.  # noqa: E501

        Full Project funding information  # noqa: E501

        :return: The funding_list of this ProjectComplete.  # noqa: E501
        :rtype: list[FundingInformation]
        """
        return self._funding_list

    @funding_list.setter
    def funding_list(self, funding_list):
        """Sets the funding_list of this ProjectComplete.

        Full Project funding information  # noqa: E501

        :param funding_list: The funding_list of this ProjectComplete.  # noqa: E501
        :type: list[FundingInformation]
        """

        self._funding_list = funding_list

    @property
    def description(self):
        """Gets the description of this ProjectComplete.  # noqa: E501

        Project description  # noqa: E501

        :return: The description of this ProjectComplete.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProjectComplete.

        Project description  # noqa: E501

        :param description: The description of this ProjectComplete.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def collaborators(self):
        """Gets the collaborators of this ProjectComplete.  # noqa: E501

        List of project collaborators  # noqa: E501

        :return: The collaborators of this ProjectComplete.  # noqa: E501
        :rtype: list[Collaborator]
        """
        return self._collaborators

    @collaborators.setter
    def collaborators(self, collaborators):
        """Sets the collaborators of this ProjectComplete.

        List of project collaborators  # noqa: E501

        :param collaborators: The collaborators of this ProjectComplete.  # noqa: E501
        :type: list[Collaborator]
        """

        self._collaborators = collaborators

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
        if issubclass(ProjectComplete, dict):
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
        if not isinstance(other, ProjectComplete):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
