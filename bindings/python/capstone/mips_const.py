# For Capstone Engine. AUTO-GENERATED FILE, DO NOT EDIT [mips_const.py]

# Operand type for instruction's operands

MIPS_OP_INVALID = 0
MIPS_OP_REG = 1
MIPS_OP_IMM = 2
MIPS_OP_MEM = 3

# MIPS registers

MIPS_REG_INVALID = 0

# General purpose registers
MIPS_REG_PC = 1
MIPS_REG_0 = 2
MIPS_REG_1 = 3
MIPS_REG_2 = 4
MIPS_REG_3 = 5
MIPS_REG_4 = 6
MIPS_REG_5 = 7
MIPS_REG_6 = 8
MIPS_REG_7 = 9
MIPS_REG_8 = 10
MIPS_REG_9 = 11
MIPS_REG_10 = 12
MIPS_REG_11 = 13
MIPS_REG_12 = 14
MIPS_REG_13 = 15
MIPS_REG_14 = 16
MIPS_REG_15 = 17
MIPS_REG_16 = 18
MIPS_REG_17 = 19
MIPS_REG_18 = 20
MIPS_REG_19 = 21
MIPS_REG_20 = 22
MIPS_REG_21 = 23
MIPS_REG_22 = 24
MIPS_REG_23 = 25
MIPS_REG_24 = 26
MIPS_REG_25 = 27
MIPS_REG_26 = 28
MIPS_REG_27 = 29
MIPS_REG_28 = 30
MIPS_REG_29 = 31
MIPS_REG_30 = 32
MIPS_REG_31 = 33

# DSP registers
MIPS_REG_DSPCCOND = 34
MIPS_REG_DSPCARRY = 35
MIPS_REG_DSPEFI = 36
MIPS_REG_DSPOUTFLAG = 37
MIPS_REG_DSPOUTFLAG16_19 = 38
MIPS_REG_DSPOUTFLAG20 = 39
MIPS_REG_DSPOUTFLAG21 = 40
MIPS_REG_DSPOUTFLAG22 = 41
MIPS_REG_DSPOUTFLAG23 = 42
MIPS_REG_DSPPOS = 43
MIPS_REG_DSPSCOUNT = 44

# ACC registers
MIPS_REG_AC0 = 45
MIPS_REG_AC1 = 46
MIPS_REG_AC2 = 47
MIPS_REG_AC3 = 48

# COP registers
MIPS_REG_CC0 = 49
MIPS_REG_CC1 = 50
MIPS_REG_CC2 = 51
MIPS_REG_CC3 = 52
MIPS_REG_CC4 = 53
MIPS_REG_CC5 = 54
MIPS_REG_CC6 = 55
MIPS_REG_CC7 = 56

# FPU registers
MIPS_REG_F0 = 57
MIPS_REG_F1 = 58
MIPS_REG_F2 = 59
MIPS_REG_F3 = 60
MIPS_REG_F4 = 61
MIPS_REG_F5 = 62
MIPS_REG_F6 = 63
MIPS_REG_F7 = 64
MIPS_REG_F8 = 65
MIPS_REG_F9 = 66
MIPS_REG_F10 = 67
MIPS_REG_F11 = 68
MIPS_REG_F12 = 69
MIPS_REG_F13 = 70
MIPS_REG_F14 = 71
MIPS_REG_F15 = 72
MIPS_REG_F16 = 73
MIPS_REG_F17 = 74
MIPS_REG_F18 = 75
MIPS_REG_F19 = 76
MIPS_REG_F20 = 77
MIPS_REG_F21 = 78
MIPS_REG_F22 = 79
MIPS_REG_F23 = 80
MIPS_REG_F24 = 81
MIPS_REG_F25 = 82
MIPS_REG_F26 = 83
MIPS_REG_F27 = 84
MIPS_REG_F28 = 85
MIPS_REG_F29 = 86
MIPS_REG_F30 = 87
MIPS_REG_F31 = 88
MIPS_REG_FCC0 = 89
MIPS_REG_FCC1 = 90
MIPS_REG_FCC2 = 91
MIPS_REG_FCC3 = 92
MIPS_REG_FCC4 = 93
MIPS_REG_FCC5 = 94
MIPS_REG_FCC6 = 95
MIPS_REG_FCC7 = 96

# AFPR128
MIPS_REG_W0 = 97
MIPS_REG_W1 = 98
MIPS_REG_W2 = 99
MIPS_REG_W3 = 100
MIPS_REG_W4 = 101
MIPS_REG_W5 = 102
MIPS_REG_W6 = 103
MIPS_REG_W7 = 104
MIPS_REG_W8 = 105
MIPS_REG_W9 = 106
MIPS_REG_W10 = 107
MIPS_REG_W11 = 108
MIPS_REG_W12 = 109
MIPS_REG_W13 = 110
MIPS_REG_W14 = 111
MIPS_REG_W15 = 112
MIPS_REG_W16 = 113
MIPS_REG_W17 = 114
MIPS_REG_W18 = 115
MIPS_REG_W19 = 116
MIPS_REG_W20 = 117
MIPS_REG_W21 = 118
MIPS_REG_W22 = 119
MIPS_REG_W23 = 120
MIPS_REG_W24 = 121
MIPS_REG_W25 = 122
MIPS_REG_W26 = 123
MIPS_REG_W27 = 124
MIPS_REG_W28 = 125
MIPS_REG_W29 = 126
MIPS_REG_W30 = 127
MIPS_REG_W31 = 128
MIPS_REG_HI = 129
MIPS_REG_LO = 130
MIPS_REG_P0 = 131
MIPS_REG_P1 = 132
MIPS_REG_P2 = 133
MIPS_REG_MPL0 = 134
MIPS_REG_MPL1 = 135
MIPS_REG_MPL2 = 136
MIPS_REG_ENDING = 137
MIPS_REG_ZERO = MIPS_REG_0
MIPS_REG_AT = MIPS_REG_1
MIPS_REG_V0 = MIPS_REG_2
MIPS_REG_V1 = MIPS_REG_3
MIPS_REG_A0 = MIPS_REG_4
MIPS_REG_A1 = MIPS_REG_5
MIPS_REG_A2 = MIPS_REG_6
MIPS_REG_A3 = MIPS_REG_7
MIPS_REG_T0 = MIPS_REG_8
MIPS_REG_T1 = MIPS_REG_9
MIPS_REG_T2 = MIPS_REG_10
MIPS_REG_T3 = MIPS_REG_11
MIPS_REG_T4 = MIPS_REG_12
MIPS_REG_T5 = MIPS_REG_13
MIPS_REG_T6 = MIPS_REG_14
MIPS_REG_T7 = MIPS_REG_15
MIPS_REG_S0 = MIPS_REG_16
MIPS_REG_S1 = MIPS_REG_17
MIPS_REG_S2 = MIPS_REG_18
MIPS_REG_S3 = MIPS_REG_19
MIPS_REG_S4 = MIPS_REG_20
MIPS_REG_S5 = MIPS_REG_21
MIPS_REG_S6 = MIPS_REG_22
MIPS_REG_S7 = MIPS_REG_23
MIPS_REG_T8 = MIPS_REG_24
MIPS_REG_T9 = MIPS_REG_25
MIPS_REG_K0 = MIPS_REG_26
MIPS_REG_K1 = MIPS_REG_27
MIPS_REG_GP = MIPS_REG_28
MIPS_REG_SP = MIPS_REG_29
MIPS_REG_FP = MIPS_REG_30
MIPS_REG_S8 = MIPS_REG_30
MIPS_REG_RA = MIPS_REG_31
MIPS_REG_HI0 = MIPS_REG_AC0
MIPS_REG_HI1 = MIPS_REG_AC1
MIPS_REG_HI2 = MIPS_REG_AC2
MIPS_REG_HI3 = MIPS_REG_AC3
MIPS_REG_LO0 = MIPS_REG_HI0
MIPS_REG_LO1 = MIPS_REG_HI1
MIPS_REG_LO2 = MIPS_REG_HI2
MIPS_REG_LO3 = MIPS_REG_HI3

# MIPS instruction

MIPS_INS_INVALID = 0
MIPS_INS_ABSQ_S = 1
MIPS_INS_ADD = 2
MIPS_INS_ADDIUPC = 3
MIPS_INS_ADDIUR1SP = 4
MIPS_INS_ADDIUR2 = 5
MIPS_INS_ADDIUS5 = 6
MIPS_INS_ADDIUSP = 7
MIPS_INS_ADDQH = 8
MIPS_INS_ADDQH_R = 9
MIPS_INS_ADDQ = 10
MIPS_INS_ADDQ_S = 11
MIPS_INS_ADDSC = 12
MIPS_INS_ADDS_A = 13
MIPS_INS_ADDS_S = 14
MIPS_INS_ADDS_U = 15
MIPS_INS_ADDU16 = 16
MIPS_INS_ADDUH = 17
MIPS_INS_ADDUH_R = 18
MIPS_INS_ADDU = 19
MIPS_INS_ADDU_S = 20
MIPS_INS_ADDVI = 21
MIPS_INS_ADDV = 22
MIPS_INS_ADDWC = 23
MIPS_INS_ADD_A = 24
MIPS_INS_ADDI = 25
MIPS_INS_ADDIU = 26
MIPS_INS_ALIGN = 27
MIPS_INS_ALUIPC = 28
MIPS_INS_AND = 29
MIPS_INS_AND16 = 30
MIPS_INS_ANDI16 = 31
MIPS_INS_ANDI = 32
MIPS_INS_APPEND = 33
MIPS_INS_ASUB_S = 34
MIPS_INS_ASUB_U = 35
MIPS_INS_AUI = 36
MIPS_INS_AUIPC = 37
MIPS_INS_AVER_S = 38
MIPS_INS_AVER_U = 39
MIPS_INS_AVE_S = 40
MIPS_INS_AVE_U = 41
MIPS_INS_B16 = 42
MIPS_INS_BADDU = 43
MIPS_INS_BAL = 44
MIPS_INS_BALC = 45
MIPS_INS_BALIGN = 46
MIPS_INS_BBIT0 = 47
MIPS_INS_BBIT032 = 48
MIPS_INS_BBIT1 = 49
MIPS_INS_BBIT132 = 50
MIPS_INS_BC = 51
MIPS_INS_BC0F = 52
MIPS_INS_BC0FL = 53
MIPS_INS_BC0T = 54
MIPS_INS_BC0TL = 55
MIPS_INS_BC1EQZ = 56
MIPS_INS_BC1F = 57
MIPS_INS_BC1FL = 58
MIPS_INS_BC1NEZ = 59
MIPS_INS_BC1T = 60
MIPS_INS_BC1TL = 61
MIPS_INS_BC2EQZ = 62
MIPS_INS_BC2F = 63
MIPS_INS_BC2FL = 64
MIPS_INS_BC2NEZ = 65
MIPS_INS_BC2T = 66
MIPS_INS_BC2TL = 67
MIPS_INS_BC3F = 68
MIPS_INS_BC3FL = 69
MIPS_INS_BC3T = 70
MIPS_INS_BC3TL = 71
MIPS_INS_BCLRI = 72
MIPS_INS_BCLR = 73
MIPS_INS_BEQ = 74
MIPS_INS_BEQC = 75
MIPS_INS_BEQL = 76
MIPS_INS_BEQZ16 = 77
MIPS_INS_BEQZALC = 78
MIPS_INS_BEQZC = 79
MIPS_INS_BGEC = 80
MIPS_INS_BGEUC = 81
MIPS_INS_BGEZ = 82
MIPS_INS_BGEZAL = 83
MIPS_INS_BGEZALC = 84
MIPS_INS_BGEZALL = 85
MIPS_INS_BGEZALS = 86
MIPS_INS_BGEZC = 87
MIPS_INS_BGEZL = 88
MIPS_INS_BGTZ = 89
MIPS_INS_BGTZALC = 90
MIPS_INS_BGTZC = 91
MIPS_INS_BGTZL = 92
MIPS_INS_BINSLI = 93
MIPS_INS_BINSL = 94
MIPS_INS_BINSRI = 95
MIPS_INS_BINSR = 96
MIPS_INS_BITREV = 97
MIPS_INS_BITSWAP = 98
MIPS_INS_BLEZ = 99
MIPS_INS_BLEZALC = 100
MIPS_INS_BLEZC = 101
MIPS_INS_BLEZL = 102
MIPS_INS_BLTC = 103
MIPS_INS_BLTUC = 104
MIPS_INS_BLTZ = 105
MIPS_INS_BLTZAL = 106
MIPS_INS_BLTZALC = 107
MIPS_INS_BLTZALL = 108
MIPS_INS_BLTZALS = 109
MIPS_INS_BLTZC = 110
MIPS_INS_BLTZL = 111
MIPS_INS_BMNZI = 112
MIPS_INS_BMNZ = 113
MIPS_INS_BMZI = 114
MIPS_INS_BMZ = 115
MIPS_INS_BNE = 116
MIPS_INS_BNEC = 117
MIPS_INS_BNEGI = 118
MIPS_INS_BNEG = 119
MIPS_INS_BNEL = 120
MIPS_INS_BNEZ16 = 121
MIPS_INS_BNEZALC = 122
MIPS_INS_BNEZC = 123
MIPS_INS_BNVC = 124
MIPS_INS_BNZ = 125
MIPS_INS_BOVC = 126
MIPS_INS_BPOSGE32 = 127
MIPS_INS_BREAK = 128
MIPS_INS_BREAK16 = 129
MIPS_INS_BSELI = 130
MIPS_INS_BSEL = 131
MIPS_INS_BSETI = 132
MIPS_INS_BSET = 133
MIPS_INS_BZ = 134
MIPS_INS_BEQZ = 135
MIPS_INS_B = 136
MIPS_INS_BNEZ = 137
MIPS_INS_BTEQZ = 138
MIPS_INS_BTNEZ = 139
MIPS_INS_CACHE = 140
MIPS_INS_CEIL = 141
MIPS_INS_CEQI = 142
MIPS_INS_CEQ = 143
MIPS_INS_CFC1 = 144
MIPS_INS_CFCMSA = 145
MIPS_INS_CINS = 146
MIPS_INS_CINS32 = 147
MIPS_INS_CLASS = 148
MIPS_INS_CLEI_S = 149
MIPS_INS_CLEI_U = 150
MIPS_INS_CLE_S = 151
MIPS_INS_CLE_U = 152
MIPS_INS_CLO = 153
MIPS_INS_CLTI_S = 154
MIPS_INS_CLTI_U = 155
MIPS_INS_CLT_S = 156
MIPS_INS_CLT_U = 157
MIPS_INS_CLZ = 158
MIPS_INS_CMPGDU = 159
MIPS_INS_CMPGU = 160
MIPS_INS_CMPU = 161
MIPS_INS_CMP = 162
MIPS_INS_COPY_S = 163
MIPS_INS_COPY_U = 164
MIPS_INS_CTC1 = 165
MIPS_INS_CTCMSA = 166
MIPS_INS_CVT = 167
MIPS_INS_C = 168
MIPS_INS_CMPI = 169
MIPS_INS_DADD = 170
MIPS_INS_DADDI = 171
MIPS_INS_DADDIU = 172
MIPS_INS_DADDU = 173
MIPS_INS_DAHI = 174
MIPS_INS_DALIGN = 175
MIPS_INS_DATI = 176
MIPS_INS_DAUI = 177
MIPS_INS_DBITSWAP = 178
MIPS_INS_DCLO = 179
MIPS_INS_DCLZ = 180
MIPS_INS_DDIV = 181
MIPS_INS_DDIVU = 182
MIPS_INS_DERET = 183
MIPS_INS_DEXT = 184
MIPS_INS_DEXTM = 185
MIPS_INS_DEXTU = 186
MIPS_INS_DI = 187
MIPS_INS_DINS = 188
MIPS_INS_DINSM = 189
MIPS_INS_DINSU = 190
MIPS_INS_DIV = 191
MIPS_INS_DIVU = 192
MIPS_INS_DIV_S = 193
MIPS_INS_DIV_U = 194
MIPS_INS_DLSA = 195
MIPS_INS_DMFC0 = 196
MIPS_INS_DMFC1 = 197
MIPS_INS_DMFC2 = 198
MIPS_INS_DMOD = 199
MIPS_INS_DMODU = 200
MIPS_INS_DMTC0 = 201
MIPS_INS_DMTC1 = 202
MIPS_INS_DMTC2 = 203
MIPS_INS_DMUH = 204
MIPS_INS_DMUHU = 205
MIPS_INS_DMUL = 206
MIPS_INS_DMULT = 207
MIPS_INS_DMULTU = 208
MIPS_INS_DMULU = 209
MIPS_INS_DOTP_S = 210
MIPS_INS_DOTP_U = 211
MIPS_INS_DPADD_S = 212
MIPS_INS_DPADD_U = 213
MIPS_INS_DPAQX_SA = 214
MIPS_INS_DPAQX_S = 215
MIPS_INS_DPAQ_SA = 216
MIPS_INS_DPAQ_S = 217
MIPS_INS_DPAU = 218
MIPS_INS_DPAX = 219
MIPS_INS_DPA = 220
MIPS_INS_DPOP = 221
MIPS_INS_DPSQX_SA = 222
MIPS_INS_DPSQX_S = 223
MIPS_INS_DPSQ_SA = 224
MIPS_INS_DPSQ_S = 225
MIPS_INS_DPSUB_S = 226
MIPS_INS_DPSUB_U = 227
MIPS_INS_DPSU = 228
MIPS_INS_DPSX = 229
MIPS_INS_DPS = 230
MIPS_INS_DROTR = 231
MIPS_INS_DROTR32 = 232
MIPS_INS_DROTRV = 233
MIPS_INS_DSBH = 234
MIPS_INS_DSHD = 235
MIPS_INS_DSLL = 236
MIPS_INS_DSLL32 = 237
MIPS_INS_DSLLV = 238
MIPS_INS_DSRA = 239
MIPS_INS_DSRA32 = 240
MIPS_INS_DSRAV = 241
MIPS_INS_DSRL = 242
MIPS_INS_DSRL32 = 243
MIPS_INS_DSRLV = 244
MIPS_INS_DSUB = 245
MIPS_INS_DSUBU = 246
MIPS_INS_EHB = 247
MIPS_INS_EI = 248
MIPS_INS_ERET = 249
MIPS_INS_EXT = 250
MIPS_INS_EXTP = 251
MIPS_INS_EXTPDP = 252
MIPS_INS_EXTPDPV = 253
MIPS_INS_EXTPV = 254
MIPS_INS_EXTRV_RS = 255
MIPS_INS_EXTRV_R = 256
MIPS_INS_EXTRV_S = 257
MIPS_INS_EXTRV = 258
MIPS_INS_EXTR_RS = 259
MIPS_INS_EXTR_R = 260
MIPS_INS_EXTR_S = 261
MIPS_INS_EXTR = 262
MIPS_INS_EXTS = 263
MIPS_INS_EXTS32 = 264
MIPS_INS_ABS = 265
MIPS_INS_FADD = 266
MIPS_INS_FCAF = 267
MIPS_INS_FCEQ = 268
MIPS_INS_FCLASS = 269
MIPS_INS_FCLE = 270
MIPS_INS_FCLT = 271
MIPS_INS_FCNE = 272
MIPS_INS_FCOR = 273
MIPS_INS_FCUEQ = 274
MIPS_INS_FCULE = 275
MIPS_INS_FCULT = 276
MIPS_INS_FCUNE = 277
MIPS_INS_FCUN = 278
MIPS_INS_FDIV = 279
MIPS_INS_FEXDO = 280
MIPS_INS_FEXP2 = 281
MIPS_INS_FEXUPL = 282
MIPS_INS_FEXUPR = 283
MIPS_INS_FFINT_S = 284
MIPS_INS_FFINT_U = 285
MIPS_INS_FFQL = 286
MIPS_INS_FFQR = 287
MIPS_INS_FILL = 288
MIPS_INS_FLOG2 = 289
MIPS_INS_FLOOR = 290
MIPS_INS_FMADD = 291
MIPS_INS_FMAX_A = 292
MIPS_INS_FMAX = 293
MIPS_INS_FMIN_A = 294
MIPS_INS_FMIN = 295
MIPS_INS_MOV = 296
MIPS_INS_FMSUB = 297
MIPS_INS_FMUL = 298
MIPS_INS_MUL = 299
MIPS_INS_NEG = 300
MIPS_INS_FRCP = 301
MIPS_INS_FRINT = 302
MIPS_INS_FRSQRT = 303
MIPS_INS_FSAF = 304
MIPS_INS_FSEQ = 305
MIPS_INS_FSLE = 306
MIPS_INS_FSLT = 307
MIPS_INS_FSNE = 308
MIPS_INS_FSOR = 309
MIPS_INS_FSQRT = 310
MIPS_INS_SQRT = 311
MIPS_INS_FSUB = 312
MIPS_INS_SUB = 313
MIPS_INS_FSUEQ = 314
MIPS_INS_FSULE = 315
MIPS_INS_FSULT = 316
MIPS_INS_FSUNE = 317
MIPS_INS_FSUN = 318
MIPS_INS_FTINT_S = 319
MIPS_INS_FTINT_U = 320
MIPS_INS_FTQ = 321
MIPS_INS_FTRUNC_S = 322
MIPS_INS_FTRUNC_U = 323
MIPS_INS_HADD_S = 324
MIPS_INS_HADD_U = 325
MIPS_INS_HSUB_S = 326
MIPS_INS_HSUB_U = 327
MIPS_INS_ILVEV = 328
MIPS_INS_ILVL = 329
MIPS_INS_ILVOD = 330
MIPS_INS_ILVR = 331
MIPS_INS_INS = 332
MIPS_INS_INSERT = 333
MIPS_INS_INSV = 334
MIPS_INS_INSVE = 335
MIPS_INS_J = 336
MIPS_INS_JAL = 337
MIPS_INS_JALR = 338
MIPS_INS_JALRS16 = 339
MIPS_INS_JALRS = 340
MIPS_INS_JALS = 341
MIPS_INS_JALX = 342
MIPS_INS_JIALC = 343
MIPS_INS_JIC = 344
MIPS_INS_JR = 345
MIPS_INS_JR16 = 346
MIPS_INS_JRADDIUSP = 347
MIPS_INS_JRC = 348
MIPS_INS_JALRC = 349
MIPS_INS_LB = 350
MIPS_INS_LBU16 = 351
MIPS_INS_LBUX = 352
MIPS_INS_LBU = 353
MIPS_INS_LD = 354
MIPS_INS_LDC1 = 355
MIPS_INS_LDC2 = 356
MIPS_INS_LDC3 = 357
MIPS_INS_LDI = 358
MIPS_INS_LDL = 359
MIPS_INS_LDPC = 360
MIPS_INS_LDR = 361
MIPS_INS_LDXC1 = 362
MIPS_INS_LH = 363
MIPS_INS_LHU16 = 364
MIPS_INS_LHX = 365
MIPS_INS_LHU = 366
MIPS_INS_LI16 = 367
MIPS_INS_LL = 368
MIPS_INS_LLD = 369
MIPS_INS_LSA = 370
MIPS_INS_LUXC1 = 371
MIPS_INS_LUI = 372
MIPS_INS_LW = 373
MIPS_INS_LW16 = 374
MIPS_INS_LWC1 = 375
MIPS_INS_LWC2 = 376
MIPS_INS_LWC3 = 377
MIPS_INS_LWL = 378
MIPS_INS_LWM16 = 379
MIPS_INS_LWM32 = 380
MIPS_INS_LWPC = 381
MIPS_INS_LWP = 382
MIPS_INS_LWR = 383
MIPS_INS_LWUPC = 384
MIPS_INS_LWU = 385
MIPS_INS_LWX = 386
MIPS_INS_LWXC1 = 387
MIPS_INS_LWXS = 388
MIPS_INS_LI = 389
MIPS_INS_MADD = 390
MIPS_INS_MADDF = 391
MIPS_INS_MADDR_Q = 392
MIPS_INS_MADDU = 393
MIPS_INS_MADDV = 394
MIPS_INS_MADD_Q = 395
MIPS_INS_MAQ_SA = 396
MIPS_INS_MAQ_S = 397
MIPS_INS_MAXA = 398
MIPS_INS_MAXI_S = 399
MIPS_INS_MAXI_U = 400
MIPS_INS_MAX_A = 401
MIPS_INS_MAX = 402
MIPS_INS_MAX_S = 403
MIPS_INS_MAX_U = 404
MIPS_INS_MFC0 = 405
MIPS_INS_MFC1 = 406
MIPS_INS_MFC2 = 407
MIPS_INS_MFHC1 = 408
MIPS_INS_MFHI = 409
MIPS_INS_MFLO = 410
MIPS_INS_MINA = 411
MIPS_INS_MINI_S = 412
MIPS_INS_MINI_U = 413
MIPS_INS_MIN_A = 414
MIPS_INS_MIN = 415
MIPS_INS_MIN_S = 416
MIPS_INS_MIN_U = 417
MIPS_INS_MOD = 418
MIPS_INS_MODSUB = 419
MIPS_INS_MODU = 420
MIPS_INS_MOD_S = 421
MIPS_INS_MOD_U = 422
MIPS_INS_MOVE = 423
MIPS_INS_MOVEP = 424
MIPS_INS_MOVF = 425
MIPS_INS_MOVN = 426
MIPS_INS_MOVT = 427
MIPS_INS_MOVZ = 428
MIPS_INS_MSUB = 429
MIPS_INS_MSUBF = 430
MIPS_INS_MSUBR_Q = 431
MIPS_INS_MSUBU = 432
MIPS_INS_MSUBV = 433
MIPS_INS_MSUB_Q = 434
MIPS_INS_MTC0 = 435
MIPS_INS_MTC1 = 436
MIPS_INS_MTC2 = 437
MIPS_INS_MTHC1 = 438
MIPS_INS_MTHI = 439
MIPS_INS_MTHLIP = 440
MIPS_INS_MTLO = 441
MIPS_INS_MTM0 = 442
MIPS_INS_MTM1 = 443
MIPS_INS_MTM2 = 444
MIPS_INS_MTP0 = 445
MIPS_INS_MTP1 = 446
MIPS_INS_MTP2 = 447
MIPS_INS_MUH = 448
MIPS_INS_MUHU = 449
MIPS_INS_MULEQ_S = 450
MIPS_INS_MULEU_S = 451
MIPS_INS_MULQ_RS = 452
MIPS_INS_MULQ_S = 453
MIPS_INS_MULR_Q = 454
MIPS_INS_MULSAQ_S = 455
MIPS_INS_MULSA = 456
MIPS_INS_MULT = 457
MIPS_INS_MULTU = 458
MIPS_INS_MULU = 459
MIPS_INS_MULV = 460
MIPS_INS_MUL_Q = 461
MIPS_INS_MUL_S = 462
MIPS_INS_NLOC = 463
MIPS_INS_NLZC = 464
MIPS_INS_NMADD = 465
MIPS_INS_NMSUB = 466
MIPS_INS_NOR = 467
MIPS_INS_NORI = 468
MIPS_INS_NOT16 = 469
MIPS_INS_NOT = 470
MIPS_INS_OR = 471
MIPS_INS_OR16 = 472
MIPS_INS_ORI = 473
MIPS_INS_PACKRL = 474
MIPS_INS_PAUSE = 475
MIPS_INS_PCKEV = 476
MIPS_INS_PCKOD = 477
MIPS_INS_PCNT = 478
MIPS_INS_PICK = 479
MIPS_INS_POP = 480
MIPS_INS_PRECEQU = 481
MIPS_INS_PRECEQ = 482
MIPS_INS_PRECEU = 483
MIPS_INS_PRECRQU_S = 484
MIPS_INS_PRECRQ = 485
MIPS_INS_PRECRQ_RS = 486
MIPS_INS_PRECR = 487
MIPS_INS_PRECR_SRA = 488
MIPS_INS_PRECR_SRA_R = 489
MIPS_INS_PREF = 490
MIPS_INS_PREPEND = 491
MIPS_INS_RADDU = 492
MIPS_INS_RDDSP = 493
MIPS_INS_RDHWR = 494
MIPS_INS_REPLV = 495
MIPS_INS_REPL = 496
MIPS_INS_RINT = 497
MIPS_INS_ROTR = 498
MIPS_INS_ROTRV = 499
MIPS_INS_ROUND = 500
MIPS_INS_SAT_S = 501
MIPS_INS_SAT_U = 502
MIPS_INS_SB = 503
MIPS_INS_SB16 = 504
MIPS_INS_SC = 505
MIPS_INS_SCD = 506
MIPS_INS_SD = 507
MIPS_INS_SDBBP = 508
MIPS_INS_SDBBP16 = 509
MIPS_INS_SDC1 = 510
MIPS_INS_SDC2 = 511
MIPS_INS_SDC3 = 512
MIPS_INS_SDL = 513
MIPS_INS_SDR = 514
MIPS_INS_SDXC1 = 515
MIPS_INS_SEB = 516
MIPS_INS_SEH = 517
MIPS_INS_SELEQZ = 518
MIPS_INS_SELNEZ = 519
MIPS_INS_SEL = 520
MIPS_INS_SEQ = 521
MIPS_INS_SEQI = 522
MIPS_INS_SH = 523
MIPS_INS_SH16 = 524
MIPS_INS_SHF = 525
MIPS_INS_SHILO = 526
MIPS_INS_SHILOV = 527
MIPS_INS_SHLLV = 528
MIPS_INS_SHLLV_S = 529
MIPS_INS_SHLL = 530
MIPS_INS_SHLL_S = 531
MIPS_INS_SHRAV = 532
MIPS_INS_SHRAV_R = 533
MIPS_INS_SHRA = 534
MIPS_INS_SHRA_R = 535
MIPS_INS_SHRLV = 536
MIPS_INS_SHRL = 537
MIPS_INS_SLDI = 538
MIPS_INS_SLD = 539
MIPS_INS_SLL = 540
MIPS_INS_SLL16 = 541
MIPS_INS_SLLI = 542
MIPS_INS_SLLV = 543
MIPS_INS_SLT = 544
MIPS_INS_SLTI = 545
MIPS_INS_SLTIU = 546
MIPS_INS_SLTU = 547
MIPS_INS_SNE = 548
MIPS_INS_SNEI = 549
MIPS_INS_SPLATI = 550
MIPS_INS_SPLAT = 551
MIPS_INS_SRA = 552
MIPS_INS_SRAI = 553
MIPS_INS_SRARI = 554
MIPS_INS_SRAR = 555
MIPS_INS_SRAV = 556
MIPS_INS_SRL = 557
MIPS_INS_SRL16 = 558
MIPS_INS_SRLI = 559
MIPS_INS_SRLRI = 560
MIPS_INS_SRLR = 561
MIPS_INS_SRLV = 562
MIPS_INS_SSNOP = 563
MIPS_INS_ST = 564
MIPS_INS_SUBQH = 565
MIPS_INS_SUBQH_R = 566
MIPS_INS_SUBQ = 567
MIPS_INS_SUBQ_S = 568
MIPS_INS_SUBSUS_U = 569
MIPS_INS_SUBSUU_S = 570
MIPS_INS_SUBS_S = 571
MIPS_INS_SUBS_U = 572
MIPS_INS_SUBU16 = 573
MIPS_INS_SUBUH = 574
MIPS_INS_SUBUH_R = 575
MIPS_INS_SUBU = 576
MIPS_INS_SUBU_S = 577
MIPS_INS_SUBVI = 578
MIPS_INS_SUBV = 579
MIPS_INS_SUXC1 = 580
MIPS_INS_SW = 581
MIPS_INS_SW16 = 582
MIPS_INS_SWC1 = 583
MIPS_INS_SWC2 = 584
MIPS_INS_SWC3 = 585
MIPS_INS_SWL = 586
MIPS_INS_SWM16 = 587
MIPS_INS_SWM32 = 588
MIPS_INS_SWP = 589
MIPS_INS_SWR = 590
MIPS_INS_SWXC1 = 591
MIPS_INS_SYNC = 592
MIPS_INS_SYNCI = 593
MIPS_INS_SYSCALL = 594
MIPS_INS_TEQ = 595
MIPS_INS_TEQI = 596
MIPS_INS_TGE = 597
MIPS_INS_TGEI = 598
MIPS_INS_TGEIU = 599
MIPS_INS_TGEU = 600
MIPS_INS_TLBP = 601
MIPS_INS_TLBR = 602
MIPS_INS_TLBWI = 603
MIPS_INS_TLBWR = 604
MIPS_INS_TLT = 605
MIPS_INS_TLTI = 606
MIPS_INS_TLTIU = 607
MIPS_INS_TLTU = 608
MIPS_INS_TNE = 609
MIPS_INS_TNEI = 610
MIPS_INS_TRUNC = 611
MIPS_INS_V3MULU = 612
MIPS_INS_VMM0 = 613
MIPS_INS_VMULU = 614
MIPS_INS_VSHF = 615
MIPS_INS_WAIT = 616
MIPS_INS_WRDSP = 617
MIPS_INS_WSBH = 618
MIPS_INS_XOR = 619
MIPS_INS_XOR16 = 620
MIPS_INS_XORI = 621

# some alias instructions
MIPS_INS_NOP = 622
MIPS_INS_NEGU = 623

# special instructions
MIPS_INS_JALR_HB = 624
MIPS_INS_JR_HB = 625
MIPS_INS_ENDING = 626

# Group of MIPS instructions

MIPS_GRP_INVALID = 0

# Generic groups
MIPS_GRP_JUMP = 1
MIPS_GRP_CALL = 2
MIPS_GRP_RET = 3
MIPS_GRP_INT = 4
MIPS_GRP_IRET = 5
MIPS_GRP_PRIVILEGE = 6
MIPS_GRP_BRANCH_RELATIVE = 7

# Architecture-specific groups
MIPS_GRP_BITCOUNT = 128
MIPS_GRP_DSP = 129
MIPS_GRP_DSPR2 = 130
MIPS_GRP_FPIDX = 131
MIPS_GRP_MSA = 132
MIPS_GRP_MIPS32R2 = 133
MIPS_GRP_MIPS64 = 134
MIPS_GRP_MIPS64R2 = 135
MIPS_GRP_SEINREG = 136
MIPS_GRP_STDENC = 137
MIPS_GRP_SWAP = 138
MIPS_GRP_MICROMIPS = 139
MIPS_GRP_MIPS16MODE = 140
MIPS_GRP_FP64BIT = 141
MIPS_GRP_NONANSFPMATH = 142
MIPS_GRP_NOTFP64BIT = 143
MIPS_GRP_NOTINMICROMIPS = 144
MIPS_GRP_NOTNACL = 145
MIPS_GRP_NOTMIPS32R6 = 146
MIPS_GRP_NOTMIPS64R6 = 147
MIPS_GRP_CNMIPS = 148
MIPS_GRP_MIPS32 = 149
MIPS_GRP_MIPS32R6 = 150
MIPS_GRP_MIPS64R6 = 151
MIPS_GRP_MIPS2 = 152
MIPS_GRP_MIPS3 = 153
MIPS_GRP_MIPS3_32 = 154
MIPS_GRP_MIPS3_32R2 = 155
MIPS_GRP_MIPS4_32 = 156
MIPS_GRP_MIPS4_32R2 = 157
MIPS_GRP_MIPS5_32R2 = 158
MIPS_GRP_GP32BIT = 159
MIPS_GRP_GP64BIT = 160
MIPS_GRP_ENDING = 161
