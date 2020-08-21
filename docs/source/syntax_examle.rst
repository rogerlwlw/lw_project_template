..  comment
    # with overline, for parts

    * with overline, for chapters
    
    =, for sections
    
    -, for subsections
    
    ^, for subsubsections
    
    ", for paragraphs

reST syntax example
====================


cross reference
----------------
this is a **link** to internal file :doc:`main page <index>`

this is a cross reference link to section :ref:`reflabel`

refer to masterdoc :ref:`masterdoc`

this is a link to function :func:`get_local_data <project_lib.dataset.load_data.get_local_data>`

this is a link to module :mod:`load_data`

this is a link to python documentation :class:`zipfile.ZipFile`

this is a link to sklearn :class:`sklearn.linear_model.Lasso`

this is a hyper link to sphinx doc `sphinxdoc`_

this is a hyper link to `sphinxdoc hyperlink <https://www.sphinx-doc.org/>`_


.. _sphinxdoc: https://www.sphinx-doc.org/


Footenote
---------

this is 1st [1]_  [2]_

this is f1 [#f1]_

this is f2 [#f2]_

this is a [citation1]_



Substitution
-------------
this package: |pkg| is  edited by |author|

.. _reflabel:

Literal blocks
--------------

This is a normal text paragraph. The next paragraph is a code sample::

   It is not processed in any way, except
   that the indentation is removed.

   It can span multiple lines.

This is a normal text paragraph again.
    

..
   This whole indented block
   is a comment.

   Still in the comment.

admonitions provided By Docutils.
----------------------------------------------------
.. note::
    pay attention to this 
    
.. warning::
    pay attention to this 
    
.. danger::
    pay attention to this 
    
.. tip::
    pay attention to this 
    
.. important::
    pay attention to this 



.. rubric:: Footnotes

.. [#] Text of the first 
.. [#] Text of the second footnote
.. [#f1] Text of the first footnote.
.. [#f2] Text of the second footnote.

.. rubric:: Citations

.. [citation1] 
    * Book1 
    
    * Book2
    
    * Article1