# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from datetime import datetime
from pprint import pformat
from six import iteritems
import re


class BuildRecordPushRequestRest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'tag_prefix': 'str',
        'build_record_id': 'int'
    }

    attribute_map = {
        'tag_prefix': 'tagPrefix',
        'build_record_id': 'buildRecordId'
    }

    def __init__(self, tag_prefix=None, build_record_id=None):
        """
        BuildRecordPushRequestRest - a model defined in Swagger
        """

        self._tag_prefix = None
        self._build_record_id = None

        if tag_prefix is not None:
          self.tag_prefix = tag_prefix
        if build_record_id is not None:
          self.build_record_id = build_record_id

    @property
    def tag_prefix(self):
        """
        Gets the tag_prefix of this BuildRecordPushRequestRest.

        :return: The tag_prefix of this BuildRecordPushRequestRest.
        :rtype: str
        """
        return self._tag_prefix

    @tag_prefix.setter
    def tag_prefix(self, tag_prefix):
        """
        Sets the tag_prefix of this BuildRecordPushRequestRest.

        :param tag_prefix: The tag_prefix of this BuildRecordPushRequestRest.
        :type: str
        """

        self._tag_prefix = tag_prefix

    @property
    def build_record_id(self):
        """
        Gets the build_record_id of this BuildRecordPushRequestRest.

        :return: The build_record_id of this BuildRecordPushRequestRest.
        :rtype: int
        """
        return self._build_record_id

    @build_record_id.setter
    def build_record_id(self, build_record_id):
        """
        Sets the build_record_id of this BuildRecordPushRequestRest.

        :param build_record_id: The build_record_id of this BuildRecordPushRequestRest.
        :type: int
        """

        self._build_record_id = build_record_id

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
	    elif isinstance(value, datetime):
		result[attr] = str(value.date())
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, BuildRecordPushRequestRest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
