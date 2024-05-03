"""Tests for the ShowcaseService class."""

# PyTest
import pytest
from unittest.mock import create_autospec

from backend.services.exceptions import (
    UserPermissionException,
    ResourceNotFoundException,
)

# Tested Dependencies
from ...models import ShowcaseProject
from ...services import ShowcaseService

# Injected Service Fixtures
from .fixtures import showcase_svc_integration

# Explicitly import Data Fixture to load entities in database
from .core_data import setup_insert_data_fixture

# Data Models for Fake Data Inserted in Setup
from .showcase_data import (
    showcases,
    post1,
    ugs,
    wc,
    to_add,
    updated_wc,
    to_add_conflicting_id,
)
from .user_data import root, user, ambassador

# Test Functions

# Test `ShowcaseService.get_showcases()`


def test_get_showcases(showcase_svc_integration: ShowcaseService):
    """Test that all showcases can be retrieved."""
    fetched_showcases = showcase_svc_integration.get_showcases()
    assert fetched_showcases is not None
    assert len(fetched_showcases) == len(showcases)
    assert isinstance(fetched_showcases[0], ShowcaseProject)


# Test `ShowcaseService.get_showcase()`


def test_get_showcase(showcase_svc_integration: ShowcaseService):
    """Test that showcases can be retrieved based on their ID."""
    fetched_showcase = showcase_svc_integration.get_showcase(wc.id)
    assert fetched_showcase is not None
    assert isinstance(fetched_showcase, ShowcaseProject)
    assert fetched_showcase.id == wc.id


# Test `ShowcaseService.create_showcase()`


def test_create_showcase_as_user(showcase_svc_integration: ShowcaseService):
    """Test that any user is able to create new organizations."""
    created_showcase = showcase_svc_integration.create_showcase(user, to_add)
    assert created_showcase is not None
    assert created_showcase.id is not None


def test_create_showcase_id_already_exists(
    showcase_svc_integration: ShowcaseService,
):
    """Test that a user is able to create new organizations when an extraneous ID is provided."""
    created_organization = showcase_svc_integration.create_showcase(
        user, to_add_conflicting_id
    )
    assert created_organization is not None
    assert created_organization.id is not None


# Test `ShowcaseService.modify_showcase()`


def test_modify_showcase_as_root(
    showcase_svc_integration: ShowcaseService,
):
    """Test that the root user is able to update any showcase even one they are not the author of"""
    showcase_svc_integration.modify_showcase(root, updated_wc)
    assert (
        showcase_svc_integration.get_showcase(updated_wc.id).title
        == "Water Conservation EDITED"
    )


def test_modify_showcase_as_author(showcase_svc_integration: ShowcaseService):
    """Test that author is able to update showcases they wrote"""
    showcase_svc_integration.modify_showcase(user, updated_wc)
    assert (
        showcase_svc_integration.get_showcase(updated_wc.id).title
        == "Water Conservation EDITED"
    )


def test_modify_showcase_as_not_author(
    showcase_svc_integration: ShowcaseService,
):
    """Test that any non-author (except root) is not able to update new organizations."""
    with pytest.raises(UserPermissionException):
        showcase_svc_integration.modify_showcase(ambassador, updated_wc)


def test_modify_showcase_does_not_exist(
    showcase_svc_integration: ShowcaseService,
):
    """Test updating a showcase that does not exist."""
    with pytest.raises(ResourceNotFoundException):
        showcase_svc_integration.modify_showcase(user, to_add)


# Test `ShowcaseService.remove_showcase()`


def test_remove_showcase_as_root(showcase_svc_integration: ShowcaseService):
    """Test that the root user is able to delete any showcase (even ones they did not author)."""
    size = len(showcase_svc_integration.get_showcases())
    deleted_showcase = showcase_svc_integration.remove_showcase(root, post1.id)
    assert len(showcase_svc_integration.get_showcases()) == size - 1
    with pytest.raises(ResourceNotFoundException):
        showcase_svc_integration.remove_showcase(user, deleted_showcase.id)


def test_remove_showcase_as_not_author(showcase_svc_integration: ShowcaseService):
    """Test that a non-author is not able to delete showcase postst they did not write"""
    with pytest.raises(UserPermissionException):
        showcase_svc_integration.remove_showcase(ambassador, ugs.id)


def test_remove_showcase_as_author(showcase_svc_integration: ShowcaseService):
    """Test that an author is able to delete their own showcases"""
    size = len(showcase_svc_integration.get_showcases())
    deleted_showcase = showcase_svc_integration.remove_showcase(user, ugs.id)
    assert len(showcase_svc_integration.get_showcases()) == size - 1
    with pytest.raises(ResourceNotFoundException):
        showcase_svc_integration.remove_showcase(user, deleted_showcase.id)


def test_delete_organization_does_not_exist(
    showcase_svc_integration: ShowcaseService,
):
    """Test deleting a showcase that does not exist."""
    with pytest.raises(ResourceNotFoundException):
        showcase_svc_integration.remove_showcase(user, to_add.id)
