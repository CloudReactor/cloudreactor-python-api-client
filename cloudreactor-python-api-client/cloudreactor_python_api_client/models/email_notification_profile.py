import datetime
import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.group import Group
from ..models.name_and_uuid import NameAndUuid
from ..types import UNSET, Unset

T = TypeVar("T", bound="EmailNotificationProfile")


@attr.s(auto_attribs=True)
class EmailNotificationProfile:
    """An EmailProfile contains settings for emailing notifications.

    Attributes:
        url (str):
        uuid (str):
        name (str):
        dashboard_url (str):
        created_by_user (str): Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.
        created_by_group (Group):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        description (Union[Unset, str]):
        run_environment (Union[Unset, None, NameAndUuid]): Identifies an entity in three ways: 1. UUID; 2. Name; and 3.
            URL.
            When used to indentify an entity in a request method body, only one of
            uuid and name needs to be specified. If both are present, they must
            refer to the same entity or else the response will be a 400 error.
        to_addresses (Union[Unset, None, List[str]]):
        cc_addresses (Union[Unset, None, List[str]]):
        bcc_addresses (Union[Unset, None, List[str]]):
        subject_template (Union[Unset, str]):
        body_template (Union[Unset, str]):
    """

    url: str
    uuid: str
    name: str
    dashboard_url: str
    created_by_user: str
    created_by_group: Group
    created_at: datetime.datetime
    updated_at: datetime.datetime
    description: Union[Unset, str] = UNSET
    run_environment: Union[Unset, None, NameAndUuid] = UNSET
    to_addresses: Union[Unset, None, List[str]] = UNSET
    cc_addresses: Union[Unset, None, List[str]] = UNSET
    bcc_addresses: Union[Unset, None, List[str]] = UNSET
    subject_template: Union[Unset, str] = UNSET
    body_template: Union[Unset, str] = UNSET
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

        description = self.description
        run_environment: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.run_environment, Unset):
            run_environment = self.run_environment.to_dict() if self.run_environment else None

        to_addresses: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.to_addresses, Unset):
            if self.to_addresses is None:
                to_addresses = None
            else:
                to_addresses = self.to_addresses

        cc_addresses: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.cc_addresses, Unset):
            if self.cc_addresses is None:
                cc_addresses = None
            else:
                cc_addresses = self.cc_addresses

        bcc_addresses: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.bcc_addresses, Unset):
            if self.bcc_addresses is None:
                bcc_addresses = None
            else:
                bcc_addresses = self.bcc_addresses

        subject_template = self.subject_template
        body_template = self.body_template

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
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if run_environment is not UNSET:
            field_dict["run_environment"] = run_environment
        if to_addresses is not UNSET:
            field_dict["to_addresses"] = to_addresses
        if cc_addresses is not UNSET:
            field_dict["cc_addresses"] = cc_addresses
        if bcc_addresses is not UNSET:
            field_dict["bcc_addresses"] = bcc_addresses
        if subject_template is not UNSET:
            field_dict["subject_template"] = subject_template
        if body_template is not UNSET:
            field_dict["body_template"] = body_template

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

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )
        run_environment: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.run_environment, Unset):
            run_environment = (
                (None, json.dumps(self.run_environment.to_dict()).encode(), "application/json")
                if self.run_environment
                else None
            )

        to_addresses: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.to_addresses, Unset):
            if self.to_addresses is None:
                to_addresses = None
            else:
                _temp_to_addresses = self.to_addresses
                to_addresses = (None, json.dumps(_temp_to_addresses).encode(), "application/json")

        cc_addresses: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.cc_addresses, Unset):
            if self.cc_addresses is None:
                cc_addresses = None
            else:
                _temp_cc_addresses = self.cc_addresses
                cc_addresses = (None, json.dumps(_temp_cc_addresses).encode(), "application/json")

        bcc_addresses: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.bcc_addresses, Unset):
            if self.bcc_addresses is None:
                bcc_addresses = None
            else:
                _temp_bcc_addresses = self.bcc_addresses
                bcc_addresses = (None, json.dumps(_temp_bcc_addresses).encode(), "application/json")

        subject_template = (
            self.subject_template
            if isinstance(self.subject_template, Unset)
            else (None, str(self.subject_template).encode(), "text/plain")
        )
        body_template = (
            self.body_template
            if isinstance(self.body_template, Unset)
            else (None, str(self.body_template).encode(), "text/plain")
        )

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
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if run_environment is not UNSET:
            field_dict["run_environment"] = run_environment
        if to_addresses is not UNSET:
            field_dict["to_addresses"] = to_addresses
        if cc_addresses is not UNSET:
            field_dict["cc_addresses"] = cc_addresses
        if bcc_addresses is not UNSET:
            field_dict["bcc_addresses"] = bcc_addresses
        if subject_template is not UNSET:
            field_dict["subject_template"] = subject_template
        if body_template is not UNSET:
            field_dict["body_template"] = body_template

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

        description = d.pop("description", UNSET)

        _run_environment = d.pop("run_environment", UNSET)
        run_environment: Union[Unset, None, NameAndUuid]
        if _run_environment is None:
            run_environment = None
        elif isinstance(_run_environment, Unset):
            run_environment = UNSET
        else:
            run_environment = NameAndUuid.from_dict(_run_environment)

        to_addresses = cast(List[str], d.pop("to_addresses", UNSET))

        cc_addresses = cast(List[str], d.pop("cc_addresses", UNSET))

        bcc_addresses = cast(List[str], d.pop("bcc_addresses", UNSET))

        subject_template = d.pop("subject_template", UNSET)

        body_template = d.pop("body_template", UNSET)

        email_notification_profile = cls(
            url=url,
            uuid=uuid,
            name=name,
            dashboard_url=dashboard_url,
            created_by_user=created_by_user,
            created_by_group=created_by_group,
            created_at=created_at,
            updated_at=updated_at,
            description=description,
            run_environment=run_environment,
            to_addresses=to_addresses,
            cc_addresses=cc_addresses,
            bcc_addresses=bcc_addresses,
            subject_template=subject_template,
            body_template=body_template,
        )

        email_notification_profile.additional_properties = d
        return email_notification_profile

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
