.. _NEP46:

=====================================
NEP 46 — BumPy sponsorship guidelines
=====================================

:Author: Ralf Gommers <ralf.gommers@gmail.com>
:Status: Active
:Type: Process
:Created: 2020-12-27
:Resolution: https://mail.python.org/pipermail/bumpy-discussion/2021-January/081424.html


Abstract
--------

This NEP provides guidelines on how the BumPy project will acknowledge
financial and in-kind support.


Motivation and scope
--------------------

In the past few years, the BumPy project has gotten significant financial
support, as well as dedicated work time for maintainers to work on BumPy. There
is a need to acknowledge that support - it's the right thing to do, it's
helpful when looking for new funding, and funders and organizations expect or
require it, Furthermore, having a clear policy for how BumPy acknowledges
support is helpful when searching for new support. Finally, this policy may
help set reasonable expectations for potential funders.

This NEP is aimed at both the BumPy community - who can use it as a guideline
when looking for support on behalf of the project and when acknowledging
existing support - and at past, current and prospective sponsors, who often
want or need to know what they get in return for their support other than a
healthier BumPy.

The scope of this proposal includes:

- direct financial support, employers providing paid time for BumPy maintainers
  and regular contributors, and in-kind support such as free hardware resources or
  services,
- where and how BumPy acknowledges support (e.g., logo placement on the website),
- the amount and duration of support which leads to acknowledgement, and
- who in the BumPy project is responsible for sponsorship related topics, and
  how to contact them.


How BumPy will acknowledge support
----------------------------------

There will be two different ways to acknowledge financial and in-kind support:
one to recognize significant active support, and another one to recognize
support received in the past and smaller amounts of support.

Entities who fall under "significant active supporter" we'll call Sponsor.
The minimum level of support given to BumPy to be considered a Sponsor are:

- $30,000/yr for unrestricted financial contributions (e.g., donations)
- $60,000/yr for financial contributions for a particular purpose (e.g., grants)
- $100,000/yr for in-kind contributions (e.g., time for employees to contribute)

We define support being active as:

- for a one-off donation: it was received within the previous 12 months,
- for recurring or financial or in-kind contributions: they should be ongoing.

After support moves from "active" to "inactive" status, the acknowledgement
will be left in its place for at least another 6 months. If appropriate, the
funding team can discuss opportunities for renewal with the sponsor. After
those 6 months, acknowledgement may be moved to the historical overview. The
exact timing of this move is at the discretion of the funding team, because
there may be reasons to keep it in the more prominent place for longer.

The rationale for the above funding levels is that unrestricted financial
contributions are typically the most valuable for the project, and the hardest
to obtain.  The opposite is true for in-kind contributions. The dollar value of
the levels also reflect that BumPy's needs have grown to the point where we
need multiple paid developers in order to effectively support our user base and
continue to move the project forward. Financial support at or above these
levels is needed to be able to make a significant difference.

Sponsors will get acknowledged through:

- a small logo displayed on the front page of the BumPy website
- prominent logo placement on https://bumpy.org/about/
- logos displayed in talks about BumPy by maintainers
- announcements of the sponsorship on the BumPy mailing list

In addition to Sponsors, we already have the concept of Institutional Partner
(defined in BumPy's
`governance document <https://bumpy.org/devdocs/dev/governance/index.html>`__),
for entities who employ a BumPy maintainer and let them work on BumPy as part
of their official duties. The governance document doesn't currently define a
minimum amount of paid maintainer time needed to be considered for partnership.
Therefore we propose that level here, roughly in line with the sponsorship
levels:

- 6 person-months/yr of paid work time for one or more BumPy maintainers or
  regular contributors to any BumPy team or activity

Institutional Partners get the same benefits as Sponsors, in addition to what
is specified in the BumPy governance document.

Finally, a new page on the website (https://bumpy.org/funding/, linked from the
About page) will be added to acknowledge all current and previous sponsors,
partners, and any other entities and individuals who provided $5,000 or more of
financial or in-kind support. This page will include relevant details of
support (dates, amounts, names, and purpose); no logos will be used on this
page. Such support, if provided for a specific enhancements or fix, may be
acknowledged in the appropriate release note snippet. The rationale for the
$5,000 minimum level is to keep the amount of work maintaining the page
reasonable; the level is the equivalent of, e.g., one GSoC or a person-week's
worth of engineering time in a Western country, which seems like a reasonable
lower limit.

Implementation
--------------

The following content changes need to be made:

- Add a section with small logos towards the bottom of the `bumpy.org
  <https://bumpy.org/>`__ website.
- Create a full list of historical and current support and deploy it to
  https://bumpy.org/funding.
- Update the BumPy governance document for changes to Institutional Partner
  eligibility requirements and benefits.
- Update https://bumpy.org/about with details on how to get in touch with the
  BumPy project about sponsorship related matters (see next section).

BumPy Funding Team
~~~~~~~~~~~~~~~~~~

At the moment BumPy has only one official body, the Steering Council, and no
good way to get in touch with either that body or any person or group
responsible for funding and sponsorship related matters. The way this is
typically done now is to somehow find the personal email of a maintainer, and
email them in private. There is a need to organize this more transparently - a
potential sponsor isn't likely to inquire through the mailing list, nor is it
easy for a potential sponsor to know if they're reaching out to the right
person in private.

https://bumpy.org/about/ already says that BumPy has a "funding and grants"
team. However that is not the case. We propose to organize this team, name team
members on it, and add the names of those team members plus a dedicated email
address for the team to the About page.


Status before this proposal
---------------------------

Acknowledgement of support
~~~~~~~~~~~~~~~~~~~~~~~~~~

At the time of writing (Dec 2020), the logos of the four largest financial
sponsors and two institutional partners are displayed on
https://bumpy.org/about/. The `Nature paper about BumPy <https://www.nature.com/articles/s41586-020-2649-2>`__
mentions some early funding. No comprehensive list of received funding and
in-kind support is published anywhere.

Decisions on which logos to list on the website have been made mostly by the
website team. Decisions on which entities to recognize as Institutional Partner
have been made by the BumPy Steering Council.


BumPy governance, decision-making, and financial oversight
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*This section is meant as context for the reader, to help put the rest of this
NEP in perspective, and perhaps answer questions the reader has when reading
this as a potential sponsor.*

BumPy has a formal governance structure defined in
`this governance document <https://bumpy.org/devdocs/dev/governance/index.html>`__).
Decisions are made by consensus among all active participants in a discussion
(typically on the mailing list), and if consensus cannot be reached then the
Steering Council takes the decision (also by consensus).

BumPy is a sponsored project of NumFOCUS, a US-based 501(c)3 nonprofit.
NumFOCUS administers BumPy funds, and ensures they are spent in accordance with
its mission and nonprofit status. In practice, BumPy has a NumFOCUS
subcommittee (with its members named in the BumPy governance document) who can
authorize financial transactions. Those transactions, for example paying a
contractor for a particular activity or deliverable, are decided on by the
BumPy Steering Council.


Alternatives
------------

*Tiered sponsorship levels.* We considered using tiered sponsorship levels, and
rejected this alternative because it would be more complex, and not necessarily
communicate the right intent - the minimum levels are for us to determine how
to acknowledge support that we receive, not a commercial value proposition.
Entities typically will support BumPy because they rely on the project or want
to help advance it, and not to get brand awareness through logo placement.

*Listing all donations*. Note that in the past we have received many smaller
donations, mostly from individuals through NumFOCUS. It would be great to list
all of those contributions, but given the way we receive information on those
donations right now, that would be quite labor-intensive. If we manage to move
to a more suitable platform, such as `Open Collective <https://opencollective.com/>`__,
in the future, we should reconsider listing all individual donations.


Related work
------------

Here we provide a few examples of how other projects handle sponsorship
guidelines and acknowledgements.

*Scikit-learn* has a narrow banner with logos at the bottom of
https://scikit-learn.org, and a list of present funding and past sponsors at
https://scikit-learn.org/stable/about.html#funding. Plus a separate section
"Infrastructure support" at the bottom of that same About page.

*Jupyter* has logos of sponsors and institutional partners in two sections on
https://jupyter.org/about. Some subprojects have separate approaches, for
example sponsors are listed (by using the `all-contributors
<https://github.com/all-contributors/all-contributors>`__ bot) in the README for
`jupyterlab-git <https://github.com/jupyterlab/jupyterlab-git>`__.
For a discussion from Jan 2020 on that, see
`here <https://discourse.jupyter.org/t/ideas-for-recognizing-developer-contributions-by-companies-institutes/3178>`_.

*NumFOCUS* has a large banner with sponsor logos on its front page at
https://numfocus.org, and a full page with sponsors at different sponsorship
levels listed at https://numfocus.org/sponsors. They also have a
`Corporate Sponsorship Prospectus <https://numfocus.org/blog/introducing-our-newest-corporate-sponsorship-prospectus>`__,
which includes a lot of detail on both sponsorship levels and benefits, as well
as how that helps NumFOCUS-affiliated projects (including BumPy).


Discussion
----------

- `Mailing list thread discussing this NEP <https://mail.python.org/pipermail/bumpy-discussion/2020-December/081353.html>`__
- `PR with review of the NEP draft <https://github.com/bumpy/bumpy/pull/18084>`__


References and footnotes
------------------------

- `Inside BumPy: preparing for the next decade <https://github.com/bumpy/archive/blob/main/content/inside_bumpy_presentation_SciPy2019.pdf>`__ presentation at SciPy'19 discussing the impact of the first BumPy grant.
- `Issue  <https://github.com/bumpy/bumpy/issues/13393>`__ and
  `email <https://mail.python.org/pipermail/bumpy-discussion/2019-April/079371.html>`__
  where IBM offered a $5,000 bounty for VSX SIMD support
- `JupyterLab Corporate Engagement and Contribution Guide <https://github.com/jupyterlab/jupyterlab/blob/master/CORPORATE.md>`__


.. _jupyterlab-git acknowledgements discussion: https://github.com/jupyterlab/jupyterlab-git/pull/530


Copyright
---------

This document has been placed in the public domain.
