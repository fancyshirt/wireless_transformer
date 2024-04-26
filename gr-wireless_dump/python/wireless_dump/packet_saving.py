#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2024 gr-wireless_dump author.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

import numpy as np
from gnuradio import gr
import pmt, json, sys, os

class packet_saving(gr.sync_block):
    """
    docstring for block packet_saving
    """
    def __init__(self, 
                mod, 
                tx_pwr, 
                save_folder, 
                save_prefix, 
                carrier_freq=2360e6, 
                samp_rate=5e6, 
                threshold=0.005, 
                debug=False, 
                record=False):
        gr.sync_block.__init__(self,
            name="packet_saving",
            in_sig=[np.complex64, np.complex64],
            out_sig=None)
        self.set_debug(debug)
        self.sef_mod(mod)
        self.sef_tx_pwr(tx_pwr)
        self.sef_save_folder(save_folder)
        self.sef_save_prefix(save_prefix)
        self.sef_carrier_freq(carrier_freq)
        self.sef_samp_rate(samp_rate)
        self.sef_threshold(threshold)

        self.set_record(record)

        self.update_save_filename()

    # ----------------------------------------------
    # Callback functions
    def set_record(self, record):
        try:
            if int(record) == 1:
                self.record = True
            else:
                self.record = False
            print(f"Setting {self.record: }")
        except Exception as exp:
            e_type, e_obj, e_tb = sys.exc_info()
            print(f'Exception: {exp}. At line {e_tb.tb_lineno}')

    def set_debug(self, debug):
        self.debug = debug
        print(f"Setting self.debug: {self.debug}")

    def sef_mod(self, mod):
        self.mod = mod
        self.update_save_filename()

    def sef_tx_pwr(self, tx_pwr):
        self.tx_pwr = tx_pwr
        self.update_save_filename()

    def sef_save_folder(self, save_folder):
        self.save_folder = save_folder
        if not os.path.exists(self.save_folder):
            print(f"Directory {self.save_folder} does not exist. Create one.")
            os.makedirs(self.save_folder)
        self.update_save_filename()

    def sef_save_prefix(self, save_prefix):
        self.save_prefix = save_prefix
        self.update_save_filename()

    def sef_carrier_freq(self, carrier_freq):
        self.carrier_freq = carrier_freq
        self.carrier_freq_in_MHz = int(self.carrier_freq/1e6)
        self.update_save_filename()

    def sef_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.samp_rate_in_MHz = int(self.samp_rate/1e6)
        self.update_save_filename()

    def sef_threshold(self, threshold):
        self.threshold = threshold

    def update_save_filename(self):
        self.save_filename = f"{self.save_prefix}_{self.mod}_{self.tx_pwr}_{self.samp_rate_in_MHz}_{self.carrier_freq_in_MHz}_"
        self.save_full_filename = f"{self.save_folder}{self.save_filename}"

        print(f"Update to save to {self.save_full_filename}")

    # ----------------------------------------------
    def work(self, input_items, output_items):
        try:

            in0 = input_items[0]
            in1 = input_items[1]

            moving_avg_ret = in1.real
            # thresold = in1.imag

            above_threshold = np.where(moving_avg_ret > self.threshold)
            

            self.consume(0, len(in0))
            self.consume(1, len(in1))

        except Exception as exp:
            e_type, e_obj, e_tb = sys.exc_info()
            print(f'Exception: {exp}. At line {e_tb.tb_lineno}')
        return False
