# MediaWiki:common.js

**Note:** After publishing, you may have to bypass your browser's cache to see the changes.   
  
  * **Firefox / Safari:** Hold _Shift_ while clicking _Reload_ , or press either _Ctrl-F5_ or _Ctrl-R_ (_⌘-R_ on a Mac)
  * **Google Chrome:** Press _Ctrl-Shift-R_ (_⌘-Shift-R_ on a Mac)
  * **Internet Explorer / Edge:** Hold _Ctrl_ while clicking _Refresh_ , or press _Ctrl-F5_
  * **Opera:** Press _Ctrl-F5_.


[code] 
    [](<#L-1>)/* Any JavaScript here will be loaded for all users on every page load. */
    [](<#L-2>)
    [](<#L-3>)function findGetParameter(parameterName) {
    [](<#L-4>)    var result = null,
    [](<#L-5>)        tmp = [];
    [](<#L-6>)    location.search
    [](<#L-7>)        .substr(1)
    [](<#L-8>)        .split("&")
    [](<#L-9>)        .forEach(function (item) {
    [](<#L-10>)          tmp = item.split("=");
    [](<#L-11>)          if (tmp[0] === parameterName) result = decodeURIComponent(tmp[1]);
    [](<#L-12>)        });
    [](<#L-13>)    return result;
    [](<#L-14>)}
    [](<#L-15>)
    [](<#L-16>)/* load TOC collapsed */
    [](<#L-17>)window.addEventListener('DOMContentLoaded', function() { try {
    [](<#L-18>)  if (document.getElementById('toc').getElementsByTagName('ul')[0].style.display != 'none') { toggleToc(); }
    [](<#L-19>)} catch (exception) {} }, false);
    [](<#L-20>)
    [](<#L-21>)/* custom toolbars */
    [](<#L-22>)var customizeToolbar = function () {
    [](<#L-23>)	$( '#wpTextbox1' ).wikiEditor( 'addToToolbar', {
    [](<#L-24>)		'section': 'main',
    [](<#L-25>)		'group': 'format',
    [](<#L-26>)		'tools': {
    [](<#L-27>)			"TDpythonbutton": {
    [](<#L-28>)				label: 'Python code',
    [](<#L-29>)				type: 'button',
    [](<#L-30>)				icon: 'https://docs.derivative.ca/images/b/bf/Pythonbutton.png',
    [](<#L-31>)				action: {
    [](<#L-32>)					type: 'encapsulate',
    [](<#L-33>)					options: {
    [](<#L-34>)						pre: "<syntaxhighlight lang=python>",
    [](<#L-35>)						post: "</syntaxhighlight>"
    [](<#L-36>)	  				}
    [](<#L-37>)	           }
    [](<#L-38>)			},
    [](<#L-39>)			"TDcodebutton": {
    [](<#L-40>)			label: 'Source code',
    [](<#L-41>)			type: 'button',
    [](<#L-42>)			icon: 'https://docs.derivative.ca/images/0/05/Codebutton.png',
    [](<#L-43>)				action: {
    [](<#L-44>)					type: 'encapsulate',
    [](<#L-45>)					options: {
    [](<#L-46>)						pre: "<code>",
    [](<#L-47>)						post: "</code>"
    [](<#L-48>)	  				}
    [](<#L-49>)	            }
    [](<#L-50>)			},
    [](<#L-51>)			"TDyoutubebutton": {
    [](<#L-52>)			label: 'Embed YouTube video',
    [](<#L-53>)			type: 'button',
    [](<#L-54>)			icon: 'https://docs.derivative.ca/images/a/af/Youtube.png',
    [](<#L-55>)			action: {
    [](<#L-56>)				type: 'encapsulate',
    [](<#L-57>)				options: {
    [](<#L-58>)					pre: "{{#widget:YouTube|id=|width=|height=}}",
    [](<#L-59>)					post: ""
    [](<#L-60>)				}
    [](<#L-61>)			}
    [](<#L-62>)			}
    [](<#L-63>)		}
    [](<#L-64>)	} );
    [](<#L-65>)	$( '#wpTextbox1' ).wikiEditor( 'addToToolbar', {
    [](<#L-66>)		'sections': {
    [](<#L-67>)			'templates': {
    [](<#L-68>)				'type': 'booklet', // Can also be 'booklet'
    [](<#L-69>)				'label': 'Templates',
    [](<#L-70>)				'pages':{
    [](<#L-71>)					'section-glossary': {
    [](<#L-72>)						'label': 'Glossary',
    [](<#L-73>)						'layout': 'characters',
    [](<#L-74>)						'characters':[
    [](<#L-75>)							{
    [](<#L-76>)								'action': {
    [](<#L-77>)									'type': 'encapsulate',
    [](<#L-78>)									'options': {
    [](<#L-79>)										'pre': '{{',
    [](<#L-80>)										'peri':'Glossary|Title=|Short=|Long=',
    [](<#L-81>)										'post':'}}'
    [](<#L-82>)									}
    [](<#L-83>)								},
    [](<#L-84>)								'label': 'Glossary Template'
    [](<#L-85>)							},
    [](<#L-86>)							{
    [](<#L-87>)								'action': {
    [](<#L-88>)									'type': 'encapsulate',
    [](<#L-89>)									'options': {
    [](<#L-90>)										'pre': '[[',
    [](<#L-91>)										'peri':'Category: Touch Glossary',
    [](<#L-92>)										'post':']]'
    [](<#L-93>)									}
    [](<#L-94>)								},
    [](<#L-95>)								'label': 'Glossary Category'
    [](<#L-96>)							}
    [](<#L-97>)						]
    [](<#L-98>)					},
    [](<#L-99>)					'section-operators': {
    [](<#L-100>)						'label': 'Operator Pages',
    [](<#L-101>)						'layout': 'characters',
    [](<#L-102>)						'characters':[
    [](<#L-103>)							{
    [](<#L-104>)								'action': {
    [](<#L-105>)									'type': 'encapsulate',
    [](<#L-106>)									'options': {
    [](<#L-107>)										'pre': '{{Summary',
    [](<#L-108>)										'peri':'|opFamily=|opLabel=|opType=|opClass=|opFilter=|opLicense=|opCategory=|os=|hardware=|short=|long=',
    [](<#L-109>)										'post':'}}'
    [](<#L-110>)									}
    [](<#L-111>)								},
    [](<#L-112>)								'label': 'Operator Summary'
    [](<#L-113>)							},
    [](<#L-114>)							{
    [](<#L-115>)								'action': {
    [](<#L-116>)									'type': 'encapsulate',
    [](<#L-117>)									'options': {
    [](<#L-118>)										'pre': '{{ParameterPage',
    [](<#L-119>)										'peri':'|opFamily=|pageName=|pageSummary=|items=',
    [](<#L-120>)										'post':'}}'
    [](<#L-121>)									}
    [](<#L-122>)								},
    [](<#L-123>)								'label': 'Parameter Page'
    [](<#L-124>)							},
    [](<#L-125>)							{
    [](<#L-126>)								'action': {
    [](<#L-127>)									'type': 'encapsulate',
    [](<#L-128>)									'options': {
    [](<#L-129>)										'pre': '{{ParameterSubPage',
    [](<#L-130>)										'peri':'|opFamily=|pageName=|pageSummary=|items=',
    [](<#L-131>)										'post':'}}'
    [](<#L-132>)									}
    [](<#L-133>)								},
    [](<#L-134>)								'label': 'Parameter Sub Page'
    [](<#L-135>)							},
    [](<#L-136>)							{
    [](<#L-137>)								'action': {
    [](<#L-138>)									'type': 'encapsulate',
    [](<#L-139>)									'options': {
    [](<#L-140>)										'pre': '{{OPSection',
    [](<#L-141>)										'peri':'|opFamily=|sectionName=|sectionSummary=|items=',
    [](<#L-142>)										'post':'}}'
    [](<#L-143>)									}
    [](<#L-144>)								},
    [](<#L-145>)								'label': 'Operator Section'
    [](<#L-146>)							},
    [](<#L-147>)							{
    [](<#L-148>)								'action': {
    [](<#L-149>)									'type': 'encapsulate',
    [](<#L-150>)									'options': {
    [](<#L-151>)										'pre': '{{OPSubSection',
    [](<#L-152>)										'peri':'|opFamily=|sectionName=|sectionSummary=',
    [](<#L-153>)										'post':'}}'
    [](<#L-154>)									}
    [](<#L-155>)								},
    [](<#L-156>)								'label': 'Operator Sub Section'
    [](<#L-157>)							},
    [](<#L-158>)							{
    [](<#L-159>)								'action': {
    [](<#L-160>)									'type': 'encapsulate',
    [](<#L-161>)									'options': {
    [](<#L-162>)										'pre': '{{InfoCHOPChannels',
    [](<#L-163>)										'peri':'|opFamily=|opLabel=|infoChannels=',
    [](<#L-164>)										'post':'}}'
    [](<#L-165>)									}
    [](<#L-166>)								},
    [](<#L-167>)								'label': 'Operator Info CHOP Section'
    [](<#L-168>)							},
    [](<#L-169>)							{
    [](<#L-170>)								'action': {
    [](<#L-171>)									'type': 'encapsulate',
    [](<#L-172>)									'options': {
    [](<#L-173>)										'pre': '{{InfoChannel',
    [](<#L-174>)										'peri':'|chanName=|chanSummary=',
    [](<#L-175>)										'post':'}}'
    [](<#L-176>)									}
    [](<#L-177>)								},
    [](<#L-178>)								'label': 'Info CHOP Channel'
    [](<#L-179>)							}
    [](<#L-180>)						]
    [](<#L-181>)					},
    [](<#L-182>)					'section-oppars': {
    [](<#L-183>)						'label': 'Operator Parameters',
    [](<#L-184>)						'layout': 'characters',
    [](<#L-185>)						'characters':[
    [](<#L-186>)							{
    [](<#L-187>)								'action': {
    [](<#L-188>)									'type': 'encapsulate',
    [](<#L-189>)									'options': {
    [](<#L-190>)										'pre': '{{Parameter',
    [](<#L-191>)										'peri':'|opFamily=|opType=|parName=|parLabel=|parDefault=|parType=|parReadOnly=|parOrder=|parSummary=|parItems=',
    [](<#L-192>)										'post':'}}'
    [](<#L-193>)									}
    [](<#L-194>)								},
    [](<#L-195>)								'label': 'Parameter'
    [](<#L-196>)							},
    [](<#L-197>)							{
    [](<#L-198>)								'action': {
    [](<#L-199>)									'type': 'encapsulate',
    [](<#L-200>)									'options': {
    [](<#L-201>)										'pre': '{{ParameterItem',
    [](<#L-202>)										'peri':'|opFamily=|parName=|itemName=|itemLabel=|itemDefault=|itemSummary=',
    [](<#L-203>)										'post':'}}'
    [](<#L-204>)									}
    [](<#L-205>)								},
    [](<#L-206>)								'label': 'Parameter Item'
    [](<#L-207>)							}
    [](<#L-208>)						]
    [](<#L-209>)					},
    [](<#L-210>)					'section-class': {
    [](<#L-211>)						'label': 'Python Classes',
    [](<#L-212>)						'layout': 'characters',
    [](<#L-213>)						'characters':[
    [](<#L-214>)							{
    [](<#L-215>)								'action': {
    [](<#L-216>)									'type': 'encapsulate',
    [](<#L-217>)									'options': {
    [](<#L-218>)										'pre': '{{',
    [](<#L-219>)										'peri':'OPClassSummary|OPfamily=|OPtype=|OPlabel=',
    [](<#L-220>)										'post':'}}'
    [](<#L-221>)									}
    [](<#L-222>)								},
    [](<#L-223>)								'label': 'OPClassSummary'
    [](<#L-224>)							},
    [](<#L-225>)							{
    [](<#L-226>)								'action': {
    [](<#L-227>)									'type': 'encapsulate',
    [](<#L-228>)									'options': {
    [](<#L-229>)										'pre': '{{',
    [](<#L-230>)										'peri':'TDClassSummary|label=|summary=',
    [](<#L-231>)										'post':'}}'
    [](<#L-232>)									}
    [](<#L-233>)								},
    [](<#L-234>)								'label': 'TDClassSummary'
    [](<#L-235>)							},
    [](<#L-236>)							{
    [](<#L-237>)								'action': {
    [](<#L-238>)									'type': 'encapsulate',
    [](<#L-239>)									'options': {
    [](<#L-240>)										'pre': '{{',
    [](<#L-241>)										'peri':'ClassMemberSection|Sectionsummary=|items=|empty=',
    [](<#L-242>)										'post':'}}'
    [](<#L-243>)									}
    [](<#L-244>)								},
    [](<#L-245>)								'label': 'ClassMemberSection'
    [](<#L-246>)							},
    [](<#L-247>)							{
    [](<#L-248>)								'action': {
    [](<#L-249>)									'type': 'encapsulate',
    [](<#L-250>)									'options': {
    [](<#L-251>)										'pre': '{{',
    [](<#L-252>)										'peri':'ClassMember|class=|name=|type=|set=|text=|deprecated=',
    [](<#L-253>)										'post':'}}'
    [](<#L-254>)									}
    [](<#L-255>)								},
    [](<#L-256>)								'label': 'ClassMember'
    [](<#L-257>)							},
    [](<#L-258>)							{
    [](<#L-259>)								'action': {
    [](<#L-260>)									'type': 'encapsulate',
    [](<#L-261>)									'options': {
    [](<#L-262>)										'pre': '{{',
    [](<#L-263>)										'peri':'ClassMethodSection|SectionSummary=|items=|empty=',
    [](<#L-264>)										'post':'}}'
    [](<#L-265>)									}
    [](<#L-266>)								},
    [](<#L-267>)								'label': 'ClassMethodSection'
    [](<#L-268>)							},
    [](<#L-269>)							{
    [](<#L-270>)								'action': {
    [](<#L-271>)									'type': 'encapsulate',
    [](<#L-272>)									'options': {
    [](<#L-273>)										'pre': '{{',
    [](<#L-274>)										'peri':'ClassMethod|class=|name=|call=|returns=|text=|deprecated=',
    [](<#L-275>)										'post':'}}'
    [](<#L-276>)									}
    [](<#L-277>)								},
    [](<#L-278>)								'label': 'ClassMethod'
    [](<#L-279>)							},
    [](<#L-280>)							{
    [](<#L-281>)								'action': {
    [](<#L-282>)									'type': 'encapsulate',
    [](<#L-283>)									'options': {
    [](<#L-284>)										'pre': '{{SubSection|title=|text=}}'
    [](<#L-285>)									}
    [](<#L-286>)								},
    [](<#L-287>)								'label': 'Class SubSection'
    [](<#L-288>)							},
    [](<#L-289>)						]
    [](<#L-290>)					},
    [](<#L-291>)					'section-page': {
    [](<#L-292>)						'label': 'General Page Elements',
    [](<#L-293>)						'layout': 'characters',
    [](<#L-294>)						'characters':[
    [](<#L-295>)							{
    [](<#L-296>)								'action': {
    [](<#L-297>)									'type': 'encapsulate',
    [](<#L-298>)									'options': {
    [](<#L-299>)										'pre': '{{History}}'
    [](<#L-300>)									}
    [](<#L-301>)								},
    [](<#L-302>)								'label': 'Tag History'
    [](<#L-303>)							},
    [](<#L-304>)							{
    [](<#L-305>)								'action': {
    [](<#L-306>)									'type': 'encapsulate',
    [](<#L-307>)									'options': {
    [](<#L-308>)										'pre': '{{SOPNavBox|opFamily=SOP}}'
    [](<#L-309>)									}
    [](<#L-310>)								},
    [](<#L-311>)								'label': 'Category Navigation Box'
    [](<#L-312>)							},
    [](<#L-313>)							{
    [](<#L-314>)								'action': {
    [](<#L-315>)									'type': 'encapsulate',
    [](<#L-316>)									'options': {
    [](<#L-317>)										'pre': '{{#invoke:Category|list|COMPs}}'
    [](<#L-318>)									}
    [](<#L-319>)								},
    [](<#L-320>)								'label': 'Category List'
    [](<#L-321>)							},
    [](<#L-322>)							{
    [](<#L-323>)								'action': {
    [](<#L-324>)									'type': 'encapsulate',
    [](<#L-325>)									'options': {
    [](<#L-326>)										'pre': '{{lowercase}}'
    [](<#L-327>)									}
    [](<#L-328>)								},
    [](<#L-329>)								'label': 'Force pagetitle to lowercase'
    [](<#L-330>)							},
    [](<#L-331>)							{
    [](<#L-332>)								'action': {
    [](<#L-333>)									'type': 'encapsulate',
    [](<#L-334>)									'options': {
    [](<#L-335>)										'pre': '#REDIRECT [[:Experimental:{{FULLPAGENAME}}]]'
    [](<#L-336>)									}
    [](<#L-337>)								},
    [](<#L-338>)								'label': 'Redirect to Experimental'
    [](<#L-339>)							}
    [](<#L-340>)						]
    [](<#L-341>)					},
    [](<#L-342>)				}
    [](<#L-343>)			}
    [](<#L-344>)		}
    [](<#L-345>)	} );
    [](<#L-346>)};
    [](<#L-347>)
    [](<#L-348>)
    [](<#L-349>)/* Check if view is in edit mode and that the required modules are available. Then, customize the toolbar … */
    [](<#L-350>)if ( [ 'edit', 'submit' ].indexOf( mw.config.get( 'wgAction' ) ) !== -1 ) {
    [](<#L-351>)	mw.loader.using( 'user.options' ).then( function () {
    [](<#L-352>)		// This can be the string "0" if the user disabled the preference ([[phab:T54542#555387]])
    [](<#L-353>)		if ( mw.user.options.get( 'usebetatoolbar' ) == 1 ) {
    [](<#L-354>)			$.when(
    [](<#L-355>)				mw.loader.using( 'ext.wikiEditor' ), $.ready
    [](<#L-356>)			).then( customizeToolbar );
    [](<#L-357>)		}
    [](<#L-358>)	} );
    [](<#L-359>)}
    [](<#L-360>)
    [](<#L-361>)// Redirect anonymous users to login form.
    [](<#L-362>)/*
    [](<#L-363>)jQuery(document).ready(function() {
    [](<#L-364>)  if (jQuery('#pt-anon_oauth_login').length) {
    [](<#L-365>)   var titleUrl = findGetParameter('title');
    [](<#L-366>)   if (titleUrl) {
    [](<#L-367>)     var returnUrl = '/index.php?title=Special:OAuth2Client/redirect&returnto=' + titleUrl;
    [](<#L-368>)   }
    [](<#L-369>)   else {
    [](<#L-370>)     var returnUrl = '/index.php?title=Special:OAuth2Client/redirect&returnto=Main+Page';
    [](<#L-371>)   }
    [](<#L-372>)   window.location.href = returnUrl;
    [](<#L-373>)  }
    [](<#L-374>)});
    [](<#L-375>)*/
    
[/code]
