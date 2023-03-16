import subprocess
import json

tags_to_add = dict(company="cv",
                   environment="prod",
                   ict_digital="digital",
                   in_service="yes",
                   ito_provider="acn",
                   application_owner="fabio.ricciato@ivecogroup.com",
                   business_unit="cv-digital",
                   is_shared="no",
                   sharing_target_bu="cv-digital",
                   sharing_target_bu_prc="100",
                   sharing_target_app_prc="100",
                   application_name="cvv",
                   sharing_target_app="cvv",
                   databricks_team="ds-digital",
                   databricks_owner="davide.colombi@external.ivecogroup.com")



def run_reset_for_job(job_id):
    '''
    :param job_id:
    :return: update tags of given databricks job_id
    '''

    print('Tagging job: ', job_id)
    new_json = dict()

    # get command -> get jobs settings
    get_job = subprocess.run(['databricks', 'jobs', 'get', '--job-id', job_id], stdout=subprocess.PIPE)

    # build new json string with new tags
    json_string = get_job.stdout.decode('utf-8')
    job_json = json.loads(json_string)
    new_json['new_settings'] = job_json['settings']
    new_json['new_settings']['tags'] = tags_to_add
    json_reset_string = json.dumps(new_json)

    # reset command -> update tags
    result = subprocess.run(['databricks', 'jobs', 'reset', '--job-id', job_id, '--json', json_reset_string],
                            stdout=subprocess.PIPE)

    # out = result.stdout.decode('utf-8')

def main(test=True):

    # IF TESTING INPUT THE JOB_ID
    if test:
        print('insert job id:' )
        job_ids = input()
        run_reset_for_job(job_ids)

    # ELSE UPDATE ALL THE JOBS PRESENT IN DATABRICKS
    else:

        # list all jobs id
        result = subprocess.run(['databricks', 'jobs', 'list', '--all'], stdout=subprocess.PIPE)
        res_string = result.stdout.decode('utf-8')
        lines = res_string.split('\n')
        job_ids = [line.split(' ')[0] for line in lines]
        job_ids = job_ids[0:len(job_ids) - 1]                # last line is empty

        print("Tagging ", len(job_ids), "jobs")

        for job_id in job_ids:
            run_reset_for_job(job_id)
    return


if __name__ == '__main__':
    main(test=True)
