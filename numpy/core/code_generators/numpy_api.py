"""Here we define the exported functions, types, etc... which need to be
exported through a global C pointer.

Each dictionary contains name -> index pair.

Whenever you change one index, you break the ABI (and the ABI version number
should be incremented). Whenever you add an item to one of the dict, the API
needs to be updated.

When adding a function, make sure to use the next integer not used as an index
(in case you use an existing index or jump, the build will stop and raise an
exception, so it should hopefully not get unnoticed).
"""

multiarray_global_vars = {
    'NPY_NUMUSERTYPES':             6,
}

multiarray_global_vars_types = {
    'NPY_NUMUSERTYPES':             'int',
}

multiarray_scalar_bool_values = {
    '_PyArrayScalar_BoolValues':    8
}

multiarray_types_api = {
    'PyArray_Type':                     1,
    'PyArrayDescr_Type':                2,
    'PyArrayFlags_Type':                3,
    'PyArrayIter_Type':                 4,
    'PyArrayMultiIter_Type':            5,
    'PyBoolArrType_Type':               7,
    'PyGenericArrType_Type':            9,
    'PyNumberArrType_Type':             10,
    'PyIntegerArrType_Type':            11,
    'PySignedIntegerArrType_Type':      12,
    'PyUnsignedIntegerArrType_Type':    13,
    'PyInexactArrType_Type':            14,
    'PyFloatingArrType_Type':           15,
    'PyComplexFloatingArrType_Type':    16,
    'PyFlexibleArrType_Type':           17,
    'PyCharacterArrType_Type':          18,
    'PyByteArrType_Type':               19,
    'PyShortArrType_Type':              20,
    'PyIntArrType_Type':                21,
    'PyLongArrType_Type':               22,
    'PyLongLongArrType_Type':           23,
    'PyUByteArrType_Type':              24,
    'PyUShortArrType_Type':             25,
    'PyUIntArrType_Type':               26,
    'PyULongArrType_Type':              27,
    'PyULongLongArrType_Type':          28,
    'PyFloatArrType_Type':              29,
    'PyDoubleArrType_Type':             30,
    'PyLongDoubleArrType_Type':         31,
    'PyCFloatArrType_Type':             32,
    'PyCDoubleArrType_Type':            33,
    'PyCLongDoubleArrType_Type':        34,
    'PyObjectArrType_Type':             35,
    'PyStringArrType_Type':             36,
    'PyUnicodeArrType_Type':            37,
    'PyVoidArrType_Type':               38,
    'PyTimeIntegerArrType_Type':        39,
    'PyDatetimeArrType_Type':           40,
    'PyTimedeltaArrType_Type':          41,
    'PyHalfArrType_Type':               221,
}

#define NPY_NUMUSERTYPES (*(int *)PyArray_API[6])
#define PyBoolArrType_Type (*(PyTypeObject *)PyArray_API[7])
#define _PyArrayScalar_BoolValues ((PyBoolScalarObject *)PyArray_API[8])

multiarray_funcs_api = {
    'PyArray_GetNDArrayCVersion':           0,
    'PyArray_SetNumericOps':                42,
    'PyArray_GetNumericOps':                43,
    'PyArray_INCREF':                       44,
    'PyArray_XDECREF':                      45,
    'PyArray_SetStringFunction':            46,
    'PyArray_DescrFromType':                47,
    'PyArray_TypeObjectFromType':           48,
    'PyArray_Zero':                         49,
    'PyArray_One':                          50,
    'PyArray_CastToType':                   51,
    'PyArray_CastTo':                       52,
    'PyArray_CastAnyTo':                    53,
    'PyArray_CanCastSafely':                54,
    'PyArray_CanCastTo':                    55,
    'PyArray_ObjectType':                   56,
    'PyArray_DescrFromObject':              57,
    'PyArray_ConvertToCommonType':          58,
    'PyArray_DescrFromScalar':              59,
    'PyArray_DescrFromTypeObject':          60,
    'PyArray_Size':                         61,
    'PyArray_Scalar':                       62,
    'PyArray_FromScalar':                   63,
    'PyArray_ScalarAsCtype':                64,
    'PyArray_CastScalarToCtype':            65,
    'PyArray_CastScalarDirect':             66,
    'PyArray_ScalarFromObject':             67,
    'PyArray_GetCastFunc':                  68,
    'PyArray_FromDims':                     69,
    'PyArray_FromDimsAndDataAndDescr':      70,
    'PyArray_FromAny':                      71,
    'PyArray_EnsureArray':                  72,
    'PyArray_EnsureAnyArray':               73,
    'PyArray_FromFile':                     74,
    'PyArray_FromString':                   75,
    'PyArray_FromBuffer':                   76,
    'PyArray_FromIter':                     77,
    'PyArray_Return':                       78,
    'PyArray_GetField':                     79,
    'PyArray_SetField':                     80,
    'PyArray_Byteswap':                     81,
    'PyArray_Resize':                       82,
    'PyArray_MoveInto':                     83,
    'PyArray_CopyInto':                     84,
    'PyArray_CopyAnyInto':                  85,
    'PyArray_CopyObject':                   86,
    'PyArray_NewCopy':                      87,
    'PyArray_ToList':                       88,
    'PyArray_ToString':                     89,
    'PyArray_ToFile':                       90,
    'PyArray_Dump':                         91,
    'PyArray_Dumps':                        92,
    'PyArray_ValidType':                    93,
    'PyArray_UpdateFlags':                  94,
    'PyArray_New':                          95,
    'PyArray_NewFromDescr':                 96,
    'PyArray_DescrNew':                     97,
    'PyArray_DescrNewFromType':             98,
    'PyArray_GetPriority':                  99,
    'PyArray_IterNew':                      100,
    'PyArray_MultiIterNew':                 101,
    'PyArray_PyIntAsInt':                   102,
    'PyArray_PyIntAsIntp':                  103,
    'PyArray_Broadcast':                    104,
    'PyArray_FillObjectArray':              105,
    'PyArray_FillWithScalar':               106,
    'PyArray_CheckStrides':                 107,
    'PyArray_DescrNewByteorder':            108,
    'PyArray_IterAllButAxis':               109,
    'PyArray_CheckFromAny':                 110,
    'PyArray_FromArray':                    111,
    'PyArray_FromInterface':                112,
    'PyArray_FromStructInterface':          113,
    'PyArray_FromArrayAttr':                114,
    'PyArray_ScalarKind':                   115,
    'PyArray_CanCoerceScalar':              116,
    'PyArray_NewFlagsObject':               117,
    'PyArray_CanCastScalar':                118,
    'PyArray_CompareUCS4':                  119,
    'PyArray_RemoveSmallest':               120,
    'PyArray_ElementStrides':               121,
    'PyArray_Item_INCREF':                  122,
    'PyArray_Item_XDECREF':                 123,
    'PyArray_FieldNames':                   124,
    'PyArray_Transpose':                    125,
    'PyArray_TakeFrom':                     126,
    'PyArray_PutTo':                        127,
    'PyArray_PutMask':                      128,
    'PyArray_Repeat':                       129,
    'PyArray_Choose':                       130,
    'PyArray_Sort':                         131,
    'PyArray_ArgSort':                      132,
    'PyArray_SearchSorted':                 133,
    'PyArray_ArgMax':                       134,
    'PyArray_ArgMin':                       135,
    'PyArray_Reshape':                      136,
    'PyArray_Newshape':                     137,
    'PyArray_Squeeze':                      138,
    'PyArray_View':                         139,
    'PyArray_SwapAxes':                     140,
    'PyArray_Max':                          141,
    'PyArray_Min':                          142,
    'PyArray_Ptp':                          143,
    'PyArray_Mean':                         144,
    'PyArray_Trace':                        145,
    'PyArray_Diagonal':                     146,
    'PyArray_Clip':                         147,
    'PyArray_Conjugate':                    148,
    'PyArray_Nonzero':                      149,
    'PyArray_Std':                          150,
    'PyArray_Sum':                          151,
    'PyArray_CumSum':                       152,
    'PyArray_Prod':                         153,
    'PyArray_CumProd':                      154,
    'PyArray_All':                          155,
    'PyArray_Any':                          156,
    'PyArray_Compress':                     157,
    'PyArray_Flatten':                      158,
    'PyArray_Ravel':                        159,
    'PyArray_MultiplyList':                 160,
    'PyArray_MultiplyIntList':              161,
    'PyArray_GetPtr':                       162,
    'PyArray_CompareLists':                 163,
    'PyArray_AsCArray':                     164,
    'PyArray_As1D':                         165,
    'PyArray_As2D':                         166,
    'PyArray_Free':                         167,
    'PyArray_Converter':                    168,
    'PyArray_IntpFromSequence':             169,
    'PyArray_Concatenate':                  170,
    'PyArray_InnerProduct':                 171,
    'PyArray_MatrixProduct':                172,
    'PyArray_CopyAndTranspose':             173,
    'PyArray_Correlate':                    174,
    'PyArray_TypestrConvert':               175,
    'PyArray_DescrConverter':               176,
    'PyArray_DescrConverter2':              177,
    'PyArray_IntpConverter':                178,
    'PyArray_BufferConverter':              179,
    'PyArray_AxisConverter':                180,
    'PyArray_BoolConverter':                181,
    'PyArray_ByteorderConverter':           182,
    'PyArray_OrderConverter':               183,
    'PyArray_EquivTypes':                   184,
    'PyArray_Zeros':                        185,
    'PyArray_Empty':                        186,
    'PyArray_Where':                        187,
    'PyArray_Arange':                       188,
    'PyArray_ArangeObj':                    189,
    'PyArray_SortkindConverter':            190,
    'PyArray_LexSort':                      191,
    'PyArray_Round':                        192,
    'PyArray_EquivTypenums':                193,
    'PyArray_RegisterDataType':             194,
    'PyArray_RegisterCastFunc':             195,
    'PyArray_RegisterCanCast':              196,
    'PyArray_InitArrFuncs':                 197,
    'PyArray_IntTupleFromIntp':             198,
    'PyArray_TypeNumFromName':              199,
    'PyArray_ClipmodeConverter':            200,
    'PyArray_OutputConverter':              201,
    'PyArray_BroadcastToShape':             202,
    '_PyArray_SigintHandler':               203,
    '_PyArray_GetSigintBuf':                204,
    'PyArray_DescrAlignConverter':          205,
    'PyArray_DescrAlignConverter2':         206,
    'PyArray_SearchsideConverter':          207,
    'PyArray_CheckAxis':                    208,
    'PyArray_OverflowMultiplyList':         209,
    'PyArray_CompareString':                210,
    'PyArray_MultiIterFromObjects':         211,
    'PyArray_GetEndianness':                212,
    'PyArray_GetNDArrayCFeatureVersion':    213,
    'PyArray_Correlate2':                   214,
    'PyArray_NeighborhoodIterNew':          215,
    'PyArray_SetDatetimeParseFunction':     216,
    'PyArray_DatetimeToDatetimeStruct':     217,
    'PyArray_TimedeltaToTimedeltaStruct':   218,
    'PyArray_DatetimeStructToDatetime':     219,
    'PyArray_TimedeltaStructToTimedelta':   220,
    'PyArray_MatrixProduct2':               221,
}

ufunc_types_api = {
    'PyUFunc_Type':                             0
}

ufunc_funcs_api = {
    'PyUFunc_FromFuncAndData':                  1,
    'PyUFunc_RegisterLoopForType':              2,
    'PyUFunc_GenericFunction':                  3,
    'PyUFunc_f_f_As_d_d':                       4,
    'PyUFunc_d_d':                              5,
    'PyUFunc_f_f':                              6,
    'PyUFunc_g_g':                              7,
    'PyUFunc_F_F_As_D_D':                       8,
    'PyUFunc_F_F':                              9,
    'PyUFunc_D_D':                              10,
    'PyUFunc_G_G':                              11,
    'PyUFunc_O_O':                              12,
    'PyUFunc_ff_f_As_dd_d':                     13,
    'PyUFunc_ff_f':                             14,
    'PyUFunc_dd_d':                             15,
    'PyUFunc_gg_g':                             16,
    'PyUFunc_FF_F_As_DD_D':                     17,
    'PyUFunc_DD_D':                             18,
    'PyUFunc_FF_F':                             19,
    'PyUFunc_GG_G':                             20,
    'PyUFunc_OO_O':                             21,
    'PyUFunc_O_O_method':                       22,
    'PyUFunc_OO_O_method':                      23,
    'PyUFunc_On_Om':                            24,
    'PyUFunc_GetPyValues':                      25,
    'PyUFunc_checkfperr':                       26,
    'PyUFunc_clearfperr':                       27,
    'PyUFunc_getfperr':                         28,
    'PyUFunc_handlefperr':                      29,
    'PyUFunc_ReplaceLoopBySignature':           30,
    'PyUFunc_FromFuncAndDataAndSignature':      31,
    'PyUFunc_SetUsesArraysAsData':              32,
    'PyUFunc_e_e':                              33,
    'PyUFunc_e_e_As_f_f':                       34,
    'PyUFunc_e_e_As_d_d':                       35,
    'PyUFunc_ee_e':                             36,
    'PyUFunc_ee_e_As_ff_f':                     37,
    'PyUFunc_ee_e_As_dd_d':                     38,
}

# List of all the dicts which define the C API
# XXX: DO NOT CHANGE THE ORDER OF TUPLES BELOW !
multiarray_api = (
        multiarray_global_vars,
        multiarray_global_vars_types,
        multiarray_scalar_bool_values,
        multiarray_types_api,
        multiarray_funcs_api,
)

ufunc_api = (
        ufunc_funcs_api,
        ufunc_types_api
)

full_api = multiarray_api + ufunc_api
