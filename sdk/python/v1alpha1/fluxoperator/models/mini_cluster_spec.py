# coding: utf-8

"""
    fluxoperator

    Python SDK for Flux-Operator  # noqa: E501

    The version of the OpenAPI document: v1alpha1
    Generated by: https://openapi-generator.tech
"""


import inspect
import pprint
import re  # noqa: F401
import six

from fluxoperator.configuration import Configuration


class MiniClusterSpec(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'cleanup': 'bool',
        'containers': 'list[MiniClusterContainer]',
        'deadline_seconds': 'int',
        'flux_restful': 'FluxRestful',
        'job_labels': 'dict(str, str)',
        'logging': 'LoggingSpec',
        'pod': 'PodSpec',
        'size': 'int',
        'tasks': 'int',
        'users': 'list[MiniClusterUser]',
        'volumes': 'dict(str, MiniClusterVolume)'
    }

    attribute_map = {
        'cleanup': 'cleanup',
        'containers': 'containers',
        'deadline_seconds': 'deadlineSeconds',
        'flux_restful': 'fluxRestful',
        'job_labels': 'jobLabels',
        'logging': 'logging',
        'pod': 'pod',
        'size': 'size',
        'tasks': 'tasks',
        'users': 'users',
        'volumes': 'volumes'
    }

    def __init__(self, cleanup=False, containers=None, deadline_seconds=31500000, flux_restful=None, job_labels=None, logging=None, pod=None, size=1, tasks=1, users=None, volumes=None, local_vars_configuration=None):  # noqa: E501
        """MiniClusterSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._cleanup = None
        self._containers = None
        self._deadline_seconds = None
        self._flux_restful = None
        self._job_labels = None
        self._logging = None
        self._pod = None
        self._size = None
        self._tasks = None
        self._users = None
        self._volumes = None
        self.discriminator = None

        if cleanup is not None:
            self.cleanup = cleanup
        self.containers = containers
        if deadline_seconds is not None:
            self.deadline_seconds = deadline_seconds
        if flux_restful is not None:
            self.flux_restful = flux_restful
        if job_labels is not None:
            self.job_labels = job_labels
        if logging is not None:
            self.logging = logging
        if pod is not None:
            self.pod = pod
        if size is not None:
            self.size = size
        if tasks is not None:
            self.tasks = tasks
        if users is not None:
            self.users = users
        if volumes is not None:
            self.volumes = volumes

    @property
    def cleanup(self):
        """Gets the cleanup of this MiniClusterSpec.  # noqa: E501

        Cleanup the pods and storage when the index broker pod is complete  # noqa: E501

        :return: The cleanup of this MiniClusterSpec.  # noqa: E501
        :rtype: bool
        """
        return self._cleanup

    @cleanup.setter
    def cleanup(self, cleanup):
        """Sets the cleanup of this MiniClusterSpec.

        Cleanup the pods and storage when the index broker pod is complete  # noqa: E501

        :param cleanup: The cleanup of this MiniClusterSpec.  # noqa: E501
        :type cleanup: bool
        """

        self._cleanup = cleanup

    @property
    def containers(self):
        """Gets the containers of this MiniClusterSpec.  # noqa: E501

        Containers is one or more containers to be created in a pod. There should only be one container to run flux with runFlux  # noqa: E501

        :return: The containers of this MiniClusterSpec.  # noqa: E501
        :rtype: list[MiniClusterContainer]
        """
        return self._containers

    @containers.setter
    def containers(self, containers):
        """Sets the containers of this MiniClusterSpec.

        Containers is one or more containers to be created in a pod. There should only be one container to run flux with runFlux  # noqa: E501

        :param containers: The containers of this MiniClusterSpec.  # noqa: E501
        :type containers: list[MiniClusterContainer]
        """
        if self.local_vars_configuration.client_side_validation and containers is None:  # noqa: E501
            raise ValueError("Invalid value for `containers`, must not be `None`")  # noqa: E501

        self._containers = containers

    @property
    def deadline_seconds(self):
        """Gets the deadline_seconds of this MiniClusterSpec.  # noqa: E501

        Should the job be limited to a particular number of seconds? Approximately one year. This cannot be zero or job won't start  # noqa: E501

        :return: The deadline_seconds of this MiniClusterSpec.  # noqa: E501
        :rtype: int
        """
        return self._deadline_seconds

    @deadline_seconds.setter
    def deadline_seconds(self, deadline_seconds):
        """Sets the deadline_seconds of this MiniClusterSpec.

        Should the job be limited to a particular number of seconds? Approximately one year. This cannot be zero or job won't start  # noqa: E501

        :param deadline_seconds: The deadline_seconds of this MiniClusterSpec.  # noqa: E501
        :type deadline_seconds: int
        """

        self._deadline_seconds = deadline_seconds

    @property
    def flux_restful(self):
        """Gets the flux_restful of this MiniClusterSpec.  # noqa: E501


        :return: The flux_restful of this MiniClusterSpec.  # noqa: E501
        :rtype: FluxRestful
        """
        return self._flux_restful

    @flux_restful.setter
    def flux_restful(self, flux_restful):
        """Sets the flux_restful of this MiniClusterSpec.


        :param flux_restful: The flux_restful of this MiniClusterSpec.  # noqa: E501
        :type flux_restful: FluxRestful
        """

        self._flux_restful = flux_restful

    @property
    def job_labels(self):
        """Gets the job_labels of this MiniClusterSpec.  # noqa: E501

        Labels for the job  # noqa: E501

        :return: The job_labels of this MiniClusterSpec.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._job_labels

    @job_labels.setter
    def job_labels(self, job_labels):
        """Sets the job_labels of this MiniClusterSpec.

        Labels for the job  # noqa: E501

        :param job_labels: The job_labels of this MiniClusterSpec.  # noqa: E501
        :type job_labels: dict(str, str)
        """

        self._job_labels = job_labels

    @property
    def logging(self):
        """Gets the logging of this MiniClusterSpec.  # noqa: E501


        :return: The logging of this MiniClusterSpec.  # noqa: E501
        :rtype: LoggingSpec
        """
        return self._logging

    @logging.setter
    def logging(self, logging):
        """Sets the logging of this MiniClusterSpec.


        :param logging: The logging of this MiniClusterSpec.  # noqa: E501
        :type logging: LoggingSpec
        """

        self._logging = logging

    @property
    def pod(self):
        """Gets the pod of this MiniClusterSpec.  # noqa: E501


        :return: The pod of this MiniClusterSpec.  # noqa: E501
        :rtype: PodSpec
        """
        return self._pod

    @pod.setter
    def pod(self, pod):
        """Sets the pod of this MiniClusterSpec.


        :param pod: The pod of this MiniClusterSpec.  # noqa: E501
        :type pod: PodSpec
        """

        self._pod = pod

    @property
    def size(self):
        """Gets the size of this MiniClusterSpec.  # noqa: E501

        Size (number of job pods to run, size of minicluster in pods)  # noqa: E501

        :return: The size of this MiniClusterSpec.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this MiniClusterSpec.

        Size (number of job pods to run, size of minicluster in pods)  # noqa: E501

        :param size: The size of this MiniClusterSpec.  # noqa: E501
        :type size: int
        """

        self._size = size

    @property
    def tasks(self):
        """Gets the tasks of this MiniClusterSpec.  # noqa: E501

        Total number of CPUs being run across entire cluster  # noqa: E501

        :return: The tasks of this MiniClusterSpec.  # noqa: E501
        :rtype: int
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        """Sets the tasks of this MiniClusterSpec.

        Total number of CPUs being run across entire cluster  # noqa: E501

        :param tasks: The tasks of this MiniClusterSpec.  # noqa: E501
        :type tasks: int
        """

        self._tasks = tasks

    @property
    def users(self):
        """Gets the users of this MiniClusterSpec.  # noqa: E501

        Users of the MiniCluster  # noqa: E501

        :return: The users of this MiniClusterSpec.  # noqa: E501
        :rtype: list[MiniClusterUser]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this MiniClusterSpec.

        Users of the MiniCluster  # noqa: E501

        :param users: The users of this MiniClusterSpec.  # noqa: E501
        :type users: list[MiniClusterUser]
        """

        self._users = users

    @property
    def volumes(self):
        """Gets the volumes of this MiniClusterSpec.  # noqa: E501

        Volumes accessible to containers from a host  # noqa: E501

        :return: The volumes of this MiniClusterSpec.  # noqa: E501
        :rtype: dict(str, MiniClusterVolume)
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """Sets the volumes of this MiniClusterSpec.

        Volumes accessible to containers from a host  # noqa: E501

        :param volumes: The volumes of this MiniClusterSpec.  # noqa: E501
        :type volumes: dict(str, MiniClusterVolume)
        """

        self._volumes = volumes

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = inspect.getargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MiniClusterSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MiniClusterSpec):
            return True

        return self.to_dict() != other.to_dict()
