# Importing users to Smartsheets

Smartsheets allows users to be created by importing CSVs.

According to the [Smartsheets documentation](https://help.smartsheet.com/articles/2480826-import-multiple-people) you can import a CSV with the following schema:

| Fields     | Required field           | Description                                                                                                                         | Formatting requirements                                                                                                                                                      |
|------------|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| user_id    | Yes* (for editing users) | The User ID stores all of the user attributes assigned to them. Exporting the people list will include User IDs for existing users. | Must be a valid User ID in the organization <br>To create new users, leave the User ID column blank. <br>To update attributes for existing users, leave their User ID intact |
| first_name |                          | Add the first name of a user.                                                                                                       | 0-255 characters                                                                                                                                                             |
| last_name  | Optional                 | Add the last name of a user.                                                                                                        | 0-255 characters                                                                                                                                                             |
| email |  | Add the email address for the user. Note that a user's profile email differs from their login email. <br>See Configure profile settings. <br>user@domain.com |
| permission_type |  | Set the permission level for the user. Note that users can change their permission type using Add/Update People. | <ul><li>Resourcing Administrator</li><li>Portfolio Editor</li><li>People Scheduler</li><li></li><li>Portfolio Reporter</li><li>Portfolio Viewer</li><li>Project Editor</li><li>Contractor</li></ul> |
| license_type |  | Set the license type for the user. Note that users can change their license type using Add/Update People. | <ul><li>licensed</li><li>managed_resource</li></ul> |
| discipline | Optional | Add the team/group for the user. A new discipline will be created if it doesn't already exist. | 0-255 characters |
| role | Optional | Add the type of work for the user. A new role will be created if it doesn't already exist. | 0-255 characters |
| location | Optional | Add the location where the user is based. A new location will be created if it doesn't already exist. | 0-255 characters |
| first_day_of_work | Optional | Add the user's first day of work. This value affects the user's starting availability. | Date format: YYYY-MM-DD |
| last_day_of_work | Optional | Add the user's last day of work. This value affects a user's ending availability. | Date format: YYYY-MM-DD |
| mobile_phone | Optional | Add the user's mobile phone number. This value is visible on a user's profile page. | 0-255 characters |
| office_phone | Optional | Add the user's office phone number. This value is visible on a user's profile page. | 0-255 characters |
| employee_number | Optional | Add an internal employee identification number. This value appears in report exports. | 0-255 characters |
| utilization_target | Optional | Add a fixed number for the user's utilization target. The target is visible in utilization reports and does not impact a user's availability. | It must be a number <br>If this value is blank, 100 will be applied |
| bill_rate | Optional | Add a modified bill rate for the user or use the default bill rate based on their discipline and role. | The modified bill rate must be a number <br>[default] applies the default bill rate based on discipline and role <br>If this field is blank, [default] will be applied |
| people_tags | Optional | Add tags to identify skills or other unique characteristics. | 0-255 characters <br>Separate multiple entries with a semicolon |
| approvers | Optional | Add or remove specific approvers for the user. <br>If project owners are enabled as approvers, they don't need to be included in this list. <br>Must be a valid User ID in the organization <br>Separate multiple entries with a semicolon |
| CF_## “name” (text field) | Optional | Add a string of text to the custom field. | 0-255 characters |
| CF_## “name” (dropdown) | Optional | Set an existing custom field value for the user. | Ensure that any values entered in this column are saved as options for this field in the Account Settings > People Custom Fields page |
| CF_## “name” (multi-select dropdown) | Optional | Set existing custom field values for the user. |  Ensure that any values entered in this column are saved as options for this field in the Account Settings > People Custom Fields page <br>Separate multiple entries with a semicolon |