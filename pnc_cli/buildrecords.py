from argh import arg

import pnc_cli.common as common
import pnc_cli.types as types
import pnc_cli.utils as utils
from pnc_cli.swagger_client import BuildrecordsApi
from pnc_cli.swagger_client import BuildconfigurationsApi
from pnc_cli.swagger_client import ProjectsApi

client = utils.get_api_client()
records_api = BuildrecordsApi(client)
configs_api = BuildconfigurationsApi(client)
projects_api = ProjectsApi(client)

@arg("-p", "--page-size", help="Limit the amount of BuildRecords returned", type=int)
@arg("-s", "--sort", help="Sorting RSQL")
@arg("-q", help="RSQL query")
def list_build_records(page_size=200, sort="", q=""):
    """
    List all BuildRecords
    """
    response = utils.checked_api_call(records_api, 'get_all', page_size=page_size, sort=sort, q=q)
    if response:
        return response.content


@arg("-i", "--id", help="BuildConfiguration ID to retrieve BuildRecords of.", type=types.existing_bc_id)
@arg("-n", "--name", help="BuildConfiguration name to retrieve BuildRecords of.", type=types.existing_bc_name)
@arg("-p", "--page-size", help="Limit the amount of BuildRecords returned", type=int)
@arg("-s", "--sort", help="Sorting RSQL")
@arg("-q", help="RSQL query")
def list_records_for_build_configuration(id=None, name=None, page_size=200, sort="", q=""):
    """
    List all BuildRecords for a given BuildConfiguration
    """
    config_id = common.set_id(configs_api, id, name)
    response = utils.checked_api_call(records_api, 'get_all_for_build_configuration', configuration_id=config_id,
                                      page_size=page_size, sort=sort, q=q)
    if response:
        return response.content


@arg("-i", "--id", help="Project ID to retrieve BuildRecords of.")
@arg("-n", "--name", help="Project name to retrieve BuildRecords of.")
@arg("-p", "--page-size", help="Limit the amount of BuildRecords returned")
@arg("-s", "--sort", help="Sorting RSQL")
@arg("-q", help="RSQL query")
def list_records_for_project(id=None, name=None, page_size=200, sort="", q=""):
    """
    List all BuildRecords for a given Project
    """
    project_id = common.set_id(projects_api, id, name)
    response = utils.checked_api_call(records_api, 'get_all_for_project', project_id=project_id, page_size=page_size,
                                      sort=sort, q=q)
    if response:
        return response.content


@arg("id", help="BuildRecord ID to retrieve.", type=types.existing_build_record)
def get_build_record(id):
    """
    Get a specific BuildRecord by ID
    """
    response = utils.checked_api_call(records_api, 'get_specific', id=id)
    if response:
        return response.content


@arg("id", help="BuildRecord ID to retrieve artifacts from.", type=types.existing_build_record)
@arg("-p", "--page-size", help="Limit the amount of Artifacts returned", type=int)
@arg("-s", "--sort", help="Sorting RSQL")
@arg("-q", help="RSQL query")
def list_built_artifacts(id, page_size=200, sort="", q=""):
    """
    List Artifacts associated with a BuildRecord
    """
    response = utils.checked_api_call(records_api, 'get_built_artifacts', id=id, page_size=page_size, sort=sort, q=q)
    if response:
        return response.content


@arg("id", help="BuildRecord ID to retrieve dependency Artifacts from.", type=types.existing_build_record)
@arg("-p", "--page-size", help="Limit the amount of Artifacts returned", type=int)
@arg("-s", "--sort", help="Sorting RSQL")
@arg("-q", help="RSQL query")
def list_dependency_artifacts(id, page_size=200, sort="", q=""):
    """
    List dependency artifacts associated with a BuildRecord
    """
    response = utils.checked_api_call(records_api, 'get_dependency_artifacts', id=id, page_size=page_size, sort=sort,
                                      q=q)
    if response:
        return response.content


@arg("id", help="BuildRecord ID to retrieve audited BuildConfiguration from.", type=types.existing_build_record)
def get_audited_configuration_for_record(id):
    """
    Get the BuildConfigurationAudited for a given BuildRecord
    """
    response = utils.checked_api_call(records_api, 'get_build_configuration_audited', id=id)
    if response:
        return response.content


@arg("id", help="BuildRecord ID to retrieve the log from.", type=types.existing_build_record)
def get_log_for_record(id):
    """
    Get the log for a given BuildRecord
    """
    response = utils.checked_api_call(records_api, 'get_logs', id=id)
    if response:
        return response


@arg("id", help="BuildRecord ID to retrieve Artifacts from.", type=types.existing_build_record)
@arg("-p", "--page-size", help="Limit the amount of Artifacts returned", type=int)
@arg("-s", "--sort", help="Sorting RSQL")
@arg("-q", help="RSQL query")
def get_artifacts(id, page_size=200, sort="", q=""):
    response = utils.checked_api_call(records_api, 'get_artifacts', id=id, page_size=page_size, sort=sort, q=q)
    if response:
        return response.content
