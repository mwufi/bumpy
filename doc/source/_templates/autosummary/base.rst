{% if objtype == 'property' %}
:orphan:
{% endif %}

{{ fullname | escape | underline}}

.. currentmodule:: {{ module }}

{% if objtype == 'property' %}
property
{% endif %}

.. auto{{ objtype }}:: {{ fullname | replace("bumpy.", "bumpy::") }}

{# In the fullname (e.g. `bumpy.ma.MaskedArray.methodname`), the module name
is ambiguous. Using a `::` separator (e.g. `bumpy::ma.MaskedArray.methodname`)
specifies `bumpy` as the module name. #}
