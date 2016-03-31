Implementation Hide Text In Image with encryption
========================================================================


日本語ドキュメント: `Japanese Document`_


Installation
-----------------

.. code-block:: bash

    $ pip install steganography

Sample Code
-----------------

.. code-block:: python

    # -*- coding: utf-8 -*-
    from __future__ import absolute_import, unicode_literals
    from mynumber import MyNumber

    # Validate
    my_number = 123456789018
    print MyNumber.validate(my_number)

    # Validate MyNumber. Duplicate Disable
    for my_number in MyNumber.gets(1000):
        assert MyNumber.validate(my_number)

    # Validate MyNumber by iterator. Duplicate Enable
    for my_number in MyNumber():
        assert MyNumber.validate(my_number)


Documentation
-----------------

- `My Number Law`_
- 日本語ドキュメント: `Japanese Document`_

.. _`Japanese Document`: http://qiita.com/haminiku/items/bcf4bac82bd1ca62c746
.. _`My Number Law`: http://www.soumu.go.jp/main_content/000327387.pdf
