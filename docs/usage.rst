=====
Usage
=====

To use Quartet Trail in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'quartet_trail.apps.QuartetTrailConfig',
        ...
    )

Add Quartet Trail's URL patterns:

.. code-block:: python

    from quartet_trail import urls as quartet_trail_urls


    urlpatterns = [
        ...
        url(r'^', include(quartet_trail_urls)),
        ...
    ]
