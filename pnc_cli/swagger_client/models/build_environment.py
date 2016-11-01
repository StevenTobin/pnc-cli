# coding: utf-8

"""
Copyright 2015 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from datetime import datetime
from pprint import pformat
from six import iteritems


class BuildEnvironment(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        BuildEnvironment - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'name': 'str',
            'description': 'str',
            'system_image_repository_url': 'str',
            'system_image_id': 'str',
            'system_image_type': 'str',
            'attributes': 'dict(str, str)',
            'field_handler': 'FieldHandler'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'description': 'description',
            'system_image_repository_url': 'systemImageRepositoryUrl',
            'system_image_id': 'systemImageId',
            'system_image_type': 'systemImageType',
            'attributes': 'attributes',
            'field_handler': 'fieldHandler'
        }

        self._id = None
        self._name = None
        self._description = None
        self._system_image_repository_url = None
        self._system_image_id = None
        self._system_image_type = None
        self._attributes = None
        self._field_handler = None

    @property
    def id(self):
        """
        Gets the id of this BuildEnvironment.


        :return: The id of this BuildEnvironment.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BuildEnvironment.


        :param id: The id of this BuildEnvironment.
        :type: int
        """
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this BuildEnvironment.


        :return: The name of this BuildEnvironment.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this BuildEnvironment.


        :param name: The name of this BuildEnvironment.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this BuildEnvironment.


        :return: The description of this BuildEnvironment.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this BuildEnvironment.


        :param description: The description of this BuildEnvironment.
        :type: str
        """
        self._description = description

    @property
    def system_image_repository_url(self):
        """
        Gets the system_image_repository_url of this BuildEnvironment.


        :return: The system_image_repository_url of this BuildEnvironment.
        :rtype: str
        """
        return self._system_image_repository_url

    @system_image_repository_url.setter
    def system_image_repository_url(self, system_image_repository_url):
        """
        Sets the system_image_repository_url of this BuildEnvironment.


        :param system_image_repository_url: The system_image_repository_url of this BuildEnvironment.
        :type: str
        """
        self._system_image_repository_url = system_image_repository_url

    @property
    def system_image_id(self):
        """
        Gets the system_image_id of this BuildEnvironment.


        :return: The system_image_id of this BuildEnvironment.
        :rtype: str
        """
        return self._system_image_id

    @system_image_id.setter
    def system_image_id(self, system_image_id):
        """
        Sets the system_image_id of this BuildEnvironment.


        :param system_image_id: The system_image_id of this BuildEnvironment.
        :type: str
        """
        self._system_image_id = system_image_id

    @property
    def system_image_type(self):
        """
        Gets the system_image_type of this BuildEnvironment.


        :return: The system_image_type of this BuildEnvironment.
        :rtype: str
        """
        return self._system_image_type

    @system_image_type.setter
    def system_image_type(self, system_image_type):
        """
        Sets the system_image_type of this BuildEnvironment.


        :param system_image_type: The system_image_type of this BuildEnvironment.
        :type: str
        """
        allowed_values = ["DOCKER_IMAGE", "VIRTUAL_MACHINE_RAW", "VIRTUAL_MACHINE_QCOW2", "LOCAL_WORKSPACE"]
        if system_image_type not in allowed_values:
            raise ValueError(
                "Invalid value for `system_image_type`, must be one of {0}"
                .format(allowed_values)
            )
        self._system_image_type = system_image_type

    @property
    def attributes(self):
        """
        Gets the attributes of this BuildEnvironment.


        :return: The attributes of this BuildEnvironment.
        :rtype: dict(str, str)
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """
        Sets the attributes of this BuildEnvironment.


        :param attributes: The attributes of this BuildEnvironment.
        :type: dict(str, str)
        """
        self._attributes = attributes

    @property
    def field_handler(self):
        """
        Gets the field_handler of this BuildEnvironment.


        :return: The field_handler of this BuildEnvironment.
        :rtype: FieldHandler
        """
        return self._field_handler

    @field_handler.setter
    def field_handler(self, field_handler):
        """
        Sets the field_handler of this BuildEnvironment.


        :param field_handler: The field_handler of this BuildEnvironment.
        :type: FieldHandler
        """
        self._field_handler = field_handler

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
