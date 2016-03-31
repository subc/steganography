Digital image steganography of encrypted text
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
    from steganography.steganography import Steganography

    # hide text to image
    path = "/tmp/image/a.jpg"
    output_path = "/tmp/image/b.jpg"
    text = 'The quick brown fox jumps over the lazy dog.'
    Steganography.encode(path, output_path, text)

    # read secret text from image
    secret_text = Steganography.decode(output_path)

Documentation
-----------------

- 日本語ドキュメント: `Japanese Document`_

.. _`Japanese Document`: http://qiita.com/haminiku/items/bcf4bac82bd1ca62c746
