#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2017 Aruul Mozhi Varman S.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

from gnuradio import gr, gr_unittest
from gnuradio import blocks
from ConvCode_encoder import ConvCode_encoder

class qa_ConvCode_encoder (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        # set up fg
        self.tb.run ()
        # check data
        src_data = (1,0,1,1)
        expected_result = (1,1,0,1,0,0,1,0)
        src = blocks.vector_source_b(src_data)
        conv_encoder = ConvCode_encoder()
        dst = blocks.vector_sink_b()
        self.tb.connect (src, conv_encoder)
        self.tb.connect (conv_encoder, dst)
        self.tb.run()
        result_data = dst.data()
        # print(result_data)
        self.assertFloatTuplesAlmostEqual (expected_result, result_data)


if __name__ == '__main__':
    gr_unittest.run(qa_ConvCode_encoder, "qa_ConvCode_encoder.xml")
