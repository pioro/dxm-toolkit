## Version 0.5

### Added:
 - user support added

### Changed:
 - fix for port and protocol setting
 - [fix for #11](https://github.com/delphix/dxm-toolkit/issues/11) - Output in JSON for metadata fetch
 - [fix for #15](https://github.com/delphix/dxm-toolkit/issues/15) - Multitenant for profile job
 - [fix for #16](https://github.com/delphix/dxm-toolkit/issues/16) - fix for MS SQL and Sybase connectors



## Version 0.42

### Added:
 - log export

### Changed:
 - various bug fixes

## Version 0.4

### Added:
 - support for sync API to export / import object between engines
 - support for Delphix Engine 5.3
 - column list is displaying a data type plus column type (index, FK, PK)

### Changed:
 - various bug fixes
 - UTF-8 related bug fixes
 - column save / batch format file is changed to similar to GUI inventory export


## Version 0.3

### Added:
 - support for profile (sets, expressions, jobs)
 - support for export/import/check ruleset with all depended objects into JSON files  

### Changed:
 - various bug fixes
 
## Version 0.22

### Changed:
 - fix for adding file into files rulesets
 - other small bug fixs

## Version 0.21

### Changed:
 - bug fixed for status in job list
 - bug fixed for same connector id for file and database connectors

## Version 0.2

### Added:
 - jobs queue added - multiple jobs can be run in parallel or serial

### Changed:
 - bug fixed for on the fly job
 - bug fixed for listing jobs

## Version 0.1

Initial release of DXM toolkit.
It's supporting the following operations:

- adding an application
- listing/adding/deleting an environment
- listing/adding/deleting a container
- listing/adding/deleting/cloning a ruleset
- listing/adding/deleting a metadata for ruleset (tables or files)
- listing/adding/deleting/setting as masked/unmasked a column for metadata (table or file)
- batch algorithm replace for columns
- load/save rulesets from/to CSV files
- load/save columns from/to CSV files
- list/adding/deleting/starting/cancelling/updating/copy a masking job
- listing/updating a table or file details ( like adding a key, where clause)
- listing/adding/deleting a file format
