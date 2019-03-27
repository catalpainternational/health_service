## health_service

A simple hierarchical models collection to describe Health services facilities and sub-facilities, with optional GIS location support.
Depends on catalpainternational/simple_locations


#### Changelog

  * Version 1.3.4
    - fix HealthFacility children inlining (code was doing something... unrelated that was breaking saves)
  * Version 1.3.3
    - quality of life improvents in admin view, add HealthFacility children inline
  * Version 1.3.2
    - fix MANIFEST.in so that it'll include templates and other files
  * Version 1.3.1
    - fix admin interface by removing old code and using django_extensions' ForeignKeyAutocompleteAdmin if available
    - override aforementioned ForeignKeyAutocompleteAdmin template avoid broken and repeated icon in Django 1.11 
  * Version 1.3.0
    - Compatibility with Django 1.11
  * Version 1.2.1
    - Change the related_name for HealthFacility->Area so that it creates a backward relation in the ORM
    - Add LICENSE file

#### Uploading a new version to PyPi

  * Bump `setup.py` to a new version
  * Create a git tag for this version: `git tag <version_number>`
  * Push the tag to github `git push origin <version_number>`
  * Upload the new version to PyPi: `python setup.py sdist upload`
