#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Labo5 2
# Generated: Wed May 19 10:15:06 2021
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import numpy
import wx


class Labo5_2(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Labo5 2")
        _icon_path = "C:\Program Files\GNURadio-3.7\share\icons\hicolor\scalable/apps\gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 16
        self.samp_rate_0 = samp_rate_0 = 16000
        self.samp_rate = samp_rate = 128000
        self.RRCrolloff = RRCrolloff = 1
        self.M = M = 2

        ##################################################
        # Blocks
        ##################################################
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
        	self.GetWin(),
        	title='Diagrama de olho',
        	sample_rate=samp_rate,
        	v_scale=1.5,
        	v_offset=0,
        	t_scale=(sps/samp_rate)*4,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=3,
        	trig_mode=wxgui.TRIG_MODE_FREE,
        	y_axis_label='Amplitude',
        )
        self.GridAdd(self.wxgui_scopesink2_0.win, 0, 0, 4, 6)
        self.low_pass_filter_0_0_0_0 = filter.interp_fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, samp_rate/sps/2, (samp_rate/sps), firdes.WIN_RECTANGULAR, 100))
        self.digital_qam_mod_0 = digital.qam.qam_mod(
          constellation_points=M**2,
          mod_code="gray",
          differential=False,
          samples_per_symbol=sps,
          excess_bw=RRCrolloff,
          verbose=False,
          log=False,
          )
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((1, ))
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_complex_to_real_1 = blocks.complex_to_real(1)
        self.blocks_complex_to_real_0_0_0 = blocks.complex_to_real(1)
        self.blocks_complex_to_real_0_0 = blocks.complex_to_real(1)
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.blocks_add_const_vxx_0_0_0 = blocks.add_const_vff((-3.7, ))
        self.blocks_add_const_vxx_0_0 = blocks.add_const_vff((0, ))
        self.blocks_add_const_vxx_0 = blocks.add_const_vff((3.5, ))
        self.analog_random_source_x_1 = blocks.vector_source_b(map(int, numpy.random.randint(0, 255, 10000)), True)
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 0)
        self.Equalizador = filter.interp_fir_filter_ccc(1, ([-0.000000+0.000000j, 0.000005+0.000024j, 0.000010+0.000047j, 0.000017+0.000071j, 0.000023+0.000094j, 0.000031+0.000118j, 0.000039+0.000141j, 0.000047+0.000165j, 0.000056+0.000188j, 0.000066+0.000211j, 0.000076+0.000234j, 0.000088+0.000258j, 0.000099+0.000281j, 0.000112+0.000304j, 0.000125+0.000327j, 0.000139+0.000351j, 0.000153+0.000374j, 0.000169+0.000398j, 0.000185+0.000421j, 0.000202+0.000445j, 0.000219+0.000469j, 0.000238+0.000493j, 0.000257+0.000517j, 0.000278+0.000541j, 0.000299+0.000565j, 0.000321+0.000590j, 0.000344+0.000614j, 0.000369+0.000639j, 0.000394+0.000664j, 0.000420+0.000690j, 0.000448+0.000715j, 0.000477+0.000741j, 0.000507+0.000767j, 0.000539+0.000794j, 0.000572+0.000821j, 0.000606+0.000848j, 0.000642+0.000876j, 0.000679+0.000904j, 0.000719+0.000933j, 0.000760+0.000962j, 0.000803+0.000991j, 0.000848+0.001021j, 0.000895+0.001052j, 0.000944+0.001083j, 0.000996+0.001115j, 0.001050+0.001148j, 0.001107+0.001182j, 0.001167+0.001216j, 0.001230+0.001251j, 0.001296+0.001287j, 0.001366+0.001325j, 0.001439+0.001363j, 0.001517+0.001403j, 0.001599+0.001443j, 0.001685+0.001486j, 0.001776+0.001530j, 0.001873+0.001575j, 0.001976+0.001622j, 0.002085+0.001672j, 0.002201+0.001723j, 0.002325+0.001777j, 0.002457+0.001834j, 0.002598+0.001894j, 0.002748+0.001956j, 0.002910+0.002023j, 0.003084+0.002094j, 0.003272+0.002169j, 0.003475+0.002250j, 0.003694+0.002336j, 0.003932+0.002430j, 0.004191+0.002531j, 0.004475+0.002642j, 0.004785+0.002763j, 0.005127+0.002897j, 0.005504+0.003047j, 0.005923+0.003215j, 0.006389+0.003405j, 0.006911+0.003623j, 0.007499+0.003876j, 0.008165+0.004172j, 0.008922+0.004525j, 0.009790+0.004952j, 0.010788+0.005477j, 0.011945+0.006134j, 0.013289+0.006973j, 0.014855+0.008065j, 0.016676+0.009512j, 0.018778+0.011464j, 0.021161+0.014135j, 0.023763+0.017827j, 0.026404+0.022944j, 0.028678+0.029991j, 0.029803+0.039513j, 0.028431+0.051904j, 0.022484+0.067004j, 0.009226+0.083393j, -0.014096+0.097437j, -0.048542+0.102514j, -0.090489+0.089522j, -0.128292+0.050416j, -0.141758-0.014087j, -0.109759-0.085009j, -0.029017-0.123254j, 0.064845-0.089386j, 0.101421+0.013165j, 0.031609+0.107195j, -0.092572+0.088792j, -0.126567-0.041670j, -0.005395-0.120178j, 0.105468-0.014778j, 0.012668+0.115972j, -0.128539+0.025538j, -0.027954-0.118439j, 0.107875+0.004178j, -0.046000+0.114163j, -0.105871-0.071816j, 0.095191-0.054911j, -0.016061+0.119678j, -0.103818-0.073230j, 0.107109-0.022285j, -0.077561+0.099072j, -0.019095-0.117949j, 0.064784+0.094414j, -0.119627-0.044584j, 0.109909-0.001165j, -0.121537+0.041902j, 0.090418-0.064044j, -0.098240+0.081069j, 0.075184-0.082604j, -0.096221+0.083455j, 0.087166-0.068403j, -0.118126+0.050729j, 0.109265-0.011932j, -0.124185-0.029605j, 0.077936+0.083887j, -0.038979-0.112948j, -0.056742+0.112300j, 0.099624-0.045211j, -0.118500-0.045810j, 0.016440+0.119626j, 0.075152-0.080179j, -0.123055-0.034981j, -0.004850+0.122987j, 0.102150-0.034926j, -0.071151-0.098726j, -0.107162+0.075436j, 0.061036+0.099422j, 0.087562-0.060620j, -0.061410-0.103445j, -0.130664+0.026128j, -0.033753+0.123751j, 0.084054+0.073653j, 0.091643-0.045400j, 0.001548-0.110419j, -0.096729-0.081713j, -0.138828+0.000511j, -0.118518+0.079041j, -0.064213+0.121972j, -0.006928+0.127100j, 0.035531+0.107716j, 0.058931+0.078866j, 0.066759+0.050821j, 0.064746+0.028337j, 0.057872+0.012374j, 0.049451+0.002029j, 0.041287-0.004156j, 0.034157-0.007540j, 0.028258-0.009163j, 0.023509-0.009741j, 0.019732-0.009732j, 0.016732-0.009414j, 0.014339-0.008950j, 0.012414-0.008433j, 0.010850-0.007911j, 0.009564-0.007411j, 0.008494-0.006943j, 0.007595-0.006511j, 0.006831-0.006116j, 0.006175-0.005755j, 0.005608-0.005426j, 0.005113-0.005125j, 0.004678-0.004851j, 0.004293-0.004599j, 0.003950-0.004367j, 0.003643-0.004154j, 0.003368-0.003957j, 0.003119-0.003775j, 0.002893-0.003605j, 0.002687-0.003447j, 0.002499-0.003300j, 0.002327-0.003162j, 0.002169-0.003032j, 0.002023-0.002910j, 0.001888-0.002796j, 0.001764-0.002687j, 0.001648-0.002585j, 0.001541-0.002488j, 0.001441-0.002396j, 0.001348-0.002308j, 0.001261-0.002224j, 0.001179-0.002145j, 0.001103-0.002068j, 0.001032-0.001995j, 0.000965-0.001926j, 0.000902-0.001859j, 0.000843-0.001794j, 0.000787-0.001732j, 0.000735-0.001673j, 0.000685-0.001615j, 0.000639-0.001560j, 0.000595-0.001506j, 0.000553-0.001454j, 0.000514-0.001404j, 0.000477-0.001356j, 0.000442-0.001308j, 0.000409-0.001263j, 0.000378-0.001218j, 0.000349-0.001175j, 0.000321-0.001133j, 0.000295-0.001092j, 0.000270-0.001052j, 0.000247-0.001013j, 0.000224-0.000975j, 0.000204-0.000938j, 0.000184-0.000901j, 0.000166-0.000866j, 0.000148-0.000831j, 0.000132-0.000797j, 0.000117-0.000763j, 0.000103-0.000731j, 0.000089-0.000699j, 0.000077-0.000667j, 0.000065-0.000636j, 0.000055-0.000605j, 0.000045-0.000575j, 0.000036-0.000546j, 0.000027-0.000517j, 0.000020-0.000488j, 0.000013-0.000460j, 0.000007-0.000432j, 0.000002-0.000404j, -0.000003-0.000377j, -0.000007-0.000350j, -0.000011-0.000324j, -0.000014-0.000298j, -0.000016-0.000272j, -0.000017-0.000246j, -0.000018-0.000220j, -0.000019-0.000195j, -0.000018-0.000170j, -0.000017-0.000145j, -0.000016-0.000121j, -0.000014-0.000096j, -0.000011-0.000072j, -0.000008-0.000048j, -0.000004-0.000024j]))
        self.Equalizador.declare_sample_delay(0)
        (self.Equalizador).set_block_alias("Equalizador (Filtro FIR)")
        self.Canal = filter.interp_fir_filter_ccc(1, ([-0.000000-0.000000j, -0.000004+0.000024j, -0.000008+0.000048j, -0.000011+0.000072j, -0.000014+0.000096j, -0.000016+0.000121j, -0.000017+0.000145j, -0.000018+0.000170j, -0.000019+0.000195j, -0.000018+0.000220j, -0.000017+0.000246j, -0.000016+0.000272j, -0.000014+0.000298j, -0.000011+0.000324j, -0.000007+0.000350j, -0.000003+0.000377j, 0.000002+0.000404j, 0.000007+0.000432j, 0.000013+0.000460j, 0.000020+0.000488j, 0.000027+0.000517j, 0.000036+0.000546j, 0.000045+0.000575j, 0.000055+0.000605j, 0.000065+0.000636j, 0.000077+0.000667j, 0.000089+0.000699j, 0.000103+0.000731j, 0.000117+0.000763j, 0.000132+0.000797j, 0.000148+0.000831j, 0.000166+0.000866j, 0.000184+0.000901j, 0.000204+0.000938j, 0.000224+0.000975j, 0.000247+0.001013j, 0.000270+0.001052j, 0.000295+0.001092j, 0.000321+0.001133j, 0.000349+0.001175j, 0.000378+0.001218j, 0.000409+0.001263j, 0.000442+0.001308j, 0.000477+0.001356j, 0.000514+0.001404j, 0.000553+0.001454j, 0.000595+0.001506j, 0.000639+0.001560j, 0.000685+0.001615j, 0.000735+0.001673j, 0.000787+0.001732j, 0.000843+0.001794j, 0.000902+0.001859j, 0.000965+0.001926j, 0.001032+0.001995j, 0.001103+0.002068j, 0.001179+0.002145j, 0.001261+0.002224j, 0.001348+0.002308j, 0.001441+0.002396j, 0.001541+0.002488j, 0.001648+0.002585j, 0.001764+0.002687j, 0.001888+0.002796j, 0.002023+0.002910j, 0.002169+0.003032j, 0.002327+0.003162j, 0.002499+0.003300j, 0.002687+0.003447j, 0.002893+0.003605j, 0.003119+0.003775j, 0.003368+0.003957j, 0.003643+0.004154j, 0.003950+0.004367j, 0.004293+0.004599j, 0.004678+0.004851j, 0.005113+0.005125j, 0.005608+0.005426j, 0.006175+0.005755j, 0.006831+0.006116j, 0.007595+0.006511j, 0.008494+0.006943j, 0.009564+0.007411j, 0.010850+0.007911j, 0.012414+0.008433j, 0.014339+0.008950j, 0.016732+0.009414j, 0.019732+0.009732j, 0.023509+0.009741j, 0.028258+0.009163j, 0.034157+0.007540j, 0.041287+0.004156j, 0.049451-0.002029j, 0.057872-0.012374j, 0.064746-0.028337j, 0.066759-0.050821j, 0.058931-0.078866j, 0.035531-0.107716j, -0.006928-0.127100j, -0.064213-0.121972j, -0.118518-0.079041j, -0.138828-0.000511j, -0.096729+0.081713j, 0.001548+0.110419j, 0.091643+0.045400j, 0.084054-0.073653j, -0.033753-0.123751j, -0.130664-0.026128j, -0.061410+0.103445j, 0.087562+0.060620j, 0.061036-0.099422j, -0.107162-0.075436j, -0.071151+0.098726j, 0.102150+0.034926j, -0.004850-0.122987j, -0.123055+0.034981j, 0.075152+0.080179j, 0.016440-0.119626j, -0.118500+0.045810j, 0.099624+0.045211j, -0.056742-0.112300j, -0.038979+0.112948j, 0.077936-0.083887j, -0.124185+0.029605j, 0.109265+0.011932j, -0.118126-0.050729j, 0.087166+0.068403j, -0.096221-0.083455j, 0.075184+0.082604j, -0.098240-0.081069j, 0.090418+0.064044j, -0.121537-0.041902j, 0.109909+0.001165j, -0.119627+0.044584j, 0.064784-0.094414j, -0.019095+0.117949j, -0.077561-0.099072j, 0.107109+0.022285j, -0.103818+0.073230j, -0.016061-0.119678j, 0.095191+0.054911j, -0.105871+0.071816j, -0.046000-0.114163j, 0.107875-0.004178j, -0.027954+0.118439j, -0.128539-0.025538j, 0.012668-0.115972j, 0.105468+0.014778j, -0.005395+0.120178j, -0.126567+0.041670j, -0.092572-0.088792j, 0.031609-0.107195j, 0.101421-0.013165j, 0.064845+0.089386j, -0.029017+0.123254j, -0.109759+0.085009j, -0.141758+0.014087j, -0.128292-0.050416j, -0.090489-0.089522j, -0.048542-0.102514j, -0.014096-0.097437j, 0.009226-0.083393j, 0.022484-0.067004j, 0.028431-0.051904j, 0.029803-0.039513j, 0.028678-0.029991j, 0.026404-0.022944j, 0.023763-0.017827j, 0.021161-0.014135j, 0.018778-0.011464j, 0.016676-0.009512j, 0.014855-0.008065j, 0.013289-0.006973j, 0.011945-0.006134j, 0.010788-0.005477j, 0.009790-0.004952j, 0.008922-0.004525j, 0.008165-0.004172j, 0.007499-0.003876j, 0.006911-0.003623j, 0.006389-0.003405j, 0.005923-0.003215j, 0.005504-0.003047j, 0.005127-0.002897j, 0.004785-0.002763j, 0.004475-0.002642j, 0.004191-0.002531j, 0.003932-0.002430j, 0.003694-0.002336j, 0.003475-0.002250j, 0.003272-0.002169j, 0.003084-0.002094j, 0.002910-0.002023j, 0.002748-0.001956j, 0.002598-0.001894j, 0.002457-0.001834j, 0.002325-0.001777j, 0.002201-0.001723j, 0.002085-0.001672j, 0.001976-0.001622j, 0.001873-0.001575j, 0.001776-0.001530j, 0.001685-0.001486j, 0.001599-0.001443j, 0.001517-0.001403j, 0.001439-0.001363j, 0.001366-0.001325j, 0.001296-0.001287j, 0.001230-0.001251j, 0.001167-0.001216j, 0.001107-0.001182j, 0.001050-0.001148j, 0.000996-0.001115j, 0.000944-0.001083j, 0.000895-0.001052j, 0.000848-0.001021j, 0.000803-0.000991j, 0.000760-0.000962j, 0.000719-0.000933j, 0.000679-0.000904j, 0.000642-0.000876j, 0.000606-0.000848j, 0.000572-0.000821j, 0.000539-0.000794j, 0.000507-0.000767j, 0.000477-0.000741j, 0.000448-0.000715j, 0.000420-0.000690j, 0.000394-0.000664j, 0.000369-0.000639j, 0.000344-0.000614j, 0.000321-0.000590j, 0.000299-0.000565j, 0.000278-0.000541j, 0.000257-0.000517j, 0.000238-0.000493j, 0.000219-0.000469j, 0.000202-0.000445j, 0.000185-0.000421j, 0.000169-0.000398j, 0.000153-0.000374j, 0.000139-0.000351j, 0.000125-0.000327j, 0.000112-0.000304j, 0.000099-0.000281j, 0.000088-0.000258j, 0.000076-0.000234j, 0.000066-0.000211j, 0.000056-0.000188j, 0.000047-0.000165j, 0.000039-0.000141j, 0.000031-0.000118j, 0.000023-0.000094j, 0.000017-0.000071j, 0.000010-0.000047j, 0.000005-0.000024j]))
        self.Canal.declare_sample_delay(0)
        (self.Canal).set_block_alias("Canal")



        ##################################################
        # Connections
        ##################################################
        self.connect((self.Canal, 0), (self.Equalizador, 0))
        self.connect((self.Canal, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.Equalizador, 0), (self.blocks_complex_to_real_0_0_0, 0))
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.analog_random_source_x_1, 0), (self.digital_qam_mod_0, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.wxgui_scopesink2_0, 0))
        self.connect((self.blocks_add_const_vxx_0_0, 0), (self.wxgui_scopesink2_0, 1))
        self.connect((self.blocks_add_const_vxx_0_0_0, 0), (self.wxgui_scopesink2_0, 2))
        self.connect((self.blocks_complex_to_real_0, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.blocks_complex_to_real_0_0, 0), (self.blocks_add_const_vxx_0_0, 0))
        self.connect((self.blocks_complex_to_real_0_0_0, 0), (self.blocks_add_const_vxx_0_0_0, 0))
        self.connect((self.blocks_complex_to_real_1, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.low_pass_filter_0_0_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_complex_to_real_0_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_complex_to_real_0, 0))
        self.connect((self.digital_qam_mod_0, 0), (self.blocks_complex_to_real_1, 0))
        self.connect((self.low_pass_filter_0_0_0_0, 0), (self.Canal, 0))
        self.connect((self.low_pass_filter_0_0_0_0, 0), (self.blocks_throttle_0, 0))

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.low_pass_filter_0_0_0_0.set_taps(firdes.low_pass(1, self.samp_rate, self.samp_rate/self.sps/2, (self.samp_rate/self.sps), firdes.WIN_RECTANGULAR, 100))

    def get_samp_rate_0(self):
        return self.samp_rate_0

    def set_samp_rate_0(self, samp_rate_0):
        self.samp_rate_0 = samp_rate_0

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)
        self.low_pass_filter_0_0_0_0.set_taps(firdes.low_pass(1, self.samp_rate, self.samp_rate/self.sps/2, (self.samp_rate/self.sps), firdes.WIN_RECTANGULAR, 100))
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_RRCrolloff(self):
        return self.RRCrolloff

    def set_RRCrolloff(self, RRCrolloff):
        self.RRCrolloff = RRCrolloff

    def get_M(self):
        return self.M

    def set_M(self, M):
        self.M = M


def main(top_block_cls=Labo5_2, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
