from dataclasses import dataclass
from typing import Any
class CuryCueStructsDef:
    @dataclass
    class ACTIVE_FIELDS:
        id_par: int=0
        id_fixture:int=0
        id_par_cue:int=0
        fixture_name:str=''
        fixture_object_location:str=''
        par_name: str = ''
        full_par_path:str = ''
        par_value: float = 0
        par_text_value: str=''
        fade_in: float = 0
        delay_in: float = 0
        is_fixture_enabled:bool=True
        is_par_enabled:bool=True
        is_cue_exist:int=0
        is_fading:int=0
        extra_export_frames:int=0
        fixture_ref: Any=None
        fixture_par_ref: Any=None
        is_key: bool = False
        is_derived: bool = False
    @dataclass
    class FIXTURE:
        id: int = 0
        order: float = 0
        name: str = ''
        global_object_location: str = ""
        original_location: str=""
        type: str = ""
        is_enabled: bool = True
        is_selected: bool = False
        pars: Any = list
        pars_float_by_name: Any = dict
    @dataclass
    class FIXPAR:
        id: int = 0
        name: str = ""
        par_name: str = ""
        default_value: float =0 
        fade_default:float = 1
        delay_default:float = 1
        global_object_location: str = ""
        is_enabled:bool=True
        id_fixture: int = 0
    @dataclass
    class CUE:
        id: int = 0
        order: float = 0
        cue_name: str = ''
        memo: str = ''
        type: str = ''
        update_mode: int = 0
        osc_bind: str = ""
        dmx_bind: int = 0
        is_enabled: bool = True
        linked: int = 0
        frame_bind: int = 0
        pars_float: Any = list
        pars_float_by_path=dict
        pars_float_by_fix_id=dict
        
    @dataclass
    class CUEPARFLOAT:
        id: int = 0
        id_fixture: int = 0
        fixture_name: str =''
        fixture_object_location:str=''
        full_par_path:str = ''
        par_name: str = ''
        par_value: float = 0
        par_text_value: str = ''
        fade_in: float = 0
        fade_out: float = 0
        delay_in: float = 0
        delay_out: float = 0
        fixture: Any = None
        fixture_par_ref: Any = None
        is_derived: bool = False
    @dataclass
    class FRAMEBINDRANGE:
        triggerConditionRange:  Any = list
        triggerRange:  Any = list