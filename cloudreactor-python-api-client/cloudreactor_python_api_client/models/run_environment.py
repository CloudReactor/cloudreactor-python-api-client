import datetime
import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.aws_ecs_run_environment_execution_method_capability import AwsEcsRunEnvironmentExecutionMethodCapability
from ..models.group import Group
from ..models.name_and_uuid import NameAndUuid
from ..types import UNSET, Unset

T = TypeVar("T", bound="RunEnvironment")


@attr.s(auto_attribs=True)
class RunEnvironment:
    """RunEnvironments contain common settings for running a set of
    related Tasks. Usually RunEnvironments group Tasks in the same
    deployment environment (e.g. staging or production).
    Task and Workflows belong to a RunEnvironment but can override
    the RunEnvironment's settings.

        Attributes:
            url (str):
            uuid (str):
            name (str):
            dashboard_url (str):
            created_by_user (str): Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.
            created_by_group (Group):
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
            execution_method_capabilities (List[AwsEcsRunEnvironmentExecutionMethodCapability]):
            description (Union[Unset, str]):
            aws_account_id (Union[Unset, str]):
            aws_default_region (Union[Unset, str]):
            aws_access_key (Union[Unset, str]):
            aws_assumed_role_external_id (Union[Unset, str]):
            aws_events_role_arn (Union[Unset, str]):
            aws_workflow_starter_lambda_arn (Union[Unset, str]):
            aws_workflow_starter_access_key (Union[Unset, str]):
            default_alert_methods (Union[Unset, List[NameAndUuid]]):
    """

    url: str
    uuid: str
    name: str
    dashboard_url: str
    created_by_user: str
    created_by_group: Group
    created_at: datetime.datetime
    updated_at: datetime.datetime
    execution_method_capabilities: List[AwsEcsRunEnvironmentExecutionMethodCapability]
    description: Union[Unset, str] = UNSET
    aws_account_id: Union[Unset, str] = UNSET
    aws_default_region: Union[Unset, str] = UNSET
    aws_access_key: Union[Unset, str] = UNSET
    aws_assumed_role_external_id: Union[Unset, str] = UNSET
    aws_events_role_arn: Union[Unset, str] = UNSET
    aws_workflow_starter_lambda_arn: Union[Unset, str] = UNSET
    aws_workflow_starter_access_key: Union[Unset, str] = UNSET
    default_alert_methods: Union[Unset, List[NameAndUuid]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        uuid = self.uuid
        name = self.name
        dashboard_url = self.dashboard_url
        created_by_user = self.created_by_user
        created_by_group = self.created_by_group.to_dict()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        execution_method_capabilities = []
        for execution_method_capabilities_item_data in self.execution_method_capabilities:
            execution_method_capabilities_item = execution_method_capabilities_item_data.to_dict()

            execution_method_capabilities.append(execution_method_capabilities_item)

        description = self.description
        aws_account_id = self.aws_account_id
        aws_default_region = self.aws_default_region
        aws_access_key = self.aws_access_key
        aws_assumed_role_external_id = self.aws_assumed_role_external_id
        aws_events_role_arn = self.aws_events_role_arn
        aws_workflow_starter_lambda_arn = self.aws_workflow_starter_lambda_arn
        aws_workflow_starter_access_key = self.aws_workflow_starter_access_key
        default_alert_methods: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.default_alert_methods, Unset):
            default_alert_methods = []
            for default_alert_methods_item_data in self.default_alert_methods:
                default_alert_methods_item = default_alert_methods_item_data.to_dict()

                default_alert_methods.append(default_alert_methods_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "uuid": uuid,
                "name": name,
                "dashboard_url": dashboard_url,
                "created_by_user": created_by_user,
                "created_by_group": created_by_group,
                "created_at": created_at,
                "updated_at": updated_at,
                "execution_method_capabilities": execution_method_capabilities,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if aws_account_id is not UNSET:
            field_dict["aws_account_id"] = aws_account_id
        if aws_default_region is not UNSET:
            field_dict["aws_default_region"] = aws_default_region
        if aws_access_key is not UNSET:
            field_dict["aws_access_key"] = aws_access_key
        if aws_assumed_role_external_id is not UNSET:
            field_dict["aws_assumed_role_external_id"] = aws_assumed_role_external_id
        if aws_events_role_arn is not UNSET:
            field_dict["aws_events_role_arn"] = aws_events_role_arn
        if aws_workflow_starter_lambda_arn is not UNSET:
            field_dict["aws_workflow_starter_lambda_arn"] = aws_workflow_starter_lambda_arn
        if aws_workflow_starter_access_key is not UNSET:
            field_dict["aws_workflow_starter_access_key"] = aws_workflow_starter_access_key
        if default_alert_methods is not UNSET:
            field_dict["default_alert_methods"] = default_alert_methods

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        url = self.url if isinstance(self.url, Unset) else (None, str(self.url).encode(), "text/plain")
        uuid = self.uuid if isinstance(self.uuid, Unset) else (None, str(self.uuid).encode(), "text/plain")
        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")
        dashboard_url = (
            self.dashboard_url
            if isinstance(self.dashboard_url, Unset)
            else (None, str(self.dashboard_url).encode(), "text/plain")
        )
        created_by_user = (
            self.created_by_user
            if isinstance(self.created_by_user, Unset)
            else (None, str(self.created_by_user).encode(), "text/plain")
        )
        created_by_group = (None, json.dumps(self.created_by_group.to_dict()).encode(), "application/json")

        created_at = self.created_at.isoformat().encode()

        updated_at = self.updated_at.isoformat().encode()

        _temp_execution_method_capabilities = []
        for execution_method_capabilities_item_data in self.execution_method_capabilities:
            execution_method_capabilities_item = execution_method_capabilities_item_data.to_dict()

            _temp_execution_method_capabilities.append(execution_method_capabilities_item)
        execution_method_capabilities = (
            None,
            json.dumps(_temp_execution_method_capabilities).encode(),
            "application/json",
        )

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )
        aws_account_id = (
            self.aws_account_id
            if isinstance(self.aws_account_id, Unset)
            else (None, str(self.aws_account_id).encode(), "text/plain")
        )
        aws_default_region = (
            self.aws_default_region
            if isinstance(self.aws_default_region, Unset)
            else (None, str(self.aws_default_region).encode(), "text/plain")
        )
        aws_access_key = (
            self.aws_access_key
            if isinstance(self.aws_access_key, Unset)
            else (None, str(self.aws_access_key).encode(), "text/plain")
        )
        aws_assumed_role_external_id = (
            self.aws_assumed_role_external_id
            if isinstance(self.aws_assumed_role_external_id, Unset)
            else (None, str(self.aws_assumed_role_external_id).encode(), "text/plain")
        )
        aws_events_role_arn = (
            self.aws_events_role_arn
            if isinstance(self.aws_events_role_arn, Unset)
            else (None, str(self.aws_events_role_arn).encode(), "text/plain")
        )
        aws_workflow_starter_lambda_arn = (
            self.aws_workflow_starter_lambda_arn
            if isinstance(self.aws_workflow_starter_lambda_arn, Unset)
            else (None, str(self.aws_workflow_starter_lambda_arn).encode(), "text/plain")
        )
        aws_workflow_starter_access_key = (
            self.aws_workflow_starter_access_key
            if isinstance(self.aws_workflow_starter_access_key, Unset)
            else (None, str(self.aws_workflow_starter_access_key).encode(), "text/plain")
        )
        default_alert_methods: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.default_alert_methods, Unset):
            _temp_default_alert_methods = []
            for default_alert_methods_item_data in self.default_alert_methods:
                default_alert_methods_item = default_alert_methods_item_data.to_dict()

                _temp_default_alert_methods.append(default_alert_methods_item)
            default_alert_methods = (None, json.dumps(_temp_default_alert_methods).encode(), "application/json")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "url": url,
                "uuid": uuid,
                "name": name,
                "dashboard_url": dashboard_url,
                "created_by_user": created_by_user,
                "created_by_group": created_by_group,
                "created_at": created_at,
                "updated_at": updated_at,
                "execution_method_capabilities": execution_method_capabilities,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if aws_account_id is not UNSET:
            field_dict["aws_account_id"] = aws_account_id
        if aws_default_region is not UNSET:
            field_dict["aws_default_region"] = aws_default_region
        if aws_access_key is not UNSET:
            field_dict["aws_access_key"] = aws_access_key
        if aws_assumed_role_external_id is not UNSET:
            field_dict["aws_assumed_role_external_id"] = aws_assumed_role_external_id
        if aws_events_role_arn is not UNSET:
            field_dict["aws_events_role_arn"] = aws_events_role_arn
        if aws_workflow_starter_lambda_arn is not UNSET:
            field_dict["aws_workflow_starter_lambda_arn"] = aws_workflow_starter_lambda_arn
        if aws_workflow_starter_access_key is not UNSET:
            field_dict["aws_workflow_starter_access_key"] = aws_workflow_starter_access_key
        if default_alert_methods is not UNSET:
            field_dict["default_alert_methods"] = default_alert_methods

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        uuid = d.pop("uuid")

        name = d.pop("name")

        dashboard_url = d.pop("dashboard_url")

        created_by_user = d.pop("created_by_user")

        created_by_group = Group.from_dict(d.pop("created_by_group"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        execution_method_capabilities = []
        _execution_method_capabilities = d.pop("execution_method_capabilities")
        for execution_method_capabilities_item_data in _execution_method_capabilities:
            execution_method_capabilities_item = AwsEcsRunEnvironmentExecutionMethodCapability.from_dict(
                execution_method_capabilities_item_data
            )

            execution_method_capabilities.append(execution_method_capabilities_item)

        description = d.pop("description", UNSET)

        aws_account_id = d.pop("aws_account_id", UNSET)

        aws_default_region = d.pop("aws_default_region", UNSET)

        aws_access_key = d.pop("aws_access_key", UNSET)

        aws_assumed_role_external_id = d.pop("aws_assumed_role_external_id", UNSET)

        aws_events_role_arn = d.pop("aws_events_role_arn", UNSET)

        aws_workflow_starter_lambda_arn = d.pop("aws_workflow_starter_lambda_arn", UNSET)

        aws_workflow_starter_access_key = d.pop("aws_workflow_starter_access_key", UNSET)

        default_alert_methods = []
        _default_alert_methods = d.pop("default_alert_methods", UNSET)
        for default_alert_methods_item_data in _default_alert_methods or []:
            default_alert_methods_item = NameAndUuid.from_dict(default_alert_methods_item_data)

            default_alert_methods.append(default_alert_methods_item)

        run_environment = cls(
            url=url,
            uuid=uuid,
            name=name,
            dashboard_url=dashboard_url,
            created_by_user=created_by_user,
            created_by_group=created_by_group,
            created_at=created_at,
            updated_at=updated_at,
            execution_method_capabilities=execution_method_capabilities,
            description=description,
            aws_account_id=aws_account_id,
            aws_default_region=aws_default_region,
            aws_access_key=aws_access_key,
            aws_assumed_role_external_id=aws_assumed_role_external_id,
            aws_events_role_arn=aws_events_role_arn,
            aws_workflow_starter_lambda_arn=aws_workflow_starter_lambda_arn,
            aws_workflow_starter_access_key=aws_workflow_starter_access_key,
            default_alert_methods=default_alert_methods,
        )

        run_environment.additional_properties = d
        return run_environment

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
