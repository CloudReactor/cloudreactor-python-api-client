import datetime
import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.name_and_uuid import NameAndUuid
from ..models.rule_type_enum import RuleTypeEnum
from ..models.threshold_property_enum import ThresholdPropertyEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkflowTransition")


@attr.s(auto_attribs=True)
class WorkflowTransition:
    """A WorkflowTransition is a directed edge in a Worfklow, which is a directed
    graph. It contains a source WorkflowTaskInstance, a destination
    WorkflowTaskInstance, as well as conditions for triggering the destination
    to execution.

        Attributes:
            url (str):
            uuid (str):
            from_workflow_task_instance (NameAndUuid): Identifies an entity in three ways: 1. UUID; 2. Name; and 3. URL.
                When used to indentify an entity in a request method body, only one of
                uuid and name needs to be specified. If both are present, they must
                refer to the same entity or else the response will be a 400 error.
            to_workflow_task_instance (NameAndUuid): Identifies an entity in three ways: 1. UUID; 2. Name; and 3. URL.
                When used to indentify an entity in a request method body, only one of
                uuid and name needs to be specified. If both are present, they must
                refer to the same entity or else the response will be a 400 error.
            rule_type (RuleTypeEnum):
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
            description (Union[Unset, str]):
            exit_codes (Union[Unset, None, List[str]]):
            threshold_property (Union[Unset, ThresholdPropertyEnum]):
            custom_expression (Union[Unset, str]):
            priority (Union[Unset, None, int]):
            ui_color (Union[Unset, str]):
            ui_line_style (Union[Unset, str]):
            ui_scale (Union[Unset, None, float]):
    """

    url: str
    uuid: str
    from_workflow_task_instance: NameAndUuid
    to_workflow_task_instance: NameAndUuid
    rule_type: RuleTypeEnum
    created_at: datetime.datetime
    updated_at: datetime.datetime
    description: Union[Unset, str] = UNSET
    exit_codes: Union[Unset, None, List[str]] = UNSET
    threshold_property: Union[Unset, ThresholdPropertyEnum] = UNSET
    custom_expression: Union[Unset, str] = UNSET
    priority: Union[Unset, None, int] = UNSET
    ui_color: Union[Unset, str] = UNSET
    ui_line_style: Union[Unset, str] = UNSET
    ui_scale: Union[Unset, None, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        uuid = self.uuid
        from_workflow_task_instance = self.from_workflow_task_instance.to_dict()

        to_workflow_task_instance = self.to_workflow_task_instance.to_dict()

        rule_type = self.rule_type.value

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        description = self.description
        exit_codes: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.exit_codes, Unset):
            if self.exit_codes is None:
                exit_codes = None
            else:
                exit_codes = self.exit_codes

        threshold_property: Union[Unset, str] = UNSET
        if not isinstance(self.threshold_property, Unset):
            threshold_property = self.threshold_property.value

        custom_expression = self.custom_expression
        priority = self.priority
        ui_color = self.ui_color
        ui_line_style = self.ui_line_style
        ui_scale = self.ui_scale

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "uuid": uuid,
                "from_workflow_task_instance": from_workflow_task_instance,
                "to_workflow_task_instance": to_workflow_task_instance,
                "rule_type": rule_type,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if exit_codes is not UNSET:
            field_dict["exit_codes"] = exit_codes
        if threshold_property is not UNSET:
            field_dict["threshold_property"] = threshold_property
        if custom_expression is not UNSET:
            field_dict["custom_expression"] = custom_expression
        if priority is not UNSET:
            field_dict["priority"] = priority
        if ui_color is not UNSET:
            field_dict["ui_color"] = ui_color
        if ui_line_style is not UNSET:
            field_dict["ui_line_style"] = ui_line_style
        if ui_scale is not UNSET:
            field_dict["ui_scale"] = ui_scale

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        url = self.url if isinstance(self.url, Unset) else (None, str(self.url).encode(), "text/plain")
        uuid = self.uuid if isinstance(self.uuid, Unset) else (None, str(self.uuid).encode(), "text/plain")
        from_workflow_task_instance = (
            None,
            json.dumps(self.from_workflow_task_instance.to_dict()).encode(),
            "application/json",
        )

        to_workflow_task_instance = (
            None,
            json.dumps(self.to_workflow_task_instance.to_dict()).encode(),
            "application/json",
        )

        rule_type = (None, str(self.rule_type.value).encode(), "text/plain")

        created_at = self.created_at.isoformat().encode()

        updated_at = self.updated_at.isoformat().encode()

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )
        exit_codes: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.exit_codes, Unset):
            if self.exit_codes is None:
                exit_codes = None
            else:
                _temp_exit_codes = self.exit_codes
                exit_codes = (None, json.dumps(_temp_exit_codes).encode(), "application/json")

        threshold_property: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.threshold_property, Unset):
            threshold_property = (None, str(self.threshold_property.value).encode(), "text/plain")

        custom_expression = (
            self.custom_expression
            if isinstance(self.custom_expression, Unset)
            else (None, str(self.custom_expression).encode(), "text/plain")
        )
        priority = (
            self.priority if isinstance(self.priority, Unset) else (None, str(self.priority).encode(), "text/plain")
        )
        ui_color = (
            self.ui_color if isinstance(self.ui_color, Unset) else (None, str(self.ui_color).encode(), "text/plain")
        )
        ui_line_style = (
            self.ui_line_style
            if isinstance(self.ui_line_style, Unset)
            else (None, str(self.ui_line_style).encode(), "text/plain")
        )
        ui_scale = (
            self.ui_scale if isinstance(self.ui_scale, Unset) else (None, str(self.ui_scale).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "url": url,
                "uuid": uuid,
                "from_workflow_task_instance": from_workflow_task_instance,
                "to_workflow_task_instance": to_workflow_task_instance,
                "rule_type": rule_type,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if exit_codes is not UNSET:
            field_dict["exit_codes"] = exit_codes
        if threshold_property is not UNSET:
            field_dict["threshold_property"] = threshold_property
        if custom_expression is not UNSET:
            field_dict["custom_expression"] = custom_expression
        if priority is not UNSET:
            field_dict["priority"] = priority
        if ui_color is not UNSET:
            field_dict["ui_color"] = ui_color
        if ui_line_style is not UNSET:
            field_dict["ui_line_style"] = ui_line_style
        if ui_scale is not UNSET:
            field_dict["ui_scale"] = ui_scale

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        uuid = d.pop("uuid")

        from_workflow_task_instance = NameAndUuid.from_dict(d.pop("from_workflow_task_instance"))

        to_workflow_task_instance = NameAndUuid.from_dict(d.pop("to_workflow_task_instance"))

        rule_type = RuleTypeEnum(d.pop("rule_type"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        description = d.pop("description", UNSET)

        exit_codes = cast(List[str], d.pop("exit_codes", UNSET))

        _threshold_property = d.pop("threshold_property", UNSET)
        threshold_property: Union[Unset, ThresholdPropertyEnum]
        if isinstance(_threshold_property, Unset):
            threshold_property = UNSET
        else:
            threshold_property = ThresholdPropertyEnum(_threshold_property)

        custom_expression = d.pop("custom_expression", UNSET)

        priority = d.pop("priority", UNSET)

        ui_color = d.pop("ui_color", UNSET)

        ui_line_style = d.pop("ui_line_style", UNSET)

        ui_scale = d.pop("ui_scale", UNSET)

        workflow_transition = cls(
            url=url,
            uuid=uuid,
            from_workflow_task_instance=from_workflow_task_instance,
            to_workflow_task_instance=to_workflow_task_instance,
            rule_type=rule_type,
            created_at=created_at,
            updated_at=updated_at,
            description=description,
            exit_codes=exit_codes,
            threshold_property=threshold_property,
            custom_expression=custom_expression,
            priority=priority,
            ui_color=ui_color,
            ui_line_style=ui_line_style,
            ui_scale=ui_scale,
        )

        workflow_transition.additional_properties = d
        return workflow_transition

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
