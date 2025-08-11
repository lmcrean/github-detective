# Issues for monzo/response

**Total Issues**: 56
**Repository**: https://github.com/monzo/response

**Open Issues**: 27
**Closed Issues**: 29

---

## Issues List (Most Recently Updated First)

- **#262: docker-compose build error at step 2/8**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2023-08-28
  > docker-compose up fails with netcat has no installation candidate error: ``` Step 2/8 : RUN apt-get update && apt-get install -y --no-install-recommends     netcat     && rm -rf /var/lib/apt/lists/*...

- **#226: Clarification for INCIDENT_CHANNEL_ID and INCIDENT_REPORT_CHANNEL_ID **
  - Labels: No labels
  - Comments: 3
  - Last updated: 2022-04-12
  > Based on the `README.md` on the `Update your settings.py` section. It says to define `INCIDENT_CHANNEL_ID`. But based on the [demo `settings.py`](https://github.com/monzo/response/blob/master/demo/dem...

- **#259: SPM portfolio management  services are not loading**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2022-03-14
  > Good morning team,  Pods services are not loading on Rancher for SPM portfolio management  , will you please investigate and revert back

- **#257: Build to Upgrade bleach to 3.3.0 is failing due to django-incident-response 0.5.1 depends on bleach 3.1.4**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2022-01-17
  > Describe the bug Build failed due to "django-incident-response 0.5.1 depends on bleach 3.1.4" The latest version of bleach is 4.1.0 Snyk detects a vulnerability issue on bleach - Cross-site Scripti...

- **#255: Racher Logs to Splunk **
  - Labels: No labels
  - Comments: 0
  - Last updated: 2021-12-09
  > Good dya Pieter and the team,  Will you please activate the process of pushing the logs to Splunk on SPM platform. we are planning to load logs into splunk in future

- **#254: Got ModuleNotFoundError: No module named 'after_response'**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2021-12-09
  > When I try to migrate by using this command  - python3 manage.py migrate. Then got this error - Got ModuleNotFoundError: No module named 'after_response'

- **#253: Rancher issues INC3519219 : Unable to logon to SPM , gravity throwing error 500**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2021-11-12
  > Good day team,  Please note that we are experiencing issues where microservices calls are not communicating with each other. will you please urgently get someone to assist. both our internal and ext...

- **#234: Rate limiting issues with users_list call**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2020-11-19
  > We're seeing issues starting up services due to rate limiting by slack on the users listing calls.  The current retry behaviour is fairly aggressive and retries 10 times with an initial delay of 0.2...

- **#125: Add back Statuspage and PagerDuty integrations**
  - Labels: feature-request
  - Comments: 4
  - Last updated: 2020-10-12
  > As in #116, we removed a few things from the `0.1.1` release (PagerDuty, Statuspage), as they didn't fit very well with the new code structure.  We also now think hardcoding them in is the wrong app...

- **#114: [Q] Is there an "official" docker image?**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2020-09-29
  > As title says, is there an official docker image you're using in your prod servers to spawn `response`? Looking forward to use it in our infra and I was wondering if I could get a curated version some...

- **#227: Edit incident via GUI**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2020-08-10
  > It is shown in the video that is posted in the README that you can login/edit the incident via the GUI.  But when I run the demo application there is no way to get to this state. Is the demo app not...

- **#218: Error calling Slack API endpoint 'channels.list': method_deprecated**
  - Labels: No labels
  - Comments: 9
  - Last updated: 2020-08-07
  > Have you seen this error? Mirrored the demo app, double checked the environment variables and Slack app configuration.  ``` response    | Traceback (most recent call last): response    |   File "m...

- **#224: Incident Reports not showing at incident channel**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2020-08-07
  > I'm exploring this package and followed every step in the document. I got the app running and setup it up for Slack. I tried to send a report using the `/incident` command, modal pop up and I input t...

- **#222: Deeplink to incident Slack channel from the incidents page**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2020-06-22
  > # Description  It'd be useful to have a deeplink (`slack://`) to the relevant conversation channel from the incidents page.  This would allow users to jump off from the incidents log without havin...

- **#214: 'channels.invite': user_not_found when creating new Comms Channel**
  - Labels: No labels
  - Comments: 2
  - Last updated: 2020-06-16
  > When I create new Comms Channel I am getting following error in logs: ``` ERROR:response.slack.action_handlers:Error calling Slack API endpoint 'channels.invite': user_not_found ```  Also, the on...

- **#183: [Suggestion] - Try to avoid fault releases?**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2020-03-04
  > @mattrco I'm aware that you're trying to do faster releases so the project doesn't stale, but for us, consumers it creates a lot of overhead to keep up. Specially if you're finding regressions and cut...

- **#184: Rendering Changes to Reporter or Incident Lead **
  - Labels: No labels
  - Comments: 0
  - Last updated: 2019-11-12
  > Has anyone encounters the attached issue when updating the Reporter or Incident Lead fields? The only way I can get them to display the usernames correctly is by doing a full page refresh(cmd + R)....

- **#168: Items in response/docs/slack_app_config.md are in the wrong order**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2019-10-14
  > You can't add the the event handler until the `response` app is up. But every time the container starts, ngrok creates a new random inbound port.   I couldn't figure out what order to do these thing...

- **#165: Possible to add a notification with a name that's too long**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2019-10-09
  > It's currently possible to create a notification handler with a function name too long to fit in the `key` column in the notifications database table.  Recommendations of fixes, either:  - Convert...

- **#164: Possible to set a channel name that's too long**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2019-10-09
  > I believe it's currently possible to set a channel name with `rename` that is too long to fit in the database table.  Recommendations of fixes:  1. Convert to `TextField`, on Postgres at least the...

- **#76: Error "Is the server running locally and accepting connection"**
  - Labels: No labels
  - Comments: 6
  - Last updated: 2019-09-26
  > Hi, I am just trying to setup response app on Local Laptop. Getting these error logs.   ``` [INFO] Waiting for DB response    | [INFO] Migrating database postgres    | 2019-07-22 11:29:09.675 UT...

- **#149: Improvements in slack integration**
  - Labels: No labels
  - Comments: 4
  - Last updated: 2019-09-25
  > Hey there, we've started to use response very recently as a PoC to handle our incident response process internally. We were looking for a solution that integrates well with slack as our company is mos...

- **#132: MySQL and timelines**
  - Labels: No labels
  - Comments: 2
  - Last updated: 2019-09-21
  > Hi,   Is it possible to do some if/else magic around the JSONField timeline option that has just been added. As it currently stands I have to patch in django_mysql to get it to talk to MySQL.  I'v...

- **#144: What is the 'action' command supposed to do?**
  - Labels: No labels
  - Comments: 2
  - Last updated: 2019-09-17
  > A more detailed description of the `@incident` commands would be really useful 🙏 I haven't been able to figure out what `@incident action [action_command]` is supposed to achieve 🤔  ![image](https://...

- **#89: Action Items displayed in the UI**
  - Labels: enhancement
  - Comments: 2
  - Last updated: 2019-09-10
  > Is it possible to get the UI updated so that it can display action items as shown in the demo video?

- **#118: Building features on top of demo application**
  - Labels: No labels
  - Comments: 5
  - Last updated: 2019-09-09
  > Hello,  I am trying to leverage the packaged version, and adding additional functionality per this documentation: https://github.com/monzo/response/blob/master/docs/development.md  In manage.py I'...

- **#139: Handlers for Incident lifecycle events**
  - Labels: No labels
  - Comments: 2
  - Last updated: 2019-09-09
  > In addition to the slack event handlers provided by response, it would be great to take actions on the opening, closing or comms channel creation for an incident.  These are the sorts of things we'd...

- **#127: Security: No login required**
  - Labels: No labels
  - Comments: 5
  - Last updated: 2019-09-08
  > Currently response does not enforce login in the UI views or the API resources. This goes somewhat against the Django convention of being secure and safe by default.  It's possible that Monzo are de...

- **#133: Code formatting/linting**
  - Labels: No labels
  - Comments: 3
  - Last updated: 2019-09-06
  > I've been playing around with the codebase and implemented a few changes. As a newcomer to the codebase it's a little tricky to understand what the expectation of code formatting/style is.  What do...

- **#119: AttributeError: 'Settings' object has no attribute 'SLACK_CLIENT'**
  - Labels: No labels
  - Comments: 3
  - Last updated: 2019-09-05
  > I installed the response app using pip. After attempting to use the slash command to create an incident, I received the following error. Could anyone provide some guidance on how to address it?:  At...

- **#116: Several things were removed in 0.1.1 without notice**
  - Labels: No labels
  - Comments: 3
  - Last updated: 2019-09-04
  > Just downloaded and install the latest version of `response` and noticed that several things like workflows, pagerduty and statuspage are missing. After re-checking the latest release-notes (https://g...

- **#86: Error Occured**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2019-09-04
  > Is the server running locally and accepting 	connections on Unix domain socket "/var/run/postgresql/.s.PGSQL.5432"?

- **#122: Odoo 11 Error**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2019-09-04
  > Hello   Thanks for previous helps,  Today i  am running odoo version 10 on ubuntu 19.04. this odoo version on eclipse with python version 2.7 but following error will occur.  File "/media/super/0c...

- **#123: Regarding Access**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2019-09-04
  > Hello Sir,  i remove rights of Inventory>>Transfer Save/Edit to Inventory Operator user who is only view Transfer. On main Screen Create/Edit button is not showing but if i click on any Transfer und...

- **#33: Feature Request: Package as Django "app" for reusability**
  - Labels: No labels
  - Comments: 10
  - Last updated: 2019-08-15
  > One of the nice features of this project is the ability to create custom interactions to power team processes.  ### Problem  Unfortunately to do this, users must essentially fork the codebase, add...

- **#26: KeyError: 'ts'**
  - Labels: bug
  - Comments: 9
  - Last updated: 2019-08-15
  > Hi,  I am trying to create an incident and I am receiving:  ``` response    | [26/May/2019 19:52:02] "POST /slack/action HTTP/1.1" 200 0 response    |  ERROR - signals    - 'ts' response    | T...

- **#21: Documentation neglects certain configurable items**
  - Labels: No labels
  - Comments: 4
  - Last updated: 2019-08-15
  > Firstly, it looks great, and it's awesome you're open sourcing this. 👍   Few 'secure by default' requests though. The docs don't mention that the django url sits off the response url under admin an...

- **#79: Bot User Not Invited to Incident Comms Channel**
  - Labels: No labels
  - Comments: 2
  - Last updated: 2019-08-14
  > Exact same issue as "too many channels" is "too many users."  https://github.com/philovivero/response/commit/5260f401f60b002efc84b43f68eb3d20601a4ed0#diff-1a2d815092cbb92582aa1e1107a106b8R179  In...

- **#98: TypeError: 'NoneType' object is not subscriptable**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2019-08-14
  > [Untitled 1.docx](https://github.com/monzo/response/files/3499825/Untitled.1.docx)  **ATTACH WHOLE ERROR AND MY SCRIPT DOCUMENT WITH THIS**  Hello, I am trying to display form fields in report bu...

- **#94: Feature contribution**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2019-08-14
  > I'd like to submit a pull request but don't have permission to push my branch. Are you open to contributions? We're using response at my work and have a few additional features in mind

- **#87: Backup of odoo database**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2019-08-14
  > i want to take backup of odoo database using shell command and crontab please guide step by step i am new here

- **#58: Add example of adding handlers/commands to demo app**
  - Labels: enhancement
  - Comments: 1
  - Last updated: 2019-08-14
  > Could an example of how to add additional handlers/commands be added to the demo app so consumers of the new architecture (as a package) know how they can add their own items that aren't core to the R...

- **#51: Static files not being served when in PROD mode**
  - Labels: No labels
  - Comments: 5
  - Last updated: 2019-08-14
  > Since the change to disable debug in PROD in #40 (rightly so!), static files are no longer being served up and producing "not found" messages for requests to the those assets including CSS, etc, when...

- **#20: Helm chart for Kubernetes**
  - Labels: enhancement
  - Comments: 3
  - Last updated: 2019-08-14
  > Hello,   First of all thanks for open sourcing this great tool, I really liked the concept behind this. I just wanted to open this issue with regards to having a `helm` chart that we can install in...

- **#29: Feature Request: Notify incident channel when closed/resolved from the headline post**
  - Labels: enhancement
  - Comments: 1
  - Last updated: 2019-08-14
  > Feature request for sending a notification to the incident channel when the incident has been closed/resolved. This would just help to know in the chat when the incident has been closed/resolved.

- **#28: Feature Request: Ability to close incident from channel**
  - Labels: No labels
  - Comments: 3
  - Last updated: 2019-08-14
  > Requesting feature to be able to close an incident from within the channel. I.e `@incident close`.  This would help as then the incident lead or engineers wouldn't have to switch back to the inciden...

- **#11: Question: Action Items**
  - Labels: No labels
  - Comments: 3
  - Last updated: 2019-08-14
  > In the demo video, I saw action items was an option but I don't think it's in the public code base. Is this something that will be made available at a later date @evnsio?

- **#97: TypeError: 'NoneType' object is not subscriptable**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2019-08-14
  > Hello, I am trying to display form fields in report but following error occur. Error:​ odoo.addons.base.ir.ir_qweb.qweb.QWebException: 'NoneType' object is not subscriptable Traceback (most recent...

- **#52: Close vs Resolve UI text**
  - Labels: No labels
  - Comments: 2
  - Last updated: 2019-07-08
  > From the headline post, "resolve" is used for the button text but from within the incident the command is `@incident close`. Do we need to standardise on the language used or are these two events and...

- **#50: Duplicate messages**
  - Labels: No labels
  - Comments: 5
  - Last updated: 2019-07-08
  > Hi,  I'm seeing a strange issue whereby messages are being processed by Response multiple times.  For example, when closing an incident, it successfully closes the incident, they very quickly afte...

- **#45: Make Demo Work**
  - Labels: No labels
  - Comments: 4
  - Last updated: 2019-07-08
  > I set up the Demo. Trying to create an incident, I get these errors:  ``` response    |  ERROR - signals    - 'Critical' response    | Traceback (most recent call last): response    |   File "/ap...

- **#46: ERROR with external users**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2019-07-04
  > Hello @evnsio I found strange bug after you added external user IDs.  ```python def get_user_profile(user_id):     if not user_id:         return None      response = slack_client.api_call(...

- **#19: Feature. DB parameters with env vars**
  - Labels: No labels
  - Comments: 2
  - Last updated: 2019-07-01
  > First of all want to say thank you for such wonderful tool. Its really awesome tool to manage incidents.   Small feature request.  Want to setup you tool to AWS and want to use RDS. Can you please...

- **#10: Ngrok session time out**
  - Labels: No labels
  - Comments: 2
  - Last updated: 2019-05-10
  > Need to sign up to ngrok and get a authentication token in order to extend the ngrok sessions past 7 hours.  Anyway to add the authentication token into this?  Thanks.

- **#9: Usage without ngrok**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2019-05-08
  > Is this just a case of removing these lines and setting up a reverse proxy on the machine to point at port 8000 on the `response` container?  https://github.com/monzo/response/blob/97e35de75cd78eb3b...

- **#6: Error on incident creation**
  - Labels: No labels
  - Comments: 4
  - Last updated: 2019-05-04
  > Any thoughts on the below?  ``` response    | [04/May/2019 07:55:08] "POST /slack/slash_command HTTP/1.1" 500 161449 response    | Internal Server Error: /slack/slash_command response    | Traceb...

