import pytest
import os
from dxm.lib.DxJobs import jobs_worker
from dxm.lib.DxColumn import column_worker
from dxm.lib.DxEngine.DxConfig import DxConfig
from dxm.lib.DxLogging import logging_est


CONFIGPATH='./test/testdb.db'
ALGNAME1="dlpx-core:FirstName"
RULESETNAME="rs_test_1"
ENVNAME="env1"
JOBNAME="job1"
METANAME3="EMPLOYEES"
COLUMNNAME1="FIRST_NAME"
ALGNAME1="dlpx-core:FirstName"
DOMAINNAME="FIRST_NAME"

#logging_est('dxm.log', True)

@pytest.fixture(autouse=True)
def open_config_file():
    DxConfig(CONFIGPATH)


def test_column_set_masking(capsys):
    rc = column_worker.column_setmasking(
        p_engine="test_eng",
        p_username=None,
        rulesetname=RULESETNAME,
        envname=None,
        metaname=METANAME3,
        columnname=COLUMNNAME1,
        algname=ALGNAME1,
        domainname=DOMAINNAME,
        dateformat=None,
        idmethod=None
    )

    output = "Column FIRST_NAME updated\n" + \
        "Algorithm dlpx-core:FirstName domain FIRST_NAME updated for ruleset rs_test_1 meta EMPLOYEES column FIRST_NAME\n"
    captured = capsys.readouterr()
    assert (rc, captured.out.replace('\r','')) == (0, output)    


@pytest.mark.dependency()
def test_job_list_ignore(capsys):
    rc = jobs_worker.jobs_list(
        p_engine="test_eng",
        p_username=None,
        p_format="csv",
        envname=ENVNAME,
        jobname=JOBNAME
    )

    if rc == 1:
        pytest.skip("Job non-exist")
    else:
        assert True

    


@pytest.mark.dependency(depends=['test_job_list_ignore'])
def test_environment_delete_old_env():
    rc = jobs_worker.job_delete(
        p_engine="test_eng",
        p_username=None,
        envname=ENVNAME,
        jobname=JOBNAME
    )

    assert rc == 0


def test_add_job_single(capsys):

    params = {}
    params['envname'] = ENVNAME
    params['jobname'] = JOBNAME
    params['rulesetname'] = RULESETNAME
    params['email'] = None
    params['feedback_size'] = None
    params['max_memory'] = None
    params['min_memory'] = None
    params['job_description'] = None
    params['num_input_streams'] = None
    params['on_the_fly_masking'] = None
    params['commit_size'] = None
    params['multi_tenant'] = None
    params['num_output_threads_per_stream'] = None
    params['batch_update'] = None
    params['bulk_data'] = None
    params['disable_constraints'] = None
    params['disable_triggers'] = None
    params['drop_indexes'] = None
    params['truncate_tables'] = None
    params['prescript'] = None
    params['postscript'] = None


    rc = jobs_worker.job_add(
        p_engine="test_eng",
        p_username=None,
        params = params
    )


    output = "Job {} added\n".format(JOBNAME)

    captured = capsys.readouterr()


    assert (rc, captured.out.replace("\r","")) == (0, output)



def test_job_list(capsys):
    rc = jobs_worker.jobs_list(
        p_engine="test_eng",
        p_username=None,
        p_format="csv",
        envname=ENVNAME,
        jobname=JOBNAME
    )


    assert rc == 0



def test_start_job_single(capsys):

    job_list = [ JOBNAME ]
        
    rc = jobs_worker.job_start(
        p_engine="test_eng",
        p_username=None,
        jobname = job_list,
        envname = None,
        tgt_connector = None,
        tgt_connector_env = None,
        nowait = None,
        monitor= None,
        parallel= 1
    )


    output = "Waiting for job job1 to start processing rows\n" + \
             "Job {} is processing rows\n".format(JOBNAME) + \
             "Masking job {} finished.\n".format(JOBNAME) + \
             "101 rows masked\n\n\n\n"

    captured = capsys.readouterr()


    assert (rc, captured.out.replace("\r","")) == (0, output)


def test_column_set_unmasking(capsys):
    rc = column_worker.column_unsetmasking(
        p_engine="test_eng",
        p_username=None,
        rulesetname=RULESETNAME,
        envname=None,
        metaname=METANAME3,
        columnname=COLUMNNAME1
    )

    output = "Column FIRST_NAME updated\n" + \
        "Algorithm None domain None updated for ruleset rs_test_1 meta EMPLOYEES column FIRST_NAME\n"
    captured = capsys.readouterr()
    assert (rc, captured.out.replace('\r','')) == (0, output)