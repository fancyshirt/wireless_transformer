clc
clear
close all
%%
% Discrete sample:
%   BPSK; QPSK; 8PSK; 16QAM; 64QAM; 4PAM; CPFSK
% Continue sample:
%   WBFM; AM-SSB; SM-DSB

addpath(genpath('./wireless_signal/'))

ttl_waveform = get_all_signals();
ttl_waveform_name = fieldnames(ttl_waveform);
for n_mod = 1:numel(ttl_waveform_name)
    waveform = ttl_waveform.(ttl_waveform_name{n_mod});
    
    size(waveform)
end


%% 
function ttl_wform = get_all_signals()
    % BPSK; QPSK; 16QAM; 64QAM

    psdu_length = 10;
    wifi_0_wform = generate_wifi(mod=0, symbol_len=psdu_length);
    wifi_1_wform = generate_wifi(mod=1, symbol_len=psdu_length);
    wifi_2_wform = generate_wifi(mod=2, symbol_len=psdu_length);
    wifi_3_wform = generate_wifi(mod=3, symbol_len=psdu_length);
    wifi_4_wform = generate_wifi(mod=4, symbol_len=psdu_length);
    wifi_5_wform = generate_wifi(mod=5, symbol_len=psdu_length);
    wifi_6_wform = generate_wifi(mod=6, symbol_len=psdu_length);
    wifi_7_wform = generate_wifi(mod=7, symbol_len=psdu_length);

    % 4PAM
    pam_mod = 4;
    pam_num_symbol = 100;
    pam_wform = generate_pam(mod=pam_mod, num_symbol=pam_num_symbol);

    % CPFSK
    cpfsk_mod = 8;
    cpfsk_spf = 115;
    cpfsk_wform = generate_cpfsk(spf=cpfsk_spf, mod=cpfsk_mod);

    % FSK
    fsk_samp_rate = 32;
    fm_sps = 8;
    fm_mod = 4;
    fm_freqsep = 8;
    fm_data_length = 10;
    fsk_wform = generate_fsk(fs=fsk_samp_rate, sps=fm_sps, mod=fm_mod, freqsep=fm_freqsep, data_length=fm_data_length);


    % AM-SSB; AM-DSB
    am_fc = 550e3;
    am_fs = 44.1e3;

    am_t = (0:1/am_fs:.01);
    continue_signal = sin(2*pi*30*am_t) + 2*sin(2*pi*60*am_t);
    [am_l_wform, am_u_wform, am_d_wform] = generate_am(continue_signal, fc=am_fc, fs=am_fs);

    % WBFM
    fm_fs = 1e3;           % Sample Frequency
    fm_fc = 200;           % Carrier Frequency 88.1 MHz - 108.1 MHz
    fm_fDev = 50;          % Frequency Deviation (Hz)/Modulation index
    fm_t = (0:1/fm_fs:.1);
    continue_signal = sin(2*pi*30*fm_t) + 2*sin(2*pi*60*fm_t);
    wbfm_wform = generate_wbfm(continue_signal, fc=fm_fc, fs=fm_fs, fDev=fm_fDev);

    % Collect all the waveforms.
    ttl_wform = {};
    ttl_wform.wifi_0 = wifi_0_wform;
    ttl_wform.wifi_1 = wifi_1_wform;
    ttl_wform.wifi_2 = wifi_2_wform;
    ttl_wform.wifi_3 = wifi_3_wform;
    ttl_wform.wifi_4 = wifi_4_wform;
    ttl_wform.wifi_5 = wifi_5_wform;
    ttl_wform.wifi_6 = wifi_6_wform;
    ttl_wform.wifi_7 = wifi_7_wform;
    ttl_wform.pam = pam_wform;
    ttl_wform.cpfsk = cpfsk_wform;
    ttl_wform.fsk = fsk_wform;
    ttl_wform.am_l = am_l_wform;
    ttl_wform.am_u = am_u_wform;
    ttl_wform.am_d = am_d_wform;
    ttl_wform.wbfm = wbfm_wform;
end















