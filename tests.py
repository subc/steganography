# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from steganography.steganography import Steganography


def test_stegano():
    path = "/tmp/image/a.jpg"
    output_path = "/tmp/image/b.jpg"
    text = 'aiueo aaaa aaaa'

    Steganography.encode(path, output_path, text)
    secrete_text = Steganography.decode(output_path)
    assert secrete_text == text


def test_stegano_overflow():
    path = "/tmp/image/a.jpg"
    output_path = "/tmp/image/c.jpg"
    text = 'aiueo aaaa aaaa' * 100

    Steganography.encode(path, output_path, text)
    secrete_text = Steganography.decode(output_path)
    assert secrete_text == text
