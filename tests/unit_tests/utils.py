from unittest import mock

from requests.models import Response


def get_responses_gitlab_api_down():
    responses = []

    response1 = mock.Mock(spec=Response)
    response1.text = "{\"status_code\":500}"
    response1.status_code = 500
    response2 = mock.Mock(spec=Response)
    response2.text = "{\"status_code\":200}"
    response2.status_code = 200

    responses.append(response1)
    responses.append(response2)

    return responses


def get_response_mattermost():
    response = mock.Mock(spec=Response)
    response.text = "{\"status_code\":201}"
    response.status_code = 201

    return response


def get_response_project_id():
    response = mock.Mock(spec=Response)
    response.text = "[{\"id\":31240995,\"description\":null,\"name\":\"Mattermost-Coffeebot\",\"name_with_" \
                    "namespace\":\"Mattermost-IV/Mattermost-Coffeebot\",\"path\":\"Mattermost-Coffeeb" \
                    "ot\",\"path_with_namespace\":\"m5520/Mattermost-Coffeebot\",\"created_at\":\"2021-11-" \
                    "11T13:53:37.774Z\",\"default_branch\":\"master\",\"tag_list\":[],\"topics\":[],\"ssh_u" \
                    "rl_to_repo\":\"git@gitlab.com:m5520/Mattermost-Coffeebot.git\",\"http_url_to_repo\":\"" \
                    "https://gitlab.com/m5520/Mattermost-Coffeebot.git\",\"web_url\":\"https://gitlab.com/m5" \
                    "520/Mattermost-Coffeebot\",\"readme_url\":\"https://gitlab.com/m5520/Mattermost-Coffeeb" \
                    "ot/-/blob/master/README.md\",\"avatar_url\":null,\"forks_count\":0,\"star_count\":0," \
                    "\"last_activity_at\":\"2021-11-15T17:09:26.690Z\",\"namespace\":{\"id\":14108836,\"na" \
                    "me\":\"Mattermost-IV\",\"path\":\"m5520\",\"kind\":\"group\",\"full_path\":\"m5520\",\"" \
                    "parent_id\":null,\"avatar_url\":null,\"web_url\":\"https://gitlab.com/groups/m5520\"" \
                    "},\"container_registry_image_prefix\":\"registry.gitlab.com/m5520/mattermost-coffee" \
                    "bot\",\"_links\":{\"self\":\"https://gitlab.com/api/v4/projects/31240995\",\"issues\"" \
                    ":\"https://gitlab.com/api/v4/projects/31240995/issues\",\"merge_requests\":\"https:/" \
                    "/gitlab.com/api/v4/projects/31240995/merge_requests\",\"repo_branches\":\"https://git" \
                    "lab.com/api/v4/projects/31240995/repository/branches\",\"labels\":\"https://gitlab.com/" \
                    "api/v4/projects/31240995/labels\",\"events\":\"https://gitlab.com/api/v4/projects/31240995" \
                    "/events\",\"members\":\"https://gitlab.com/api/v4/projects/31240995/members\"},\"package" \
                    "s_enabled\":true,\"empty_repo\":false,\"archived\":false,\"visibility\":\"public\",\"r" \
                    "esolve_outdated_diff_discussions\":false,\"container_expiration_policy\":{\"cadence\":\"" \
                    "1d\",\"enabled\":false,\"keep_n\":10,\"older_than\":\"90d\",\"name_regex\":\".*\",\"n" \
                    "ame_regex_keep\":null,\"next_run_at\":\"2021-11-12T13:53:37.827Z\"},\"issues_enabled\"" \
                    ":true,\"merge_requests_enabled\":true,\"wiki_enabled\":true,\"jobs_enabled\":true,\"sni" \
                    "ppets_enabled\":true,\"container_registry_enabled\":true,\"service_desk_enabled\":true" \
                    ",\"service_desk_address\":\"contact-project+m5520-mattermost-coffeebot-31240995-issue-@" \
                    "incoming.gitlab.com\",\"can_create_merge_request_in\":true,\"issues_access_level\":\"en" \
                    "abled\",\"repository_access_level\":\"enabled\",\"merge_requests_access_level\":\"enabl" \
                    "ed\",\"forking_access_level\":\"enabled\",\"wiki_access_level\":\"enabled\",\"builds_ac" \
                    "cess_level\":\"enabled\",\"snippets_access_level\":\"enabled\",\"pages_access_level\":\"e" \
                    "nabled\",\"operations_access_level\":\"enabled\",\"analytics_access_level\":\"enable" \
                    "d\",\"container_registry_access_level\":\"enabled\",\"emails_disabled\":false,\"share" \
                    "d_runners_enabled\":true,\"lfs_enabled\":true,\"creator_id\":10195829,\"import_statu" \
                    "s\":\"none\",\"open_issues_count\":0,\"ci_default_git_depth\":50,\"ci_forward_deployme" \
                    "nt_enabled\":true,\"ci_job_token_scope_enabled\":false,\"public_jobs\":true,\"build_tim" \
                    "eout\":3600,\"auto_cancel_pending_pipelines\":\"enabled\",\"build_coverage_regex\":null" \
                    ",\"ci_config_path\":\"\",\"shared_with_groups\":[],\"only_allow_merge_if_pipeline_succe" \
                    "eds\":false,\"allow_merge_on_skipped_pipeline\":null,\"restrict_user_defined_variable" \
                    "s\":false,\"request_access_enabled\":true,\"only_allow_merge_if_all_discussions_are_re" \
                    "solved\":false,\"remove_source_branch_after_merge\":true,\"printing_merge_request_lin" \
                    "k_enabled\":true,\"merge_method\":\"merge\",\"squash_option\":\"default_off\",\"sugge" \
                    "stion_commit_message\":null,\"merge_commit_template\":null,\"auto_devops_enabled\":f" \
                    "alse,\"auto_devops_deploy_strategy\":\"continuous\",\"autoclose_referenced_issues\":t" \
                    "rue,\"keep_latest_artifact\":true,\"approvals_before_merge\":0,\"mirror\":false,\"ext" \
                    "ernal_authorization_classification_label\":\"\",\"marked_for_deletion_at\":null,\"ma" \
                    "rked_for_deletion_on\":null,\"requirements_enabled\":true,\"security_and_compliance" \
                    "_enabled\":true,\"compliance_frameworks\":[],\"issues_template\":null,\"merge_reque" \
                    "sts_template\":null,\"merge_pipelines_enabled\":false,\"merge_trains_enabled\":fals" \
                    "e,\"permissions\":{\"project_access\":null,\"group_access\":{\"access_level\":50,\"not" \
                    "ification_level\":3}}}]"
    response.status_code = 200

    return response


def get_response_issue_id():
    response = mock.Mock(spec=Response)
    response.text = "[{\"id\":97802049,\"iid\":6,\"project_id\":31240995,\"title\":\"API_ERROR\",\"description" \
                    "\":\"\",\"state\":\"opened\",\"created_at\":\"2021-11-23T11:39:54.267Z\",\"updated_" \
                    "at\":\"2021-11-23T11:39:54.267Z\",\"closed_at\":null,\"closed_by\":null,\"labels\":[" \
                    "],\"milestone\":null,\"assignees\":[],\"author\":{\"id\":10195829,\"name\":\"PyHelpe" \
                    "r\",\"username\":\"PyHelper\",\"state\":\"active\",\"avatar_url\":\"https://secure.gr" \
                    "avatar.com/avatar/fed8cb82c04c562f2580b10dbfc3a53b?s=80&d=identicon\",\"web_url\":\"htt" \
                    "ps://gitlab.com/PyHelper\"},\"type\":\"ISSUE\",\"assignee\":null,\"user_notes_count\":0" \
                    ",\"merge_requests_count\":0,\"upvotes\":0,\"downvotes\":0,\"due_date\":null,\"confident" \
                    "ial\":false,\"discussion_locked\":null,\"issue_type\":\"issue\",\"web_url\":\"https://gi" \
                    "tlab.com/m5520/Mattermost-Coffeebot/-/issues/6\",\"time_stats\":{\"time_estimate\":0,\"t" \
                    "otal_time_spent\":0,\"human_time_estimate\":null,\"human_total_time_spent\":null},\"task" \
                    "_completion_status\":{\"count\":0,\"completed_count\":0},\"weight\":null,\"blocking_issu" \
                    "es_count\":0,\"has_tasks\":false,\"_links\":{\"self\":\"https://gitlab.com/api/v4/projects" \
                    "/31240995/issues/6\",\"notes\":\"https://gitlab.com/api/v4/projects/31240995/issues/6/note" \
                    "s\",\"award_emoji\":\"https://gitlab.com/api/v4/projects/31240995/issues/6/award_emoji\",\"" \
                    "project\":\"https://gitlab.com/api/v4/projects/31240995\"},\"references\":{\"short\":\"#6\"" \
                    ",\"relative\":\"#6\",\"full\":\"m5520/Mattermost-Coffeebot#6\"},\"moved_to_id\":null,\"serv" \
                    "ice_desk_reply_to\":null,\"health_status\":null}]"
    response.status_code = 200

    return response


def get_response_issue_or_project_id_exception():
    response = mock.Mock(spec=Response)
    response.text = "[]"
    response.status_code = 200

    return response


def get_response_check_branch():
    response = mock.Mock(spec=Response)
    response.text = "{\"name\":\"master\",\"commit\":{\"id\":\"ffa254791534a16a9a6e8b06ad634db0d8969ac" \
                    "6\",\"short_id\":\"ffa25479\",\"created_at\":\"2021-11-11T14:58:01.000+01:00\",\"pa" \
                    "rent_ids\":[\"9f29c8fe387e141f20dcbdafaf12f7c450e211e3\"],\"title\":\"update\",\"me" \
                    "ssage\":\"update\\n\",\"author_name\":\"Lucas\",\"author_email\":\"lucas-at-59074914" \
                    "0953\",\"authored_date\":\"2021-11-11T14:58:01.000+01:00\",\"committer_name\":\"Luca" \
                    "s\",\"committer_email\":\"lucas-at-590749140953\",\"committed_date\":\"2021-11-11T14:" \
                    "58:01.000+01:00\",\"trailers\":{},\"web_url\":\"https://gitlab.com/m5520/Mattermost-C" \
                    "offeebot/-/commit/ffa254791534a16a9a6e8b06ad634db0d8969ac6\"},\"merged\":false,\"prote" \
                    "cted\":true,\"developers_can_push\":false,\"developers_can_merge\":false,\"can_push\":t" \
                    "rue,\"default\":true,\"web_url\":\"https://gitlab.com/m5520/Mattermost-Coffeebot/-/tree" \
                    "/master\"}"
    response.status_code = 200

    return response


def get_response_check_branch_exception():
    response = mock.Mock(spec=Response)
    response.text = "{\"status_code\":\"404\"}"
    response.status_code = 404

    return response


def get_response_create_mr():
    response = mock.Mock(spec=Response)
    response.text = "{\"id\":127413811,\"iid\":5,\"project_id\":31240995,\"title\":\"Test\",\"descript" \
                    "ion\":null,\"state\":\"opened\",\"created_at\":\"2021-11-23T12:08:58.755Z\",\"up" \
                    "dated_at\":\"2021-11-23T12:08:58.755Z\",\"merged_by\":null,\"merged_at\":null,\"cl" \
                    "osed_by\":null,\"closed_at\":null,\"target_branch\":\"dev\",\"source_branch\":\"ma" \
                    "ster\",\"user_notes_count\":0,\"upvotes\":0,\"downvotes\":0,\"author\":{\"id\":1019" \
                    "5829,\"name\":\"PyHelper\",\"username\":\"PyHelper\",\"state\":\"active\",\"avatar_" \
                    "url\":\"https://secure.gravatar.com/avatar/fed8cb82c04c562f2580b10dbfc3a53b?s=80&d=i" \
                    "denticon\",\"web_url\":\"https://gitlab.com/PyHelper\"},\"assignees\":[],\"assignee\":n" \
                    "ull,\"reviewers\":[],\"source_project_id\":31240995,\"target_project_id\":31240995,\"l" \
                    "abels\":[],\"draft\":false,\"work_in_progress\":false,\"milestone\":null,\"merge_when_" \
                    "pipeline_succeeds\":false,\"merge_status\":\"checking\",\"sha\":\"ffa254791534a16a9a6e" \
                    "8b06ad634db0d8969ac6\",\"merge_commit_sha\":null,\"squash_commit_sha\":null,\"discussio" \
                    "n_locked\":null,\"should_remove_source_branch\":null,\"force_remove_source_branch\":nul" \
                    "l,\"reference\":\"!5\",\"references\":{\"short\":\"!5\",\"relative\":\"!5\",\"full\":\"m5" \
                    "520/Mattermost-Coffeebot!5\"},\"web_url\":\"https://gitlab.com/m5520/Mattermost-Coffeebo" \
                    "t/-/merge_requests/5\",\"time_stats\":{\"time_estimate\":0,\"total_time_spent\":0,\"human_t" \
                    "ime_estimate\":null,\"human_total_time_spent\":null},\"squash\":false,\"task_completion_st" \
                    "atus\":{\"count\":0,\"completed_count\":0},\"has_conflicts\":false,\"blocking_discussions" \
                    "_resolved\":true,\"approvals_before_merge\":null,\"subscribed\":true,\"changes_count\":n" \
                    "ull,\"latest_build_started_at\":null,\"latest_build_finished_at\":null,\"first_deployed_t" \
                    "o_production_at\":null,\"pipeline\":null,\"head_pipeline\":null,\"diff_refs\":{\"base_sha" \
                    "\":\"ffa254791534a16a9a6e8b06ad634db0d8969ac6\",\"head_sha\":\"ffa254791534a16a9a6e8b06ad" \
                    "634db0d8969ac6\",\"start_sha\":\"0ab64d9d2b84406fd9164006ed706f7359afafa7\"},\"merge_erro" \
                    "r\":null,\"user\":{\"can_merge\":true}}"
    response.status_code = 201

    return response


def get_response_mr_already_exists():
    response = mock.Mock(spec=Response)
    response.text = "{\"message\":[\"Another open merge request already exists for this source branch: !5\"]}"
    response.status_code = 409

    return response


def get_response_create_r():
    response = mock.Mock(spec=Response)
    response.text = "{\"name\":\"Test\",\"tag_name\":\"v4.0\",\"description\":null,\"created_at\":\"2021-11-23" \
                    "T13:53:15.414Z\",\"released_at\":\"2021-11-23T13:53:15.414Z\",\"author\":{\"id\":101958" \
                    "29,\"name\":\"PyHelper\",\"username\":\"PyHelper\",\"state\":\"active\",\"avatar_url\":\"ht" \
                    "tps://secure.gravatar.com/avatar/fed8cb82c04c562f2580b10dbfc3a53b?s=80&d=identicon\",\"web" \
                    "_url\":\"https://gitlab.com/PyHelper\"},\"commit\":{\"id\":\"ffa254791534a16a9a6e8b06ad634" \
                    "db0d8969ac6\",\"short_id\":\"ffa25479\",\"created_at\":\"2021-11-11T14:58:01.000+01:00\",\"" \
                    "parent_ids\":[\"9f29c8fe387e141f20dcbdafaf12f7c450e211e3\"],\"title\":\"update\",\"message\"" \
                    ":\"update\\n\",\"author_name\":\"Lucas\",\"author_email\":\"lucas-at-590749140953\",\"auth" \
                    "ored_date\":\"2021-11-11T14:58:01.000+01:00\",\"committer_name\":\"Lucas\",\"committer_ema" \
                    "il\":\"lucas-at-590749140953\",\"committed_date\":\"2021-11-11T14:58:01.000+01:00\",\"trail" \
                    "ers\":{},\"web_url\":\"https://gitlab.com/m5520/Mattermost-Coffeebot/-/commit/ffa254791534a" \
                    "16a9a6e8b06ad634db0d8969ac6\"},\"upcoming_release\":false,\"commit_path\":\"/m5520/Mattermo" \
                    "st-Coffeebot/-/commit/ffa254791534a16a9a6e8b06ad634db0d8969ac6\",\"tag_path\":\"/m5520/Matt" \
                    "ermost-Coffeebot/-/tags/v4.0\",\"assets\":{\"count\":4,\"sources\":[{\"format\":\"zip\",\"u" \
                    "rl\":\"https://gitlab.com/m5520/Mattermost-Coffeebot/-/archive/v4.0/Mattermost-Coffeebot-v4" \
                    ".0.zip\"},{\"format\":\"tar.gz\",\"url\":\"https://gitlab.com/m5520/Mattermost-Coffeebot/-/" \
                    "archive/v4.0/Mattermost-Coffeebot-v4.0.tar.gz\"},{\"format\":\"tar.bz2\",\"url\":\"https://" \
                    "gitlab.com/m5520/Mattermost-Coffeebot/-/archive/v4.0/Mattermost-Coffeebot-v4.0.tar.bz2\"}," \
                    "{\"format\":\"tar\",\"url\":\"https://gitlab.com/m5520/Mattermost-Coffeebot/-/archive/v4.0" \
                    "/Mattermost-Coffeebot-v4.0.tar\"}],\"links\":[]},\"evidences\":[],\"_links\":{\"self\":\"h" \
                    "ttps://gitlab.com/m5520/Mattermost-Coffeebot/-/releases/v4.0\",\"edit_url\":\"https://git" \
                    "lab.com/m5520/Mattermost-Coffeebot/-/releases/v4.0/edit\"}}"
    response.status_code = 201

    return response


def get_response_create_r_tagnotfound():
    response = mock.Mock(spec=Response)
    response.text = "{\"message\":\"Ref is not specified\"}"
    response.status_code = 422

    return response


def get_response_create_r_already_exists():
    response = mock.Mock(spec=Response)
    response.text = "{\"message\":\"Release already exists\"}"
    response.status_code = 409

    return response


def get_response_create_i():
    response = mock.Mock(spec=Response)
    response.text = "{\"id\":97814085,\"iid\":7,\"project_id\":31240995,\"title\":\"test_title\",\"descript" \
                    "ion\":\"test_description\",\"state\":\"opened\",\"created_at\":\"2021-11-23T14:19:5" \
                    "7.585Z\",\"updated_at\":\"2021-11-23T14:19:57.585Z\",\"closed_at\":null,\"closed" \
                    "_by\":null,\"labels\":[],\"milestone\":null,\"assignees\":[],\"author\":{\"id\":1" \
                    "0195829,\"name\":\"PyHelper\",\"username\":\"PyHelper\",\"state\":\"active\",\"avat" \
                    "ar_url\":\"https://secure.gravatar.com/avatar/fed8cb82c04c562f2580b10dbfc3a53b?s=80" \
                    "&d=identicon\",\"web_url\":\"https://gitlab.com/PyHelper\"},\"type\":\"ISSUE\",\"as" \
                    "signee\":null,\"user_notes_count\":0,\"merge_requests_count\":0,\"upvotes\":0,\"down" \
                    "votes\":0,\"due_date\":null,\"confidential\":false,\"discussion_locked\":null,\"issue" \
                    "_type\":\"issue\",\"web_url\":\"https://gitlab.com/m5520/Mattermost-Coffeebot/-/issue" \
                    "s/7\",\"time_stats\":{\"time_estimate\":0,\"total_time_spent\":0,\"human_time_estimat" \
                    "e\":null,\"human_total_time_spent\":null},\"task_completion_status\":{\"count\":0,\"c" \
                    "ompleted_count\":0},\"weight\":null,\"blocking_issues_count\":0,\"has_tasks\":false,\"" \
                    "_links\":{\"self\":\"https://gitlab.com/api/v4/projects/31240995/issues/7\",\"notes\"" \
                    ":\"https://gitlab.com/api/v4/projects/31240995/issues/7/notes\",\"award_emoji\":\"htt" \
                    "ps://gitlab.com/api/v4/projects/31240995/issues/7/award_emoji\",\"project\":\"https:/" \
                    "/gitlab.com/api/v4/projects/31240995\"},\"references\":{\"short\":\"#7\",\"relative\"" \
                    ":\"#7\",\"full\":\"m5520/Mattermost-Coffeebot#7\"},\"subscribed\":true,\"moved_to_id\"" \
                    ":null,\"service_desk_reply_to\":null,\"health_status\":null}"
    response.status_code = 201

    return response


def get_response_close_i():
    response = mock.Mock(spec=Response)
    response.text = "{\"id\":97814085,\"iid\":6,\"project_id\":31240995,\"title\":\"API_ERROR\",\"descrip" \
                    "tion\":\"test_description\",\"state\":\"opened\",\"created_at\":\"2021-11-23T14:19:5" \
                    "7.585Z\",\"updated_at\":\"2021-11-23T14:19:57.585Z\",\"closed_at\":null,\"closed_by\"" \
                    ":null,\"labels\":[],\"milestone\":null,\"assignees\":[],\"author\":{\"id\":10195829,\"" \
                    "name\":\"PyHelper\",\"username\":\"PyHelper\",\"state\":\"active\",\"avatar_url\":\"h" \
                    "ttps://secure.gravatar.com/avatar/fed8cb82c04c562f2580b10dbfc3a53b?s=80&d=identicon\"" \
                    ",\"web_url\":\"https://gitlab.com/PyHelper\"},\"type\":\"ISSUE\",\"assignee\":null,\"u" \
                    "ser_notes_count\":0,\"merge_requests_count\":0,\"upvotes\":0,\"downvotes\":0,\"due_dat" \
                    "e\":null,\"confidential\":false,\"discussion_locked\":null,\"issue_type\":\"issue\",\"we" \
                    "b_url\":\"https://gitlab.com/m5520/Mattermost-Coffeebot/-/issues/7\",\"time_stats\":{\"" \
                    "time_estimate\":0,\"total_time_spent\":0,\"human_time_estimate\":null,\"human_total_tim" \
                    "e_spent\":null},\"task_completion_status\":{\"count\":0,\"completed_count\":0},\"weight" \
                    "\":null,\"blocking_issues_count\":0,\"has_tasks\":false,\"_links\":{\"self\":\"https://" \
                    "gitlab.com/api/v4/projects/31240995/issues/7\",\"notes\":\"https://gitlab.com/api/v4/pr" \
                    "ojects/31240995/issues/7/notes\",\"award_emoji\":\"https://gitlab.com/api/v4/projects/3" \
                    "1240995/issues/7/award_emoji\",\"project\":\"https://gitlab.com/api/v4/projects/31240995" \
                    "\"},\"references\":{\"short\":\"#7\",\"relative\":\"#7\",\"full\":\"m5520/Mattermost-Cof" \
                    "feebot#7\"},\"subscribed\":true,\"moved_to_id\":null,\"service_desk_reply_to\":null,\"health" \
                    "_status\":null}"
    response.status_code = 200

    return response
