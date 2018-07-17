__all__ = ['runchar']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['magicGet', 'selStat', 'run'])
@Js
def PyJsHoisted_magicGet_(lista, possibile, this, arguments, var=var):
    var = Scope({'lista':lista, 'arguments':arguments, 'possibile':possibile, 'this':this}, var)
    var.registers(['ret', 'lista', 'possibile'])
    var.put('ret', Js([]))
    var.get('ret').put('value', var.get('possibile').get(var.get('lista')))
    var.get('ret').put('style', Js([]))
    var.get('ret').get('style').put('display', var.get(u"null"))
    return var.get('ret')
PyJsHoisted_magicGet_.func_name = 'magicGet'
var.put('magicGet', PyJsHoisted_magicGet_)
@Js
def PyJsHoisted_selStat_(level, stat, possibile, this, arguments, var=var):
    var = Scope({'stat':stat, 'level':level, 'arguments':arguments, 'possibile':possibile, 'this':this}, var)
    var.registers(['stat', 'level', 'possibile'])
    var.get('possibile').put(var.get('stat'), var.get('level'))
    return var.get('possibile')
PyJsHoisted_selStat_.func_name = 'selStat'
var.put('selStat', PyJsHoisted_selStat_)
@Js
def PyJsHoisted_run_(level, gender, this, arguments, var=var):
    var = Scope({'gender':gender, 'level':level, 'arguments':arguments, 'this':this}, var)
    var.registers(['whichMagic', 'wa3', 'ringStone', 'tempAr', 'sp3', 'warriorArmor', 'elfWeapon', 'so3', 'dwarfWeapon', 'magicRare', 'pickManeuvers', 'ba4', 'baCantrip', 'ba3', 'yy', 'initiative', 'patronSpells5', 'wpDam', 'skills', 'languageOutput', 'forceGender', 'wi5', 'scrollBardVery', 'modNum', 'wiz4', 'waTomeRituals', 'enemies', 'weOutput', 'lowest', 'abOutput', 'hasArmor', 'ra3', 'y', 'arOutput', 'scrollWizaVery', 'ci0', 'output', 'ci5', 'clDomain', 'ss4', 'upgrade', 'forceDomain', 'companionsAttack2', 'scrollDruiUnc', 'dr2', 'z', 'scrollClerUnc', 'forceSchool', 'abilNames', 'forceLvl', 'pa3', 'scrollWarlVery', 'companionsAttackText2', 'toOutput', 'forceWarl', 'sp5', 'patronSpells4', 'wiz3', 'scrollWarlUnc', 'sp', 'magicArmor', 'burglar', 'wi1', 'ba1', 'hpgain', 'magicArrowType', 'ci4', 'clCantrip', 'wiCantrip', 'dr4', 'forcePala', 'companionsStats', 'forceBard', 'skOutput', 'hp', 'drCantrip', 'gold', 'x', 'schools', 'whichMagicArmor', 'loSpells', 'tomeRituals', 'scrollWizaRare', 'ra1', 'cl5', 'forceRogu', 'forceMonk', 'humanoids', 'prof', 'ba2', 'companionsDamageExtra', 'level', 'abil', 'raceSpellAbility', 'ci3', 'valuables', 'showPlus', 'forceFigh', 'companionsAttackDamage2', 'wiSchool', 'ci1', 'companionsAttack1', 'magicArrowDisplay', 'dragType', 'factions', 'forceRang', 'companionshp', 'dwarfMagicArmor', 'newLang', 'magicVeryRare', 'oaSpells', 'magicArrowPlus', 'jewelryAdjectives', 'elfBow', 'wa2', 'exotic', 'ra2', 'tempSpells', 'soOrigin', 'wpNum', 'so2', 'patronSpells2', 'companionsDamage1', 'tome', 'magicWeapon', 'wiz4Prepared', 'sum', 'dr5', 'land', 'music', 'humLangs', 'mySkills', 'wiz5', 'detailedStats', 'wa5', 'scrollClerRare', 'poOutput', 'scrollWarlRare', 'cOutput', 'doSpells', 'scrollPalaRare', 'speed', 'cl2', 'ac', 'scrollBardUnc', 'skLearn', 'myWp', 'scrollRangVery', 'platinum', 'showAbil', 'al', 'sp2', 'flaw', 'abilIncrease', 'spOutput', 'bg', 'jewelry', 'bootsOfSS', 'familiars', 'ss2', 'ci2', 'ringResistance', 'weapons', 'companionsAC', 'upgradeRare', 'dr1', 'wpRange', 'forceSorc', 'waTome', 'bond', 'lifestyles', 'dr3', 'ciSpells', 'wpType', 'wi4', 'size', 'fiStyle', 'ba5', 'pa2', 'wa1', 'eqOutput', 'drCircle', 'ideal', 'bgOutput', 'jewelryAdjectivesRare', 'rangedWeapons', 'ss5', 'q', 'firstIncrease', 'waSpells', 'maneuvers', 'wiz2Prepared', 'companionsDamageBonus2', 'maOutput', 'wpOutput', 'myMusic', 'myCantrips', 'pickWeap', 'scrollRangUnc', 'scrollClerVery', 'wiz3Prepared', 'wrOutput', 'genAbil', 'abilRaw', 'forceBarb', 'wa4', 'count', 'soCantrip', 'scrollRangRare', 'ss3', 'scrollPalaVery', 'bool', 'sp1', 'dragon', 'forceAbil', 'moreLang', 'forceCl', 'tempTxt', 'upgradeVeryRare', 'mod', 'hd', 'waPatron', 'ci6', 'golddebug', 'pickMeta', 'scrollDruiVery', 'eldritch', 'xx', 'cl1', 'so4', 'wi2', 'hasShield', 'enLangs', 'st', 'jewelryRare', 'saves', 'scrollDruiRare', 'companionsDamageBonus', 'wpDistance', 'magicUncommon', 'raceSpells', 'ss1', 'sp4', 'pickSome', 'bgText', 'myInstrument', 'forceCircle', 'forceWarlPact', 'patronSpells1', 'so1', 'armors', 'armorAC', 'so5', 'myAr', 'companions', 'meta', 'scrollBardRare', 'wiz1', 'myLifestyle', 'pa1', 'wi3', 'digits', 'wiz2', 'temp', 'ci7', 'patronSpells3', 'waCantrip', 'elemType', 'i', 'pickEldritch', 'scrollPalaUnc', 'wiz1Prepared', 'ringProtection', 'rollOutput', 'fiStyle2', 'personality', 'wiz5Prepared', 'cl3', 'cl4', 'res', 'forceRace', 'scrollWizaUnc', 'expertise', 'gaming', 'mySpells', 'skAbil', 'artisans', 'upgradeUncommon', 'magicArrows', 'ki', 'GRECHINA', 'forceBg', 'gender', 'myFaction', 'spellAbility'])
    @Js
    def PyJsHoisted_dwarfWeapon_(this, arguments, var=var):
        var = Scope({'arguments':arguments, 'this':this}, var)
        var.registers([])
        if ((var.get('racetxt')==Js('Hill Dwarf')) or (var.get('racetxt')==Js('Mountain Dwarf'))):
            if ((var.get('Math').callprop('random')>Js(0.5)) and (var.get('cl')!=Js(3.0))):
                var.get('myWp').callprop('push', var.get('weapons').get('11'))
            else:
                var.get('myWp').callprop('push', var.get('weapons').get('19'))
            return Js(True)
        else:
            return Js(False)
    PyJsHoisted_dwarfWeapon_.func_name = 'dwarfWeapon'
    var.put('dwarfWeapon', PyJsHoisted_dwarfWeapon_)
    @Js
    def PyJsHoisted_warriorArmor_(this, arguments, var=var):
        var = Scope({'arguments':arguments, 'this':this}, var)
        var.registers([])
        if (var.get('mod').get('1')>Js(3.0)):
            if ((var.get('upgrade')()==Js(True)) and (var.get('level')>Js(1.0))):
                var.get('myAr').callprop('push', var.get('armors').get('3'))
            else:
                var.get('myAr').callprop('push', var.get('armors').get('2'))
        else:
            if (((var.get('mod').get('1')>Js(0.0)) and (var.get('level')>Js(1.0))) and (var.get('upgrade')()==Js(True))):
                if (var.get('upgrade')()==Js(True)):
                    if (var.get('upgrade')()==Js(True)):
                        var.get('myAr').callprop('push', var.get('armors').get('8'))
                    else:
                        var.get('myAr').callprop('push', var.get('armors').get('7'))
                else:
                    var.get('myAr').callprop('push', var.get('armors').get('6'))
            else:
                if (((var.get('upgradeUncommon')()==Js(True)) and (var.get('abil').get('0')>Js(14.0))) and (var.get('level')>Js(1.0))):
                    if (var.get('upgradeUncommon')()==Js(True)):
                        var.get('myAr').callprop('push', var.get('armors').get('12'))
                    else:
                        var.get('myAr').callprop('push', var.get('armors').get('11'))
                else:
                    if (var.get('abil').get('0')>Js(12.0)):
                        var.get('myAr').callprop('push', var.get('armors').get('10'))
                    else:
                        var.get('myAr').callprop('push', var.get('armors').get('9'))
    PyJsHoisted_warriorArmor_.func_name = 'warriorArmor'
    var.put('warriorArmor', PyJsHoisted_warriorArmor_)
    @Js
    def PyJsHoisted_elfWeapon_(this, arguments, var=var):
        var = Scope({'arguments':arguments, 'this':this}, var)
        var.registers([])
        if ((var.get('racetxt')==Js('High Elf')) or (var.get('racetxt')==Js('Wood Elf'))):
            if (var.get('mod').get('1')>var.get('mod').get('0')):
                var.get('myWp').callprop('push', var.get('weapons').get('18'))
            else:
                var.get('myWp').callprop('push', var.get('weapons').get('14'))
            return Js(True)
        else:
            if (var.get('racetxt')==Js('Drow Elf')):
                if (var.get('mod').get('1')>var.get('mod').get('0')):
                    var.get('myWp').callprop('push', var.get('weapons').get('16'))
                    return Js(True)
                else:
                    return Js(False)
            else:
                return Js(False)
    PyJsHoisted_elfWeapon_.func_name = 'elfWeapon'
    var.put('elfWeapon', PyJsHoisted_elfWeapon_)
    @Js
    def PyJsHoisted_dragon_(this, arguments, var=var):
        var = Scope({'arguments':arguments, 'this':this}, var)
        var.registers([])
        var.put('x', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(10.0))))
        while 1:
            SWITCHED = False
            CONDITION = (var.get('x'))
            if SWITCHED or PyJsStrictEq(CONDITION, Js(0.0)):
                SWITCHED = True
                var.put('tempAr', Js([Js('Black'), Js('Acid'), Js('5 x 30 ft. line')]))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
                SWITCHED = True
                var.put('tempAr', Js([Js('Blue'), Js('Lightning'), Js('5 x 30 ft. line')]))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                SWITCHED = True
                var.put('tempAr', Js([Js('Brass'), Js('Fire'), Js('5 x 30 ft. line')]))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js(3.0)):
                SWITCHED = True
                var.put('tempAr', Js([Js('Bronze'), Js('Lightning'), Js('5 x 30 ft. line')]))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js(4.0)):
                SWITCHED = True
                var.put('tempAr', Js([Js('Copper'), Js('Acid'), Js('5 x 30 ft. line')]))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js(5.0)):
                SWITCHED = True
                var.put('tempAr', Js([Js('Gold'), Js('Fire'), Js('15 ft. cone')]))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js(6.0)):
                SWITCHED = True
                var.put('tempAr', Js([Js('Green'), Js('Poison'), Js('15 ft. cone')]))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js(7.0)):
                SWITCHED = True
                var.put('tempAr', Js([Js('Red'), Js('Fire'), Js('15 ft. cone')]))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js(8.0)):
                SWITCHED = True
                var.put('tempAr', Js([Js('Silver'), Js('Cold'), Js('15 ft. cone')]))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js(9.0)):
                SWITCHED = True
                var.put('tempAr', Js([Js('White'), Js('Cold'), Js('15 ft. cone')]))
                break
            SWITCHED = True
            break
        return var.get('tempAr')
    PyJsHoisted_dragon_.func_name = 'dragon'
    var.put('dragon', PyJsHoisted_dragon_)
    @Js
    def PyJsHoisted_pickEldritch_(this, arguments, var=var):
        var = Scope({'arguments':arguments, 'this':this}, var)
        var.registers(['answers'])
        var.put('answers', Js([]))
        var.put('y', Js(2.0))
        if (var.get('level')>Js(4.0)):
            var.put('y', Js(3.0))
        if (var.get('level')>Js(6.0)):
            var.put('y', Js(4.0))
        if (var.get('level')>Js(8.0)):
            var.put('y', Js(5.0))
        if (var.get('level')>Js(4.0)):
            var.get('eldritch').callprop('push', Js('One with Shadows'))
            var.get('eldritch').callprop('push', Js('Sign of Ill Omen'))
            var.get('eldritch').callprop('push', Js('Mire the Mind'))
        if (var.get('level')>Js(6.0)):
            var.get('eldritch').callprop('push', Js('Sculptor of Flesh'))
            var.get('eldritch').callprop('push', Js('Bewitching Whispers'))
            var.get('eldritch').callprop('push', Js('Dreadful Word'))
            var.get('eldritch').callprop('push', Js('Sculptor of Flesh'))
        if (var.get('level')>Js(8.0)):
            var.get('eldritch').callprop('push', Js('Ascendant Flesh'))
            var.get('eldritch').callprop('push', Js('Minions of Chaos'))
            var.get('eldritch').callprop('push', Js('Otherworldly Leap'))
            var.get('eldritch').callprop('push', Js('Whispers of the Grave'))
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<var.get('y')):
            var.put('x', var.get('eldritch').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('eldritch').get('length')))))
            if (((var.get('level')>Js(4.0)) and (var.get('tempTxt').callprop('indexOf', Js('Pact of the Blade'))>(-Js(1.0)))) and (var.get('Math').callprop('random')>Js(0.67))):
                var.put('x', Js('Thirsting Blade'))
            if ((var.get('tempTxt').callprop('indexOf', Js('Pact of the Chain'))>(-Js(1.0))) and (var.get('Math').callprop('random')>Js(0.67))):
                var.put('x', Js('Voice of the Chain Master'))
            if ((var.get('tempTxt').callprop('indexOf', Js('Pact of the Tome'))>(-Js(1.0))) and (var.get('Math').callprop('random')>Js(0.67))):
                var.put('x', Js('Book of Ancient Secrets'))
            if (var.get('answers').callprop('indexOf', var.get('x'))==(-Js(1.0))):
                var.get('answers').callprop('push', var.get('x'))
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
        
        var.get('answers').callprop('sort')
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<var.get('answers').get('length')):
            try:
                if (var.get('i')==Js(0.0)):
                    var.put('abOutput', (Js('(')+var.get('answers').get(var.get('i'))), '+')
                else:
                    var.put('abOutput', (Js(', ')+var.get('answers').get(var.get('i'))), '+')
            finally:
                    (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
        var.put('abOutput', Js(')'), '+')
        return var.get('answers')
    PyJsHoisted_pickEldritch_.func_name = 'pickEldritch'
    var.put('pickEldritch', PyJsHoisted_pickEldritch_)
    @Js
    def PyJsHoisted_elfBow_(this, arguments, var=var):
        var = Scope({'arguments':arguments, 'this':this}, var)
        var.registers([])
        if (((var.get('racetxt')==Js('High Elf')) or (var.get('racetxt')==Js('Wood Elf'))) and (var.get('level')>Js(1.0))):
            var.get('myWp').callprop('push', var.get('weapons').get('9'))
            return Js(True)
        else:
            return Js(False)
    PyJsHoisted_elfBow_.func_name = 'elfBow'
    var.put('elfBow', PyJsHoisted_elfBow_)
    @Js
    def PyJsHoisted_upgradeRare_(this, arguments, var=var):
        var = Scope({'arguments':arguments, 'this':this}, var)
        var.registers([])
        var.put('x', (((var.get('level')*var.get('level'))/Js(2.0))*Js(0.01)))
        if (var.get('level')==Js(1.0)):
            var.put('x', Js(0.0))
        if (var.get('Math').callprop('random')<var.get('x')):
            return Js(True)
        else:
            return Js(False)
    PyJsHoisted_upgradeRare_.func_name = 'upgradeRare'
    var.put('upgradeRare', PyJsHoisted_upgradeRare_)
    @Js
    def PyJsHoisted_pickManeuvers_(z, this, arguments, var=var):
        var = Scope({'z':z, 'arguments':arguments, 'this':this}, var)
        var.registers(['z', 'answers'])
        var.put('answers', Js([]))
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<var.get('z')):
            var.put('x', var.get('maneuvers').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('maneuvers').get('length')))))
            if (var.get('answers').callprop('indexOf', var.get('x'))>(-Js(1.0))):
                pass
            else:
                var.get('answers').callprop('push', var.get('x'))
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
        
        var.get('answers').callprop('sort')
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<var.get('answers').get('length')):
            try:
                if (var.get('i')==Js(0.0)):
                    var.put('abOutput', (Js('(')+var.get('answers').get(var.get('i'))), '+')
                else:
                    var.put('abOutput', (Js(', ')+var.get('answers').get(var.get('i'))), '+')
            finally:
                    (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
        var.put('abOutput', Js(')'), '+')
    PyJsHoisted_pickManeuvers_.func_name = 'pickManeuvers'
    var.put('pickManeuvers', PyJsHoisted_pickManeuvers_)
    @Js
    def PyJsHoisted_upgradeVeryRare_(this, arguments, var=var):
        var = Scope({'arguments':arguments, 'this':this}, var)
        var.registers([])
        var.put('x', (((var.get('level')*var.get('level'))/Js(4.0))*Js(0.01)))
        if (var.get('level')<Js(5.0)):
            var.put('x', Js(0.0))
        if (var.get('Math').callprop('random')<var.get('x')):
            return Js(True)
        else:
            return Js(False)
    PyJsHoisted_upgradeVeryRare_.func_name = 'upgradeVeryRare'
    var.put('upgradeVeryRare', PyJsHoisted_upgradeVeryRare_)
    @Js
    def PyJsHoisted_pickWeap_(z, this, arguments, var=var):
        var = Scope({'z':z, 'arguments':arguments, 'this':this}, var)
        var.registers(['z'])
        var.put('x', var.get('z').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('z').get('length')))))
        return var.get('x')
    PyJsHoisted_pickWeap_.func_name = 'pickWeap'
    var.put('pickWeap', PyJsHoisted_pickWeap_)
    @Js
    def PyJsHoisted_digits_(x, this, arguments, var=var):
        var = Scope({'x':x, 'arguments':arguments, 'this':this}, var)
        var.registers(['x'])
        if (var.get('x')<Js(10.0)):
            return (Js(' ')+var.get('x'))
        else:
            return var.get('x')
    PyJsHoisted_digits_.func_name = 'digits'
    var.put('digits', PyJsHoisted_digits_)
    @Js
    def PyJsHoisted_upgrade_(this, arguments, var=var):
        var = Scope({'arguments':arguments, 'this':this}, var)
        var.registers([])
        var.put('x', (Js(0.3)+((var.get('level')-Js(2.0))*Js(0.2))))
        if (var.get('level')==Js(1.0)):
            var.put('x', Js(0.0))
        if (var.get('Math').callprop('random')<var.get('x')):
            return Js(True)
        else:
            return Js(False)
    PyJsHoisted_upgrade_.func_name = 'upgrade'
    var.put('upgrade', PyJsHoisted_upgrade_)
    @Js
    def PyJsHoisted_modNum_(x, this, arguments, var=var):
        var = Scope({'x':x, 'arguments':arguments, 'this':this}, var)
        var.registers(['x'])
        while 1:
            SWITCHED = False
            CONDITION = (var.get('x'))
            if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
                SWITCHED = True
                return (-Js(5.0))
            if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                SWITCHED = True
                return (-Js(4.0))
            if SWITCHED or PyJsStrictEq(CONDITION, Js(3.0)):
                SWITCHED = True
                return (-Js(4.0))
            if SWITCHED or PyJsStrictEq(CONDITION, Js(4.0)):
                SWITCHED = True
                return (-Js(3.0))
            if SWITCHED or PyJsStrictEq(CONDITION, Js(5.0)):
                SWITCHED = True
                return (-Js(3.0))
            if SWITCHED or PyJsStrictEq(CONDITION, Js(6.0)):
                SWITCHED = True
                return (-Js(2.0))
            if SWITCHED or PyJsStrictEq(CONDITION, Js(7.0)):
                SWITCHED = True
                return (-Js(2.0))
            if SWITCHED or PyJsStrictEq(CONDITION, Js(8.0)):
                SWITCHED = True
                return (-Js(1.0))
            if SWITCHED or PyJsStrictEq(CONDITION, Js(9.0)):
                SWITCHED = True
                return (-Js(1.0))
            if SWITCHED or PyJsStrictEq(CONDITION, Js(10.0)):
                SWITCHED = True
                return Js(0.0)
            if SWITCHED or PyJsStrictEq(CONDITION, Js(11.0)):
                SWITCHED = True
                return Js(0.0)
            if SWITCHED or PyJsStrictEq(CONDITION, Js(12.0)):
                SWITCHED = True
                return Js(1.0)
            if SWITCHED or PyJsStrictEq(CONDITION, Js(13.0)):
                SWITCHED = True
                return Js(1.0)
            if SWITCHED or PyJsStrictEq(CONDITION, Js(14.0)):
                SWITCHED = True
                return Js(2.0)
            if SWITCHED or PyJsStrictEq(CONDITION, Js(15.0)):
                SWITCHED = True
                return Js(2.0)
            if SWITCHED or PyJsStrictEq(CONDITION, Js(16.0)):
                SWITCHED = True
                return Js(3.0)
            if SWITCHED or PyJsStrictEq(CONDITION, Js(17.0)):
                SWITCHED = True
                return Js(3.0)
            if SWITCHED or PyJsStrictEq(CONDITION, Js(18.0)):
                SWITCHED = True
                return Js(4.0)
            if SWITCHED or PyJsStrictEq(CONDITION, Js(19.0)):
                SWITCHED = True
                return Js(4.0)
            if SWITCHED or PyJsStrictEq(CONDITION, Js(20.0)):
                SWITCHED = True
                return Js(5.0)
            SWITCHED = True
            break
    PyJsHoisted_modNum_.func_name = 'modNum'
    var.put('modNum', PyJsHoisted_modNum_)
    @Js
    def PyJsHoisted_pickSome_(z, this, arguments, var=var):
        var = Scope({'z':z, 'arguments':arguments, 'this':this}, var)
        var.registers(['z'])
        var.put('bool', Js(False))
        var.put('i', Js(0.0))
        while (var.get('bool')==Js(False)):
            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            var.put('y', var.get('z').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('z').get('length')))))
            if (var.get('i')>Js(500.0)):
                var.put('z', Js([Js(0.0), Js(1.0), Js(2.0), Js(3.0), Js(4.0), Js(5.0), Js(6.0), Js(7.0), Js(8.0), Js(9.0), Js(10.0), Js(11.0), Js(12.0), Js(13.0), Js(14.0), Js(15.0), Js(16.0), Js(17.0)]))
                var.get('console').callprop('log', Js('500 tries already.  Allowing any skills.'))
            if (var.get('skLearn').get(var.get('y'))!=Js(True)):
                var.get('skLearn').put(var.get('y'), Js(True))
                var.put('bool', Js(True))
                return var.get('y')
    PyJsHoisted_pickSome_.func_name = 'pickSome'
    var.put('pickSome', PyJsHoisted_pickSome_)
    @Js
    def PyJsHoisted_pickMeta_(this, arguments, var=var):
        var = Scope({'arguments':arguments, 'this':this}, var)
        var.registers(['answers'])
        var.put('z', Js(2.0))
        if (var.get('level')>Js(9.0)):
            var.put('z', Js(3.0))
        var.put('answers', Js([]))
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<var.get('z')):
            var.put('x', var.get('meta').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('meta').get('length')))))
            if (var.get('answers').callprop('indexOf', var.get('x'))>(-Js(1.0))):
                pass
            else:
                var.get('answers').callprop('push', var.get('x'))
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
        
        var.get('answers').callprop('sort')
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<var.get('answers').get('length')):
            try:
                if (var.get('i')==Js(0.0)):
                    var.put('abOutput', (Js('(')+var.get('answers').get(var.get('i'))), '+')
                else:
                    var.put('abOutput', (Js(', ')+var.get('answers').get(var.get('i'))), '+')
            finally:
                    (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
        var.put('abOutput', Js(')'), '+')
    PyJsHoisted_pickMeta_.func_name = 'pickMeta'
    var.put('pickMeta', PyJsHoisted_pickMeta_)
    @Js
    def PyJsHoisted_genAbil_(this, arguments, var=var):
        var = Scope({'arguments':arguments, 'this':this}, var)
        var.registers([])
        var.put('d1', var.get('Math').callprop('floor', ((var.get('Math').callprop('random')*Js(6.0))+Js(1.0))))
        var.put('d2', var.get('Math').callprop('floor', ((var.get('Math').callprop('random')*Js(6.0))+Js(1.0))))
        var.put('d3', var.get('Math').callprop('floor', ((var.get('Math').callprop('random')*Js(6.0))+Js(1.0))))
        var.put('d4', var.get('Math').callprop('floor', ((var.get('Math').callprop('random')*Js(6.0))+Js(1.0))))
        var.put('total', ((((var.get('d1')+var.get('d2'))+var.get('d3'))+var.get('d4'))-var.get('Math').callprop('min', var.get('d1'), var.get('d2'), var.get('d3'), var.get('d4'))))
        return var.get('total')
    PyJsHoisted_genAbil_.func_name = 'genAbil'
    var.put('genAbil', PyJsHoisted_genAbil_)
    @Js
    def PyJsHoisted_showPlus_(x, this, arguments, var=var):
        var = Scope({'x':x, 'arguments':arguments, 'this':this}, var)
        var.registers(['x'])
        if (var.get('x')>(-Js(1.0))):
            return (Js('+')+var.get('x'))
        else:
            return var.get('x')
    PyJsHoisted_showPlus_.func_name = 'showPlus'
    var.put('showPlus', PyJsHoisted_showPlus_)
    @Js
    def PyJsHoisted_upgradeUncommon_(this, arguments, var=var):
        var = Scope({'arguments':arguments, 'this':this}, var)
        var.registers([])
        var.put('x', (Js(0.1)+((var.get('level')-Js(2.0))*Js(0.075))))
        if (var.get('level')==Js(1.0)):
            var.put('x', Js(0.0))
        if (var.get('Math').callprop('random')<var.get('x')):
            return Js(True)
        else:
            return Js(False)
    PyJsHoisted_upgradeUncommon_.func_name = 'upgradeUncommon'
    var.put('upgradeUncommon', PyJsHoisted_upgradeUncommon_)
    @Js
    def PyJsHoisted_dwarfMagicArmor_(this, arguments, var=var):
        var = Scope({'arguments':arguments, 'this':this}, var)
        var.registers([])
        if ((var.get('level')>Js(1.0)) and (var.get('racetxt')==Js('Mountain Dwarf'))):
            if (var.get('mod').get('1')>Js(2.0)):
                if (var.get('upgrade')()==Js(True)):
                    var.get('myAr').callprop('push', var.get('armors').get('3'))
                    return Js(True)
                else:
                    var.get('myAr').callprop('push', var.get('armors').get('2'))
                    return Js(True)
            else:
                if (var.get('upgradeUncommon')()==Js(True)):
                    var.get('myAr').callprop('push', var.get('armors').get('7'))
                    return Js(True)
                else:
                    var.get('myAr').callprop('push', var.get('armors').get('5'))
                    return Js(True)
        else:
            return Js(False)
    PyJsHoisted_dwarfMagicArmor_.func_name = 'dwarfMagicArmor'
    var.put('dwarfMagicArmor', PyJsHoisted_dwarfMagicArmor_)
    @Js
    def PyJsHoisted_showAbil_(this, arguments, var=var):
        var = Scope({'arguments':arguments, 'this':this}, var)
        var.registers([])
        var.put('passive', (Js(10.0)+var.get('mod').get('4')))
        if (var.get('skLearn').get('11')==Js(True)):
            var.put('passive', var.get('prof'), '+')
            if (var.get('expertise').callprop('indexOf', Js(11.0))>(-Js(1.0))):
                var.put('passive', var.get('prof'), '+')
        else:
            if (var.get('abOutput').callprop('indexOf', Js('Jack of all'))>(-Js(1.0))):
                var.put('passive', var.get('Math').callprop('floor', (var.get('prof')/Js(2.0))), '+')
        def PyJs_LONG_8_(var=var):
            def PyJs_LONG_7_(var=var):
                def PyJs_LONG_6_(var=var):
                    return ((((((((((((Js('<b>Ability scores:</b>==EOF==<pre>STR:  ')+var.get('digits')(var.get('abil').get('0')))+Js(' ('))+var.get('showPlus')(var.get('mod').get('0')))+Js(')   DEX:  '))+var.get('digits')(var.get('abil').get('1')))+Js(' ('))+var.get('showPlus')(var.get('mod').get('1')))+Js(')   CON: '))+var.get('digits')(var.get('abil').get('2')))+Js(' ('))+var.get('showPlus')(var.get('mod').get('2')))+Js(')   ==EOF==INT:  '))
                return ((((((((((((PyJs_LONG_6_()+var.get('digits')(var.get('abil').get('3')))+Js(' ('))+var.get('showPlus')(var.get('mod').get('3')))+Js(')   WIS:  '))+var.get('digits')(var.get('abil').get('4')))+Js(' ('))+var.get('showPlus')(var.get('mod').get('4')))+Js(')   CHA: '))+var.get('digits')(var.get('abil').get('5')))+Js(' ('))+var.get('showPlus')(var.get('mod').get('5')))+Js(')</pre>==EOF==<b>Saving throws:</b>==EOF==<pre>STR:  '))
            return (((((((((((PyJs_LONG_7_()+var.get('showPlus')(var.get('saves').get('0')))+Js('   DEX:  '))+var.get('showPlus')(var.get('saves').get('1')))+Js('    CON: '))+var.get('showPlus')(var.get('saves').get('2')))+Js('   ==EOF==INT:  '))+var.get('showPlus')(var.get('saves').get('3')))+Js('   WIS:  '))+var.get('showPlus')(var.get('saves').get('4')))+Js('    CHA: '))+var.get('showPlus')(var.get('saves').get('5')))
        var.put('output', ((((PyJs_LONG_8_()+Js('==EOF==</pre><b>Initiative:</b>  '))+var.get('showPlus')(var.get('initiative')))+Js('   <b>Speed:</b>  '))+var.get('speed')), '+')
        if ((var.get('bootsOfSS')==Js(True)) and (var.get('speed')<Js(30.0))):
            var.put('output', Js(' (30 with boots)'), '+')
        if (var.get('racetxt')==Js('Aarakocra')):
            var.put('output', Js(' (50 flying speed)'), '+')
        var.put('output', (((((Js('   <b>Passive perception:</b>  ')+var.get('passive'))+Js('==EOF==<b>Size:</b>  '))+var.get('size'))+Js('==EOF==<b>Proficiency bonus:</b>  '))+var.get('showPlus')(var.get('prof'))), '+')
        if (var.get('gender')==Js(2.0)):
            var.put('output', Js('==EOF==<b>Gender:</b> Female ♀'), '+')
        else:
            var.put('output', Js('==EOF==<b>Gender:</b>  Male ️♂'), '+')
        var.put('output', Js('==EOF=='), '+')
    PyJsHoisted_showAbil_.func_name = 'showAbil'
    var.put('showAbil', PyJsHoisted_showAbil_)
    PyJs_Object_0_ = Js({})
    var.put('possibile', PyJs_Object_0_)
    var.put('possibile', var.get('selStat')(var.get('level'), Js('selLevel'), var.get('possibile')))
    var.put('possibile', var.get('selStat')(var.get('gender'), Js('selGender'), var.get('possibile')))
    var.get('console').callprop('log', var.get('possibile'))
    var.get('console').callprop('log', var.get('possibile').get('selLevel'))
    var.get('console').callprop('log', var.get('possibile').get('selGender'))
    var.get('console').callprop('log', Js('-------------------------starting--------------------------------'))
    if ((var.get('magicGet')(Js('genMethod'), var.get('possibile')).get('value')==Js('2')) or (var.get('magicGet')(Js('genMethod'), var.get('possibile')).get('value')==Js('3'))):
        var.get('magicGet')(Js('buyDropdowns'), var.get('possibile')).get('style').put('display', Js('inline'))
    if (var.get('magicGet')(Js('genMethod'), var.get('possibile')).get('value')==Js('3')):
        var.put('detailedStats', var.get('document').callprop('getElementsByClassName', Js('detailed')))
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<var.get('detailedStats').get('length')):
            try:
                var.get('detailedStats').get(var.get('i')).get('style').put('display', Js('inline'))
            finally:
                    (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    if (var.get('magicGet')(Js('genMethod'), var.get('possibile')).get('value')!=Js('0')):
        var.get('magicGet')(Js('selAbil'), var.get('possibile')).get('style').put('display', Js('none'))
    if (var.get('magicGet')(Js('selClass'), var.get('possibile')).get('value')==Js(15.0)):
        var.get('magicGet')(Js('wizardOptions'), var.get('possibile')).get('style').put('display', Js('inline'))
    if (var.get('magicGet')(Js('selClass'), var.get('possibile')).get('value')==Js(3.0)):
        var.get('magicGet')(Js('clericOptions'), var.get('possibile')).get('style').put('display', Js('inline'))
    if (var.get('magicGet')(Js('selClass'), var.get('possibile')).get('value')==Js(4.0)):
        var.get('magicGet')(Js('druidOptions'), var.get('possibile')).get('style').put('display', Js('inline'))
    if (var.get('magicGet')(Js('selClass'), var.get('possibile')).get('value')==Js(1.0)):
        var.get('magicGet')(Js('barbarianOptions'), var.get('possibile')).get('style').put('display', Js('inline'))
    if (var.get('magicGet')(Js('selClass'), var.get('possibile')).get('value')==Js(2.0)):
        var.get('magicGet')(Js('bardOptions'), var.get('possibile')).get('style').put('display', Js('inline'))
    if ((var.get('magicGet')(Js('selClass'), var.get('possibile')).get('value')==Js(6.0)) or (var.get('magicGet')(Js('selClass'), var.get('possibile')).get('value')==Js(7.0))):
        var.get('magicGet')(Js('fighterOptions'), var.get('possibile')).get('style').put('display', Js('inline'))
    if (var.get('magicGet')(Js('selClass'), var.get('possibile')).get('value')==Js(8.0)):
        var.get('magicGet')(Js('monkOptions'), var.get('possibile')).get('style').put('display', Js('inline'))
    if (var.get('magicGet')(Js('selClass'), var.get('possibile')).get('value')==Js(9.0)):
        var.get('magicGet')(Js('paladinOptions'), var.get('possibile')).get('style').put('display', Js('inline'))
    if (var.get('magicGet')(Js('selClass'), var.get('possibile')).get('value')==Js(10.0)):
        var.get('magicGet')(Js('rangerOptions'), var.get('possibile')).get('style').put('display', Js('inline'))
    if (var.get('magicGet')(Js('selClass'), var.get('possibile')).get('value')==Js(11.0)):
        var.get('magicGet')(Js('rogueOptions'), var.get('possibile')).get('style').put('display', Js('inline'))
    if (var.get('magicGet')(Js('selClass'), var.get('possibile')).get('value')==Js(13.0)):
        var.get('magicGet')(Js('sorcererOptions'), var.get('possibile')).get('style').put('display', Js('inline'))
    if (var.get('magicGet')(Js('selClass'), var.get('possibile')).get('value')==Js(14.0)):
        var.get('magicGet')(Js('warlockOptions'), var.get('possibile')).get('style').put('display', Js('inline'))
    var.put('al', Js(False))
    if (var.get('magicGet')(Js('al'), var.get('possibile')).get('checked')==Js(True)):
        var.put('al', Js(True))
    var.put('gender', (-Js(1.0)))
    var.put('forceGender', Js(0.0))
    var.put('forceGender', (var.get('magicGet')(Js('selGender'), var.get('possibile')).get('value')*Js(1.0)))
    var.put('forceCl', Js(0.0))
    var.put('forceCl', (var.get('magicGet')(Js('selClass'), var.get('possibile')).get('value')*Js(1.0)))
    var.put('forceRace', Js(0.0))
    var.put('forceRace', (var.get('magicGet')(Js('selRace'), var.get('possibile')).get('value')*Js(1.0)))
    var.put('forceBg', Js(0.0))
    var.put('forceBg', (var.get('magicGet')(Js('selBg'), var.get('possibile')).get('value')*Js(1.0)))
    var.put('forceAbil', Js(0.0))
    var.put('forceAbil', (var.get('magicGet')(Js('selAbil'), var.get('possibile')).get('value')*Js(1.0)))
    var.put('forceDomain', Js(0.0))
    var.put('forceDomain', (var.get('magicGet')(Js('selCleric'), var.get('possibile')).get('value')*Js(1.0)))
    var.put('forceSchool', Js(0.0))
    var.put('forceSchool', (var.get('magicGet')(Js('selWizard'), var.get('possibile')).get('value')*Js(1.0)))
    var.put('forceCircle', Js(0.0))
    var.put('forceCircle', (var.get('magicGet')(Js('selDruid'), var.get('possibile')).get('value')*Js(1.0)))
    var.put('forceBarb', (var.get('magicGet')(Js('selBarbarian'), var.get('possibile')).get('value')*Js(1.0)))
    var.put('forceBard', (var.get('magicGet')(Js('selBard'), var.get('possibile')).get('value')*Js(1.0)))
    var.put('forceFigh', (var.get('magicGet')(Js('selFighter'), var.get('possibile')).get('value')*Js(1.0)))
    var.put('forceMonk', (var.get('magicGet')(Js('selMonk'), var.get('possibile')).get('value')*Js(1.0)))
    var.put('forcePala', (var.get('magicGet')(Js('selPaladin'), var.get('possibile')).get('value')*Js(1.0)))
    var.put('forceRang', (var.get('magicGet')(Js('selRanger'), var.get('possibile')).get('value')*Js(1.0)))
    var.put('forceRogu', (var.get('magicGet')(Js('selRogue'), var.get('possibile')).get('value')*Js(1.0)))
    var.put('forceSorc', (var.get('magicGet')(Js('selSorcerer'), var.get('possibile')).get('value')*Js(1.0)))
    var.put('forceWarl', (var.get('magicGet')(Js('selWarlock'), var.get('possibile')).get('value')*Js(1.0)))
    var.put('forceWarlPact', (var.get('magicGet')(Js('selWarlockPact'), var.get('possibile')).get('value')*Js(1.0)))
    var.put('x', Js(0.0))
    var.put('y', Js(0.0))
    var.put('z', Js(0.0))
    var.put('xx', Js(0.0))
    var.put('yy', Js(0.0))
    var.put('i', Js(0.0))
    var.put('q', Js(0.0))
    var.put('whichMagic', (-Js(1.0)))
    var.put('whichMagicArmor', (-Js(1.0)))
    var.put('magicArrowPlus', Js(0.0))
    var.put('magicArrows', Js(0.0))
    var.put('magicArrowType', Js(''))
    var.put('magicArrowDisplay', Js(False))
    var.put('rangedWeapons', Js([]))
    var.put('mod', Js([Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0)]))
    var.put('abil', Js([Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0)]))
    var.put('abilNames', Js([Js('Strength'), Js('Dexterity'), Js('Constitution'), Js('Intelligence'), Js('Wisdom'), Js('Charisma')]))
    var.put('firstIncrease', (-Js(1.0)))
    var.put('output', Js(''))
    var.put('hp', Js(0.0))
    pass
    var.put('ac', Js(0.0))
    var.put('hd', Js(0.0))
    var.put('gold', Js(0.0))
    var.put('platinum', Js(0.0))
    var.put('forceLvl', Js(0.0))
    var.put('forceLvl', (var.get('magicGet')(Js('selLevel'), var.get('possibile')).get('value')*Js(1.0)))
    var.get('console').callprop('log', (Js('forceLvl: ')+var.get('forceLvl')))
    var.put('level', var.get('Math').callprop('floor', ((var.get('Math').callprop('random')*Js(10.0))+Js(1.0))))
    if (var.get('forceLvl')>Js(0.0)):
        var.put('level', var.get('forceLvl'))
    if (var.get('forceLvl')==Js(21.0)):
        var.put('level', var.get('Math').callprop('floor', ((var.get('Math').callprop('random')*Js(4.0))+Js(1.0))))
    if (var.get('forceLvl')==Js(22.0)):
        var.put('level', var.get('Math').callprop('floor', ((var.get('Math').callprop('random')*Js(6.0))+Js(5.0))))
    if (var.get('forceLvl')==Js(23.0)):
        var.put('level', var.get('Math').callprop('floor', ((var.get('Math').callprop('random')*Js(4.0))+Js(8.0))))
    if (var.get('forceLvl')==Js(24.0)):
        var.put('level', var.get('Math').callprop('floor', ((var.get('Math').callprop('random')*Js(4.0))+Js(12.0))))
    if (var.get('forceLvl')==Js(25.0)):
        var.put('level', var.get('Math').callprop('floor', ((var.get('Math').callprop('random')*Js(4.0))+Js(17.0))))
    var.get('console').callprop('log', (Js('LEVEL: ')+var.get('level')))
    var.put('prof', Js(2.0))
    if (var.get('level')>Js(4.0)):
        var.put('prof', Js(3.0))
    if (var.get('level')>Js(8.0)):
        var.put('prof', Js(4.0))
    if (var.get('level')>Js(12.0)):
        var.put('prof', Js(5.0))
    if (var.get('level')>Js(16.0)):
        var.put('prof', Js(6.0))
    var.put('languageOutput', Js(''))
    var.put('moreLang', Js(0.0))
    var.put('speed', Js(0.0))
    var.put('size', Js('Medium'))
    var.put('factions', Js([Js('Harpers'), Js('Order of the Gauntlet'), Js('Emerald Enclave'), Js("Lords' Alliance"), Js('Zhentarim')]))
    var.put('myFaction', (-Js(1.0)))
    var.put('lifestyles', Js([Js('Wretched'), Js('Squalid'), Js('Poor'), Js('Modest'), Js('Comfortable'), Js('Wealthy'), Js('Artistocratic')]))
    var.put('myLifestyle', (-Js(1.0)))
    var.put('skills', Js([Js('Acrobatics'), Js('Animal Handling'), Js('Arcana'), Js('Athletics'), Js('Deception'), Js('History'), Js('Insight'), Js('Intimidation'), Js('Investigation'), Js('Medicine'), Js('Nature'), Js('Perception'), Js('Perform'), Js('Persuasion'), Js('Religion'), Js('Sleight of Hand'), Js('Stealth'), Js('Survival')]))
    var.put('patronSpells1', Js([]))
    var.put('patronSpells2', Js([]))
    var.put('patronSpells3', Js([]))
    var.put('patronSpells4', Js([]))
    var.put('patronSpells5', Js([]))
    var.put('pa1', Js([Js('Bless'), Js('Command'), Js('Compelled Duel'), Js('Cure Wounds'), Js('Detect Evil and Good'), Js('Detect Magic'), Js('Detect Poison and Disease'), Js('Divine Favor'), Js('Heroism'), Js('Protection from Evil and Good'), Js('Purify Food and Drink'), Js('Searing Smite'), Js('Shield of Faith'), Js('Thunderous Smite'), Js('Wrathful Smite')]))
    var.put('pa2', Js([Js('Aid'), Js('Branding Smite'), Js('Find Steed'), Js('Lesser Restoration'), Js('Locate Object'), Js('Magic Weapon'), Js('Protection from Poison'), Js('Zone of Truth')]))
    var.put('pa3', Js([Js('Aura of Vitality'), Js('Blinding Smite'), Js('Create Food and Water'), Js("Crusader's Mantle"), Js('Daylight'), Js('Dispel Magic'), Js('Elemental Weapon')]))
    var.put('ra1', Js([Js('Absorb Elements'), Js('Beast Bond'), Js('Alarm'), Js('Animal Friendship'), Js('Cure Wounds'), Js('Detect Magic'), Js('Detect Poison and Disease'), Js('Ensnaring Strike'), Js('Fog Cloud'), Js('Goodberry'), Js('Hail of Thorns'), Js("Hunter's Mark"), Js('Jump'), Js('Longstrider'), Js('Speak with Animals')]))
    var.put('ra2', Js([Js('Animal Messenger'), Js('Barkskin'), Js('Beast Sense'), Js('Cordon of Arrows'), Js('Darkvision'), Js('Find Traps'), Js('Lesser Restoration'), Js('Locate Animals or Plants'), Js('Locate Object'), Js('Pass without Trace'), Js('Protection from Poison'), Js('Silence'), Js('Spike Growth')]))
    var.put('ra3', Js([Js('Flame Arrows'), Js('Conjure Animals'), Js('Conjure Barrage'), Js('Daylight'), Js('Lightning Arrow'), Js('Nondetection'), Js('Plant Growth'), Js('Protection from Energy'), Js('Speak with Plants'), Js('Water Breathing'), Js('Water Walk'), Js('Wind Wall')]))
    var.put('clCantrip', Js([Js('Guidance'), Js('Light'), Js('Mending'), Js('Resistance'), Js('Sacred Flame'), Js('Spare the Dying'), Js('Thaumaturgy')]))
    var.put('cl1', Js([Js('Bane'), Js('Bless'), Js('Command'), Js('Create or Destroy Water'), Js('Cure Wounds'), Js('Detect Evil and Good'), Js('Detect Magic'), Js('Detect Poison and Disease'), Js('Guiding Bolt'), Js('Healing Word'), Js('Inflict Wounds'), Js('Protection from Evil and Good'), Js('Purify Food and Drink'), Js('Sanctuary'), Js('Shield of Faith')]))
    var.put('cl2', Js([Js('Aid'), Js('Augury'), Js('Blindness/Deafness'), Js('Calm Emotions'), Js('Continual Flame'), Js('Enhance Ability'), Js('Find Traps'), Js('Gentle Repose'), Js('Hold Person'), Js('Lesser Restoration'), Js('Locate Object'), Js('Prayer of Healing'), Js('Protection from Poison'), Js('Silence'), Js('Spiritual Weapon'), Js('Warding Bond'), Js('Zone of Truth')]))
    var.put('cl3', Js([Js('Animate Dead'), Js('Beacon of Hope'), Js('Bestow Curse'), Js('Clairvoyance'), Js('Create Food and Water'), Js('Daylight'), Js('Dispel Magic'), Js('Feign Death'), Js('Glyph of Warding'), Js('Magic Circle'), Js('Mass Healing Word'), Js('Meld into Stone'), Js('Protection from Energy'), Js('Remove Curse'), Js('Revivify'), Js('Sending'), Js('Speak with Dead'), Js('Spirit Guardians'), Js('Tongues'), Js('Water Walk')]))
    var.put('cl4', Js([Js('Banishment'), Js('Control Water'), Js('Death Ward'), Js('Divination'), Js('Freedom of Movement'), Js('Guardian of Faith'), Js('Locate Creature'), Js('Stone Shape')]))
    var.put('cl5', Js([Js('Commune'), Js('Contagion'), Js('Dispel Evil and Good'), Js('Flame Strike'), Js('Geas'), Js('Greater Restoration'), Js('Hallow'), Js('Insect Plague'), Js('Legend Lore'), Js('Mass Cure Wounds'), Js('Planar Binding'), Js('Raise Dead'), Js('Scrying')]))
    var.put('baCantrip', Js([Js('Blade Ward'), Js('Dancing Lights'), Js('Friends'), Js('Light'), Js('Mage Hand'), Js('Mending'), Js('Message'), Js('Minor Illusion'), Js('Prestidigitation'), Js('Thunderclap'), Js('True Strike'), Js('Vicious Mockery')]))
    var.put('ba1', Js([Js('Animal Friendship'), Js('Bane'), Js('Charm Person'), Js('Comprehend Languages'), Js('Cure Wounds'), Js('Detect Magic'), Js('Disguise Self'), Js('Dissonant Whispers'), Js('Earth Tremor'), Js('Faerie Fire'), Js('Feather Fall'), Js('Healing Word'), Js('Heroism'), Js('Identify'), Js('Illusory Script'), Js('Longstrider'), Js('Silent Image'), Js('Sleep'), Js('Speak with Animals'), Js("Tasha's Hideous Laughter"), Js('Thunderwave'), Js('Unseen Servant')]))
    var.put('ba2', Js([Js('Animal Messenger'), Js('Blindness/Deafness'), Js('Calm Emotions'), Js('Cloud of Daggers'), Js('Crown of Madness'), Js('Detect Thoughts'), Js('Enhance Ability'), Js('Enthrall'), Js('Heat Metal'), Js('Hold Person'), Js('Invisibility'), Js('Knock'), Js('Lesser Restoration'), Js('Locate Animals or Plants'), Js('Locate Object'), Js('Magic Mouth'), Js('Phantasmal Force'), Js('Pyrotechnics'), Js('See Invisibility'), Js('Shatter'), Js('Silence'), Js('Skywrite'), Js('Suggestion'), Js('Warding Wind'), Js('Zone of Truth')]))
    var.put('ba3', Js([Js('Bestow Curse'), Js('Clairvoyance'), Js('Dispel Magic'), Js('Fear'), Js('Feign Death'), Js('Glyph of Warding'), Js('Hypnotic Pattern'), Js('Leomund’s Tiny Hut'), Js('Major Image'), Js('Nondetection'), Js('Plant Growth'), Js('Sending'), Js('Speak with Dead'), Js('Speak with Plants'), Js('Stinking Cloud'), Js('Tongues')]))
    var.put('ba4', Js([Js('Compulsion'), Js('Confusion'), Js('Dimension Door'), Js('Freedom of Movement'), Js('Greater Invisibility'), Js('Hallucinatory Terrain'), Js('Locate Creature'), Js('Polymorph')]))
    var.put('ba5', Js([Js('Animate Objects'), Js('Awaken'), Js('Dominate Person'), Js('Dream'), Js('Geas'), Js('Greater Restoration'), Js('Hold Monster'), Js('Legend Lore'), Js('Mass Cure Wounds'), Js('Mislead'), Js('Modify Memory'), Js('Planar Binding'), Js('Raise Dead'), Js('Scrying'), Js('Seeming'), Js('Teleportation Circle')]))
    var.put('drCantrip', Js([Js('Create Bonfire'), Js('Control Flames'), Js('Druidcraft'), Js('Frostbite'), Js('Guidance'), Js('Gust'), Js('Magic Stone'), Js('Mending'), Js('Mold earth'), Js('Poison Spray'), Js('Produce Flame'), Js('Resistance'), Js('Shillelagh'), Js('Shape Water'), Js('Thorn Whip'), Js('Thunderclap')]))
    var.put('dr1', Js([Js('Absorb Elements'), Js('Beast Bond'), Js('Ice Knife'), Js('Earth Tremor'), Js('Animal Friendship'), Js('Charm Person'), Js('Create or Destroy Water'), Js('Cure Wounds'), Js('Detect Magic'), Js('Detect Poison and Disease'), Js('Entangle'), Js('Faerie Fire'), Js('Fog Cloud'), Js('Goodberry'), Js('Healing Word'), Js('Jump'), Js('Longstrider'), Js('Purify Food and Drink'), Js('Speak with Animals'), Js('Thunderwave')]))
    var.put('dr2', Js([Js('Dust Devil'), Js('Earthbind'), Js('Skywrite'), Js('Warding Wind'), Js('Animal Messenger'), Js('Barkskin'), Js('Beast Sense'), Js('Darkvision'), Js('Enhance Ability'), Js('Find Traps'), Js('Flame Blade'), Js('Flaming Sphere'), Js('Gust of Wind'), Js('Heat Metal'), Js('Hold Person'), Js('Lesser Restoration'), Js('Locate Object'), Js('Moonbeam'), Js('Pass without Trace'), Js('Protection from Poison'), Js('Spike Growth')]))
    var.put('dr3', Js([Js('Erupting Earth'), Js('Flame Arrows'), Js('Tidal Wave'), Js('Wall of Water'), Js('Call Lightning'), Js('Conjure Animals'), Js('Daylight'), Js('Dispel Magic'), Js('Feign Death'), Js('Meld into Stone'), Js('Plant Growth'), Js('Protection from Energy'), Js('Sleet Storm'), Js('Speak with Plants'), Js('Water Breathing'), Js('Water Walk'), Js('Wind Wall')]))
    var.put('dr4', Js([Js('Elemental Bane'), Js('Watery Sphere'), Js('Blight'), Js('Confusion'), Js('Conjure Minor Elementals'), Js('Conjure Woodland Beings'), Js('Control Water'), Js('Dominate Beast'), Js('Freedom of Movement'), Js('Giant Insect'), Js('Grasping Vine'), Js('Hallucinatory Terrain'), Js('Ice Storm'), Js('Locate Creature'), Js('Polymorph'), Js('Stone Shape'), Js('Stoneskin'), Js('Wall of Fire')]))
    var.put('dr5', Js([Js('Control Winds'), Js('Maelstrom'), Js('Transmute Rock'), Js('Antilife Shell'), Js('Awaken'), Js('Commune with Nature'), Js('Conjure Elemental'), Js('Contagion'), Js('Geas'), Js('Greater Restoration'), Js('Insect Plague'), Js('Mass Cure Wounds'), Js('Planar Binding'), Js('Reincarnate'), Js('Scrying'), Js('Tree Stride'), Js('Wall of Stone')]))
    var.put('soCantrip', Js([Js('Create Bonfire'), Js('Control Flames'), Js('Frostbite'), Js('Gust'), Js('Mold Earth'), Js('Shape Water'), Js('Thunderclap'), Js('Acid Splash'), Js('Blade Ward'), Js('Chill Touch'), Js('Dancing Lights'), Js('Fire Bolt'), Js('Friends'), Js('Light'), Js('Mage Hand'), Js('Mending'), Js('Message'), Js('Minor Illusion'), Js('Poison Spray'), Js('Prestidigitation'), Js('Ray of Frost'), Js('Shocking Grasp'), Js('True Strike')]))
    var.put('so1', Js([Js('Catapult'), Js('Ice Knife'), Js('Earth Tremor'), Js('Burning Hands'), Js('Burning Hands'), Js('Charm Person'), Js('Chromatic Orb'), Js('Color Spray'), Js('Comprehend Languages'), Js('Detect Magic'), Js('Disguise Self'), Js('Expeditious Retreat'), Js('False Life'), Js('Feather Fall'), Js('Fog Cloud'), Js('Jump'), Js('Magic Missile'), Js('Magic Missile'), Js('Mage Armor'), Js('Ray of Sickness'), Js('Shield'), Js('Silent Image'), Js('Sleep'), Js('Thunderwave'), Js('Witch Bolt')]))
    var.put('so2', Js([Js("Aganazzar's Scorcher"), Js('Dust Devil'), Js('Earthbind'), Js("Maximilian's Earthen Grasp"), Js('Pyrotechnics'), Js("Snilloc's Snowball Swarm"), Js('Warding Wind'), Js('Alter Self'), Js('Blindness/Deafness'), Js('Blur'), Js('Cloud of Daggers'), Js('Crown of Madness'), Js('Darkness'), Js('Darkvision'), Js('Detect Thoughts'), Js('Enhance Ability'), Js('Enlarge/Reduce'), Js('Gust of Wind'), Js('Hold Person'), Js('Invisibility'), Js('Knock'), Js('Levitate'), Js('Mirror Image'), Js('Misty Step'), Js('Phantasmal Force'), Js('Scorching Ray'), Js('See Invisibility'), Js('Shatter'), Js('Spider Climb'), Js('Suggestion'), Js('Web')]))
    var.put('so3', Js([Js('Erupting Earth'), Js('Flame Arrows'), Js("Melf's Minute Meteors"), Js('Wall of Water'), Js('Blink'), Js('Clairvoyance'), Js('Counterspell'), Js('Daylight'), Js('Dispel Magic'), Js('Fear'), Js('Fireball'), Js('Fly'), Js('Gaseous Form'), Js('Haste'), Js('Hypnotic Pattern'), Js('Lightning Bolt'), Js('Major Image'), Js('Protection from Energy'), Js('Sleet Storm'), Js('Slow'), Js('Stinking Cloud'), Js('Tongues'), Js('Water Breathing'), Js('Water Walk')]))
    var.put('so4', Js([Js('Storm Sphere'), Js('Vitriolic Sphere'), Js('Watery Sphere'), Js('Banishment'), Js('Blight'), Js('Confusion'), Js('Dimension Door'), Js('Dominate Beast'), Js('Greater Invisibility'), Js('Ice Storm'), Js('Polymorph'), Js('Stoneskin'), Js('Wall of Fire')]))
    var.put('so5', Js([Js('Control Winds'), Js('Immolation'), Js('Animate Objects'), Js('Cloudkill'), Js('Cone of Cold'), Js('Creation'), Js('Dominate Person'), Js('Hold Monster'), Js('Insect Plague'), Js('Seeming'), Js('Telekinesis'), Js('Teleportation Circle'), Js('Wall of Stone')]))
    var.put('waCantrip', Js([Js('Create Bonfire'), Js('Frostbite'), Js('Magic Stone'), Js('Thunderclap'), Js('Blade Ward'), Js('Chill Touch'), Js('Eldritch Blast'), Js('Friends'), Js('Mage Hand'), Js('Minor Illusion'), Js('Poison Spray'), Js('Prestidigitation'), Js('True Strike')]))
    var.put('wa1', Js([Js('Armor of Agathys'), Js('Arms of Hadar'), Js('Charm Person'), Js('Comprehend Languages'), Js('Expeditious Retreat'), Js('Hellish Rebuke'), Js('Hex'), Js('Illusory Script'), Js('Protection from Good and Evil'), Js('Unseen Servant'), Js('Witch Bolt')]))
    var.put('wa2', Js([Js('Earthbind'), Js('Cloud of Daggers'), Js('Crown of Madness'), Js('Darkness'), Js('Enthrall'), Js('Hold Person'), Js('Invisibility'), Js('Mirror Image'), Js('Misty Step'), Js('Ray of Enfeeblement'), Js('Shatter'), Js('Spider Climb'), Js('Suggestion')]))
    var.put('wa3', Js([Js('Counterspell'), Js('Dispel Magic'), Js('Fear'), Js('Fly'), Js('Gaseous Form'), Js('Hunger of Hadar'), Js('Hypnotic Pattern'), Js('Magic Circle'), Js('Major Image'), Js('Remove Curse'), Js('Tongues'), Js('Vampiric Touch')]))
    var.put('wa4', Js([Js('Elemental Bane'), Js('Banishment'), Js('Blight'), Js('Dimension Door'), Js('Hallucinatory Terrain')]))
    var.put('wa5', Js([Js('Contact Other Plane'), Js('Dream'), Js('Hold Monster'), Js('Scrying')]))
    var.put('tomeRituals', Js([Js('Illusory Script'), Js('Identify'), Js('Identify'), Js('Identify'), Js('Find Familiar'), Js('Detect Disease and Poison'), Js('Detect Magic'), Js('Detect Magic'), Js('Detect Magic'), Js('Comprehend Languages'), Js('Unseen Servant'), Js("Tenser's Floating Disk"), Js('Speak with Animals'), Js('Speak with Animals'), Js('Purify Food and Drink'), Js('Alarm'), Js('Alarm')]))
    var.put('wiCantrip', Js([Js('Create Bonfire'), Js('Control Flames'), Js('Frostbite'), Js('Gust'), Js('Mold Earth'), Js('Shape Water'), Js('Thunderclap'), Js('Acid Splash'), Js('Blade Ward'), Js('Chill Touch'), Js('Dancing Lights'), Js('Fire Bolt'), Js('Friends'), Js('Light'), Js('Mage Hand'), Js('Mending'), Js('Message'), Js('Minor Illusion'), Js('Poison Spray'), Js('Prestidigitation'), Js('Ray of Frost'), Js('Shocking Grasp'), Js('True Strike')]))
    var.put('wi1', Js([Js('Absorb Elements'), Js('Catapult'), Js('Ice Knife'), Js('Earth Tremor'), Js('Alarm'), Js('Burning Hands'), Js('Charm Person'), Js('Chromatic Orb'), Js('Color Spray'), Js('Comprehend Languages'), Js('Detect Magic'), Js('Disguise Self'), Js('Expeditious Retreat'), Js('False Life'), Js('Feather Fall'), Js('Find Familiar'), Js('Find Familiar'), Js('Fog Cloud'), Js('Grease'), Js('Identify'), Js('Illusory Script'), Js('Jump'), Js('Longstrider'), Js('Mage Armor'), Js('Magic Missile'), Js('Protection from Good and Evil'), Js('Ray of Sickness'), Js('Shield'), Js('Silent Image'), Js('Sleep'), Js("Tasha's Hideous Laughter"), Js("Tenser's Floating Disk"), Js('Thunderwave'), Js('Unseen Servant'), Js('Witch Bolt')]))
    var.put('wi2', Js([Js("Aganazzar's Scorcher"), Js('Dust Devil'), Js('Earthbind'), Js("Maximilian's Earthen Grap"), Js('Pyrotechnics'), Js('Skywrite'), Js("Snilloc's Snowball Swarm"), Js('Alter Self'), Js('Arcane Lock'), Js('Blindness/Deafness'), Js('Blur'), Js('Cloud of Daggers'), Js('Continual Flame'), Js('Crown of Madness'), Js('Darkness'), Js('Darkvision'), Js('Detect Thoughts'), Js('Enlarge/Reduce'), Js('Flaming Sphere'), Js('Gentle Repose'), Js('Gust of Wind'), Js('Hold Person'), Js('Invisibility'), Js('Knock'), Js('Levitate'), Js('Locate Object'), Js('Magic Mouth'), Js('Magic Weapon'), Js("Melf's Acid Arrow"), Js('Mirror Image'), Js('Misty Step'), Js("Nystul's Magic Aura"), Js('Phantasmal Force'), Js('Ray of Enfeeblement'), Js('Rope Trick'), Js('Scorching Ray'), Js('See Invisibility'), Js('Shatter'), Js('Spider Climb'), Js('Suggestion'), Js('Web')]))
    var.put('wi3', Js([Js('Erupting Earth'), Js('Flame Arrows'), Js("Melf's Minute Meteors"), Js('Tidal Wave'), Js('Wall of Sand'), Js('Wall of Water'), Js('Animate Dead'), Js('Bestow Curse'), Js('Blink'), Js('Clairvoyance'), Js('Counterspell'), Js('Dispel Magic'), Js('Fear'), Js('Feign Death'), Js('Fireball'), Js('Fly'), Js('Gaseous Form'), Js('Glyph of Warding'), Js('Haste'), Js('Hypnotic Pattern'), Js('Leomund’s Tiny Hut'), Js('Lightning Bolt'), Js('Magic Circle'), Js('Major Image'), Js('Nondetection'), Js('Phantom Steed'), Js('Protection from Energy'), Js('Remove Curse'), Js('Sending'), Js('Sleet Storm'), Js('Slow'), Js('Stinking Cloud'), Js('Tongues'), Js('Vampiric Touch'), Js('Water Breathing')]))
    var.put('wi4', Js([Js('Elemental Bane'), Js('Storm Sphere'), Js('Vitriolic Sphere'), Js('Watery Sphere'), Js('Arcane Eye'), Js('Banishment'), Js('Blight'), Js('Confusion'), Js('Conjure Minor Elementals'), Js('Control Water'), Js('Dimension Door'), Js("Evard's Black Tentacles"), Js('Fabricate'), Js('Fire Shield'), Js('Greater Invisibility'), Js('Hallucinatory Terrain'), Js('Ice Storm'), Js('Leomund’s Secret Chest'), Js('Locate Creature'), Js('Mordenkainen’s Faithful Hound'), Js('Mordenkainen’s Private Sanctum'), Js('Otiluke’s Resilient Sphere'), Js('Phantasmal Killer'), Js('Polymorph'), Js('Stone Shape'), Js('Stoneskin'), Js('Wall of Fire')]))
    var.put('wi5', Js([Js('Control Winds'), Js('Immolation'), Js('Transmute Rock'), Js('Animate Objects'), Js('Bigby’s Hand'), Js('CloudkilI'), Js('Cone of Cold'), Js('Conjure Elemental'), Js('Contact Other Plane'), Js('Creation'), Js('Dominate Person'), Js('Dream'), Js('Geas'), Js('Hold Monster'), Js('Legend Lore'), Js('Mislead'), Js('Modify Memory'), Js('Passwall'), Js('Planar Binding'), Js('Rary’s Telepathic Bond'), Js('Scrying'), Js('Seeming'), Js('Telekinesis'), Js('Teleportation Circle'), Js('Wall of Force'), Js('Wall of Stone')]))
    var.put('scrollBardUnc', Js([Js('Cure Wounds'), Js('Speak with Dead'), Js('Fear'), Js('Invisibility'), Js('Dispel Magic'), Js('Polymorph'), Js('Major Image')]))
    var.put('scrollBardRare', Js([Js('Animate Objects'), Js('Hold Monster'), Js('Guards and Wards'), Js('Raise Dead')]))
    var.put('scrollBardVery', Js([Js('Teleport'), Js('Power Word Kill'), Js('Power Word Stun')]))
    var.put('scrollClerUnc', Js([Js('Prayer of Healing'), Js('Prayer of Healing'), Js('Magic Circle'), Js('Aid'), Js('Tongues'), Js('Mass Healing Word'), Js('Revivify'), Js('Revivify'), Js('Guardian of Faith')]))
    var.put('scrollClerRare', Js([Js('Flame Strike'), Js('Mass Cure Wounds'), Js('Blade Barrier'), Js('Raise Dead'), Js('Heal')]))
    var.put('scrollClerVery', Js([Js('Control Weather'), Js('Regenerate'), Js('Heal'), Js('True Resurrection'), Js('Gate')]))
    var.put('scrollDruiUnc', Js([Js('Cure Wounds'), Js('Conjure Animals'), Js('Conjure Minor Elementals'), Js('Hold Person'), Js('Water Breathing')]))
    var.put('scrollDruiRare', Js([Js('Mass Cure Wounds'), Js('Scrying'), Js('Dominate Beast'), Js('Heal')]))
    var.put('scrollDruiVery', Js([Js('Heal'), Js('Wall of Thorns'), Js('Earthquake'), Js('True Resurrection'), Js('Tsunami')]))
    var.put('scrollPalaUnc', Js([Js('Cure Wounds'), Js('Blinding Smite'), Js('Dispel Magic'), Js('Aura of Life'), Js('Detect Magic'), Js('Aid')]))
    var.put('scrollPalaRare', Js([Js('Raise Dead'), Js('Geas'), Js('Banishing Smite')]))
    var.put('scrollPalaVery', Js([Js('Raise Dead'), Js('Geas'), Js('Banishing Smite')]))
    var.put('scrollRangUnc', Js([Js('Cure Wounds'), Js('Lightning Arrow'), Js('Conjure Barrage'), Js('Water Breathing')]))
    var.put('scrollRangRare', Js([Js('Conjure Volley'), Js('Swift Quiver')]))
    var.put('scrollRangVery', Js([Js('Conjure Volley'), Js('Swift Quiver')]))
    var.put('scrollWarlUnc', Js([Js('Vampiric Touch'), Js('Tongues'), Js('Gaseous Form'), Js('Fear'), Js('Spider Climb'), Js('Comprehend Languages'), Js('Shatter')]))
    var.put('scrollWarlRare', Js([Js('Blight'), Js('Scrying'), Js('Hold Monster'), Js('Conjure Fey')]))
    var.put('scrollWarlVery', Js([Js('Mass Suggestion'), Js('Finger of Death'), Js('Power Word Stun')]))
    var.put('scrollWizaUnc', Js([Js('Fireball'), Js('Haste'), Js('Slow'), Js('Fly'), Js('Knock'), Js('Lightning Bolt'), Js('Water Breathing'), Js('Dispel Magic')]))
    var.put('scrollWizaRare', Js([Js('Greater Invisibility'), Js('Wall of Fire'), Js('Ice Storm')]))
    var.put('scrollWizaVery', Js([Js('Mass Suggestion'), Js('Plane Shift'), Js('Delayed Blast Fireball')]))
    var.put('ci0', Js([Js('Hold Person'), Js('Spike Growth'), Js('Sleet Storm'), Js('Slow')]))
    var.put('ci1', Js([Js('Mirror image'), Js('Misty Step'), Js('Water Breathing'), Js('Water Walk')]))
    var.put('ci2', Js([Js('Blur'), Js('Silence'), Js('Create Food and Water'), Js('Protection from Energy')]))
    var.put('ci3', Js([Js('Barkskin'), Js('Spider Climb'), Js('Call Lightning'), Js('Plant Growth')]))
    var.put('ci4', Js([Js('Invisibility'), Js('Pass Without Trace'), Js('Daylight'), Js('Haste')]))
    var.put('ci5', Js([Js('Spider Climb'), Js('Spike Growth'), Js('Lightning Bolt'), Js('Meld into Stone')]))
    var.put('ci6', Js([Js('Darkness'), Js('Melf’s Acid Arrow'), Js('Water Walk'), Js('Stinking Cloud')]))
    var.put('ci7', Js([Js('Spider Climb'), Js('Web'), Js('Gaseous Form'), Js('Stinking Cloud')]))
    var.put('spellAbility', (-Js(1.0)))
    var.put('raceSpellAbility', (-Js(1.0)))
    var.put('raceSpells', Js([]))
    var.put('wiSchool', (-Js(1.0)))
    var.put('waPatron', (-Js(1.0)))
    var.put('soOrigin', (-Js(1.0)))
    var.put('clDomain', (-Js(1.0)))
    var.put('drCircle', (-Js(1.0)))
    var.put('ciSpells', Js([]))
    var.put('oaSpells', Js([]))
    var.put('doSpells', Js([]))
    var.put('loSpells', Js([]))
    var.put('waSpells', Js([]))
    var.put('wiz1', Js(0.0))
    var.put('wiz2', Js(0.0))
    var.put('wiz3', Js(0.0))
    var.put('wiz4', Js(0.0))
    var.put('wiz5', Js(0.0))
    var.put('wiz1Prepared', Js([]))
    var.put('wiz2Prepared', Js([]))
    var.put('wiz3Prepared', Js([]))
    var.put('wiz4Prepared', Js([]))
    var.put('wiz5Prepared', Js([]))
    var.put('tempTxt', Js(''))
    var.put('exotic', Js(0.0))
    var.put('land', Js(''))
    var.put('fiStyle', (-Js(1.0)))
    var.put('fiStyle2', (-Js(1.0)))
    var.put('ki', Js(0.0))
    var.put('ss1', Js(0.0))
    var.put('ss2', Js(0.0))
    var.put('ss3', Js(0.0))
    var.put('ss4', Js(0.0))
    var.put('ss5', Js(0.0))
    var.put('sp', Js(0.0))
    var.put('hasShield', Js(False))
    var.put('hasArmor', (-Js(1.0)))
    var.put('skLearn', Js([Js(False), Js(False), Js(False), Js(False), Js(False), Js(False), Js(False), Js(False), Js(False), Js(False), Js(False), Js(False), Js(False), Js(False), Js(False), Js(False), Js(False), Js(False)]))
    def PyJs_LONG_1_(var=var):
        return var.put('allArrays', Js([Js([Js(15.0), Js(15.0), Js(15.0), Js(8.0), Js(8.0), Js(8.0)]), Js([Js(15.0), Js(15.0), Js(14.0), Js(10.0), Js(8.0), Js(8.0)]), Js([Js(15.0), Js(15.0), Js(14.0), Js(9.0), Js(9.0), Js(8.0)]), Js([Js(15.0), Js(15.0), Js(13.0), Js(12.0), Js(8.0), Js(8.0)]), Js([Js(15.0), Js(15.0), Js(13.0), Js(11.0), Js(9.0), Js(8.0)]), Js([Js(15.0), Js(15.0), Js(13.0), Js(10.0), Js(10.0), Js(8.0)]), Js([Js(15.0), Js(15.0), Js(13.0), Js(10.0), Js(9.0), Js(9.0)]), Js([Js(15.0), Js(15.0), Js(12.0), Js(12.0), Js(9.0), Js(8.0)]), Js([Js(15.0), Js(15.0), Js(12.0), Js(11.0), Js(10.0), Js(8.0)]), Js([Js(15.0), Js(15.0), Js(12.0), Js(11.0), Js(9.0), Js(9.0)]), Js([Js(15.0), Js(15.0), Js(12.0), Js(10.0), Js(10.0), Js(9.0)]), Js([Js(15.0), Js(15.0), Js(11.0), Js(11.0), Js(11.0), Js(8.0)]), Js([Js(15.0), Js(15.0), Js(11.0), Js(11.0), Js(10.0), Js(9.0)]), Js([Js(15.0), Js(15.0), Js(11.0), Js(10.0), Js(10.0), Js(10.0)]), Js([Js(15.0), Js(14.0), Js(14.0), Js(12.0), Js(8.0), Js(8.0)]), Js([Js(15.0), Js(14.0), Js(14.0), Js(11.0), Js(9.0), Js(8.0)]), Js([Js(15.0), Js(14.0), Js(14.0), Js(10.0), Js(10.0), Js(8.0)]), Js([Js(15.0), Js(14.0), Js(14.0), Js(10.0), Js(9.0), Js(9.0)]), Js([Js(15.0), Js(14.0), Js(13.0), Js(13.0), Js(9.0), Js(8.0)]), Js([Js(15.0), Js(14.0), Js(13.0), Js(12.0), Js(10.0), Js(8.0)]), Js([Js(15.0), Js(14.0), Js(13.0), Js(12.0), Js(9.0), Js(9.0)]), Js([Js(15.0), Js(14.0), Js(13.0), Js(11.0), Js(11.0), Js(8.0)]), Js([Js(15.0), Js(14.0), Js(13.0), Js(11.0), Js(10.0), Js(9.0)]), Js([Js(15.0), Js(14.0), Js(13.0), Js(10.0), Js(10.0), Js(10.0)]), Js([Js(15.0), Js(14.0), Js(12.0), Js(12.0), Js(11.0), Js(8.0)]), Js([Js(15.0), Js(14.0), Js(12.0), Js(12.0), Js(10.0), Js(9.0)]), Js([Js(15.0), Js(14.0), Js(12.0), Js(11.0), Js(11.0), Js(9.0)]), Js([Js(15.0), Js(14.0), Js(12.0), Js(11.0), Js(10.0), Js(10.0)]), Js([Js(15.0), Js(14.0), Js(11.0), Js(11.0), Js(11.0), Js(10.0)]), Js([Js(15.0), Js(13.0), Js(13.0), Js(13.0), Js(11.0), Js(8.0)]), Js([Js(15.0), Js(13.0), Js(13.0), Js(13.0), Js(10.0), Js(9.0)]), Js([Js(15.0), Js(13.0), Js(13.0), Js(12.0), Js(12.0), Js(8.0)]), Js([Js(15.0), Js(13.0), Js(13.0), Js(12.0), Js(11.0), Js(9.0)]), Js([Js(15.0), Js(13.0), Js(13.0), Js(12.0), Js(10.0), Js(10.0)]), Js([Js(15.0), Js(13.0), Js(13.0), Js(11.0), Js(11.0), Js(10.0)]), Js([Js(15.0), Js(13.0), Js(12.0), Js(12.0), Js(12.0), Js(9.0)]), Js([Js(15.0), Js(13.0), Js(12.0), Js(12.0), Js(11.0), Js(10.0)]), Js([Js(15.0), Js(13.0), Js(12.0), Js(11.0), Js(11.0), Js(11.0)]), Js([Js(15.0), Js(12.0), Js(12.0), Js(12.0), Js(12.0), Js(10.0)]), Js([Js(15.0), Js(12.0), Js(12.0), Js(12.0), Js(11.0), Js(11.0)]), Js([Js(14.0), Js(14.0), Js(14.0), Js(13.0), Js(9.0), Js(8.0)]), Js([Js(14.0), Js(14.0), Js(14.0), Js(12.0), Js(10.0), Js(8.0)]), Js([Js(14.0), Js(14.0), Js(14.0), Js(12.0), Js(9.0), Js(9.0)]), Js([Js(14.0), Js(14.0), Js(14.0), Js(11.0), Js(11.0), Js(8.0)]), Js([Js(14.0), Js(14.0), Js(14.0), Js(11.0), Js(10.0), Js(9.0)]), Js([Js(14.0), Js(14.0), Js(14.0), Js(10.0), Js(10.0), Js(10.0)]), Js([Js(14.0), Js(14.0), Js(13.0), Js(13.0), Js(11.0), Js(8.0)]), Js([Js(14.0), Js(14.0), Js(13.0), Js(13.0), Js(10.0), Js(9.0)]), Js([Js(14.0), Js(14.0), Js(13.0), Js(12.0), Js(12.0), Js(8.0)]), Js([Js(14.0), Js(14.0), Js(13.0), Js(12.0), Js(11.0), Js(9.0)]), Js([Js(14.0), Js(14.0), Js(13.0), Js(12.0), Js(10.0), Js(10.0)]), Js([Js(14.0), Js(14.0), Js(13.0), Js(11.0), Js(11.0), Js(10.0)]), Js([Js(14.0), Js(14.0), Js(12.0), Js(12.0), Js(12.0), Js(9.0)]), Js([Js(14.0), Js(14.0), Js(12.0), Js(12.0), Js(11.0), Js(10.0)]), Js([Js(14.0), Js(14.0), Js(12.0), Js(11.0), Js(11.0), Js(11.0)]), Js([Js(14.0), Js(13.0), Js(13.0), Js(13.0), Js(13.0), Js(8.0)]), Js([Js(14.0), Js(13.0), Js(13.0), Js(13.0), Js(12.0), Js(9.0)]), Js([Js(14.0), Js(13.0), Js(13.0), Js(13.0), Js(11.0), Js(10.0)]), Js([Js(14.0), Js(13.0), Js(13.0), Js(12.0), Js(12.0), Js(10.0)]), Js([Js(14.0), Js(13.0), Js(13.0), Js(12.0), Js(11.0), Js(11.0)]), Js([Js(14.0), Js(13.0), Js(12.0), Js(12.0), Js(12.0), Js(11.0)]), Js([Js(14.0), Js(12.0), Js(12.0), Js(12.0), Js(12.0), Js(12.0)]), Js([Js(13.0), Js(13.0), Js(13.0), Js(13.0), Js(13.0), Js(10.0)]), Js([Js(13.0), Js(13.0), Js(13.0), Js(13.0), Js(12.0), Js(11.0)]), Js([Js(13.0), Js(13.0), Js(13.0), Js(12.0), Js(12.0), Js(12.0)])]))
    PyJs_LONG_1_()
    var.put('skAbil', Js([Js(1.0), Js(4.0), Js(3.0), Js(0.0), Js(5.0), Js(3.0), Js(4.0), Js(5.0), Js(3.0), Js(4.0), Js(3.0), Js(4.0), Js(5.0), Js(5.0), Js(3.0), Js(1.0), Js(1.0), Js(4.0)]))
    var.put('skOutput', Js(''))
    var.put('abOutput', Js(''))
    var.put('abilIncrease', Js([Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0)]))
    var.put('mySkills', Js([]))
    var.put('expertise', Js([]))
    var.put('armors', Js([Js('Shield'), Js('Padded'), Js('Leather'), Js('Studded Leather'), Js('Hide'), Js('Chain shirt'), Js('Scale mail'), Js('Breastplate'), Js('Half plate'), Js('Ring mail'), Js('Chain mail'), Js('Splint mail'), Js('Plate mail')]))
    var.put('armorAC', Js([Js(2.0), Js(11.0), Js(11.0), Js(12.0), Js(12.0), Js(13.0), Js(14.0), Js(14.0), Js(15.0), Js(14.0), Js(16.0), Js(17.0), Js(18.0)]))
    var.put('weapons', Js([Js('Dagger'), Js('Mace'), Js('Spear'), Js('Handaxe'), Js('Javelin'), Js('Light crossbow'), Js('Heavy crossbow'), Js('Hand crossbow'), Js('Short bow'), Js('Long bow'), Js('Throwing hammer'), Js('Battleaxe'), Js('Greatsword'), Js('Halberd'), Js('Longsword'), Js('Morning Star'), Js('Rapier'), Js('Scimitar'), Js('Shortsword'), Js('Warhammer'), Js('Great Axe'), Js('Dart'), Js('Quarterstaff'), Js('Unarmed Strike'), Js('Sling')]))
    var.put('wpDam', Js([Js('1d4'), Js('1d6'), Js('1d6(1d8)'), Js('1d6'), Js('1d6'), Js('1d8'), Js('1d10'), Js('1d6'), Js('1d6'), Js('1d8'), Js('1d4'), Js('1d8(1d10)'), Js('2d6'), Js('1d10'), Js('1d8(1d10)'), Js('1d8'), Js('1d8'), Js('1d6'), Js('1d6'), Js('1d8(1d10)'), Js('1d12'), Js('1d4'), Js('1d6(1d8)'), Js('1d4'), Js('1d4')]))
    var.put('wpType', Js([Js('piercing'), Js('bludgeoning'), Js('piercing'), Js('slashing'), Js('piercing'), Js('piercing'), Js('piercing'), Js('piercing'), Js('piercing'), Js('piercing'), Js('bludgeoning'), Js('slashing'), Js('slashing'), Js('slashing'), Js('slashing'), Js('piercing'), Js('piercing'), Js('slashing'), Js('piercing'), Js('bludgeoning'), Js('slashing'), Js('piercing'), Js('bludgeoning'), Js('bludgeoning'), Js('bludgeoning')]))
    var.put('wpRange', Js([Js(4.0), Js(0.0), Js(3.0), Js(3.0), Js(3.0), Js(2.0), Js(2.0), Js(2.0), Js(2.0), Js(2.0), Js(3.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(1.0), Js(1.0), Js(1.0), Js(0.0), Js(0.0), Js(2.0), Js(0.0), Js(1.0), Js(2.0)]))
    var.put('wpDistance', Js([Js('20/60'), Js(''), Js('20/60'), Js('20/60'), Js('30/120'), Js('80/320'), Js('100/400'), Js('30/120'), Js('80/320'), Js('150/600'), Js('20/60'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('20/60'), Js(''), Js(''), Js('30/120')]))
    var.put('wpNum', Js([Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0)]))
    var.put('maneuvers', Js([Js("Commander's Strike"), Js('Disarming Attack'), Js('Distracting Strike'), Js('Evasive Footwork'), Js('Feinting Attack'), Js('Goading Attack'), Js('Lunging Attack'), Js('Maneuvering Attack'), Js('Menacing Attack'), Js('Parry'), Js('Precision Attack'), Js('Pushing Attack'), Js('Rally'), Js('Riposte'), Js('Sweeping Attack'), Js('Trip Attack')]))
    var.put('meta', Js([Js('Careful Spell'), Js('Distant Spell'), Js('Empowered Spell'), Js('Extended Spell'), Js('Heightened Spell'), Js('Quickened Spell'), Js('Subtle Spell'), Js('Twinned Spell')]))
    var.put('eldritch', Js([Js('Agonizing Blast'), Js('Armor of Shadows'), Js('Beast Speech'), Js('Beguiling Influence'), Js("Devil's Sight"), Js('Eldritch Sight'), Js('Eldritch Spear'), Js('Eyes of the Rune Keeper'), Js('Fiendish Vigor'), Js('Gaze of Two Minds'), Js('Mask of Many Faces'), Js('Misty Visions'), Js('Repelling Blast'), Js('Thief of Five Fates')]))
    var.put('tome', Js(False))
    var.put('waTome', Js([]))
    var.put('waTomeRituals', Js([]))
    var.put('artisans', Js([Js('Alchemist'), Js('Armorer'), Js('Brewer'), Js('Calligrapher'), Js('Carpenter'), Js('Cartographer'), Js('Cobbler'), Js('Cook'), Js('Glassblower'), Js('Jeweler'), Js('Leatherworker'), Js('Mason'), Js('Painter'), Js('Potter'), Js('Shipwright'), Js('Smith'), Js('Tinker'), Js('Wagon-maker'), Js('Weaver'), Js('Woodcarver')]))
    var.put('eblast', Js(False))
    var.put('familiar', Js(''))
    var.put('familiars', Js([Js('Bat'), Js('Bat'), Js('Cat'), Js('Cat'), Js('Cat'), Js('Crab'), Js('Frog (toad)'), Js('Hawk'), Js('Hawk'), Js('Lizard'), Js('Octopus'), Js('Owl'), Js('Owl'), Js('Owl'), Js('Poisonous Snake'), Js('Fish (quipper)'), Js('Rat'), Js('Rat'), Js('Rat'), Js('Raven'), Js('Raven'), Js('Raven'), Js('Sea Horse'), Js('Spider'), Js('Weasel'), Js('Weasel')]))
    var.put('enemies', Js([Js('Aberrations'), Js('Beasts'), Js('Celestials'), Js('Constructs'), Js('Dragons'), Js('Elementals'), Js('Fey'), Js('Fiends'), Js('Giants'), Js('Monstrosities'), Js('Oozes'), Js('Plants'), Js('Undead')]))
    var.put('enLangs', Js([Js(''), Js(''), Js('Celestial'), Js(''), Js('Draconic'), Js('Primordial'), Js('Sylvan'), Js(''), Js('Giant'), Js(''), Js(''), Js(''), Js('')]))
    var.put('humanoids', Js([Js('Orcs'), Js('Goblins'), Js('Kobolds'), Js('Bugbears'), Js('Hobgoblins'), Js('Gnolls')]))
    var.put('humLangs', Js([Js('Orc'), Js('Goblin'), Js('Draconic'), Js('Goblin'), Js('Goblin'), Js('Gnoll')]))
    var.put('companions', Js([Js('Boar'), Js('Panther'), Js('Wolf'), Js('Giant Badger'), Js('Giant Poisonous Snake')]))
    var.put('companionsStats', Js([Js('<i>Charge, Relentless</i>, Tusk +'), Js('<i>Keen Smell, Pounce,</i> Bite +'), Js('<i>Keen Hearing and Smell, Pack Tactics,</i> Bite +'), Js('<i>Keen Smell, Multiattack,</i> Bite +'), Js('<i>Blindsight 10 ft,</i> Bite +')]))
    var.put('companionshp', Js([Js(11.0), Js(13.0), Js(11.0), Js(13.0), Js(11.0)]))
    var.put('companionsAC', Js([Js(11.0), Js(12.0), Js(13.0), Js(10.0), Js(14.0)]))
    var.put('companionsAttack1', Js([Js(3.0), Js(4.0), Js(4.0), Js(3.0), Js(6.0)]))
    var.put('companionsDamage1', Js([Js('1d6'), Js('1d6'), Js('2d4'), Js('1d6'), Js('1d4')]))
    var.put('companionsDamageBonus', Js([Js(1.0), Js(2.0), Js(2.0), Js(1.0), Js(4.0)]))
    var.put('companionsDamageExtra', Js([Js(''), Js(''), Js(' and roll to  knock prone'), Js(''), Js(' and 3d6 poison dmg')]))
    var.put('companionsAttack2', Js([Js(0.0), Js(4.0), Js(0.0), Js(3.0), Js(0.0)]))
    var.put('companionsAttackText2', Js([Js(''), Js('Claw'), Js(''), Js('Claws'), Js('')]))
    var.put('companionsAttackDamage2', Js([Js(''), Js('1d4'), Js(''), Js('2d4'), Js('')]))
    var.put('companionsDamageBonus2', Js([Js(0.0), Js(2.0), Js(0.0), Js(1.0), Js(0.0)]))
    var.put('music', Js([Js('Lute'), Js('Flute'), Js('Harp'), Js('Fiddle'), Js('Pipes'), Js('Drums'), Js('Bagpipes'), Js('Dulcimer'), Js('Lyre'), Js('Horn'), Js('Guitar'), Js('Pan flute'), Js('Shawm'), Js('Viol')]))
    var.put('gaming', Js([Js('Dice games'), Js('Dragonchess'), Js('Playing cards'), Js('Three-Dragon Ante')]))
    var.put('valuables', Js([Js('Gold Nugget'), Js('Gold Figurine'), Js('Silver Cutlery'), Js('Bag of Gold Dust'), Js('Jeweled Helmet'), Js('Jeweled Dagger'), Js('Rare Book'), Js('Rare Map'), Js('Silver Wand'), Js('Jeweled Copper Helmet'), Js('Silver Ring'), Js('Silver Jewelry Box'), Js('Jeweled Copper Bracelet'), Js('Finely-crafted Copper Necklace'), Js('Rare Hunting Trophy'), Js('Engraved Silver Plate'), Js('Engraved Silver Holy Symbol'), Js('Jeweled Copper Holy Symbol'), Js('Silver Tobacco Box'), Js('Silver and Leather Bound Book'), Js('Gold and Leather Bound Book'), Js('Pieces of Plate Mail'), Js('Silver Chain'), Js('Finely-crafted Silk Robe'), Js('Silver Dice'), Js('Golden Dice'), Js('Finely-crafted Silver and Leather Shoes'), Js('Bottle of Rare Wine'), Js('Leather and Silver Quiver'), Js('Gold Belt Buckle'), Js('Dragonchess Set with Silver Pieces'), Js('Gold Dragonchess Pieces'), Js('Finely-crafted Viol'), Js('Finely-crafted Lute'), Js('Collection of Rare Coins'), Js('Exceptional Painting'), Js('Pearl'), Js('Pearl'), Js('Rare Gold and Silk Military Medal'), Js('Finely-crafted Crystal Slop Bucket'), Js('Silver Ceremonial Dagger'), Js('Half of a severely burned, barely legible spellbook'), Js('Silver and Wood Ceremonial Mask'), Js('Gold and Wood Longstemmed Pipe'), Js('Small Gold Bell'), Js('Arrow Made of Gold'), Js('Silver Clockwork Toy'), Js('Small gem'), Js('Small gem'), Js('Small gem'), Js('Diamond'), Js('Bag of Very Rare Herbs'), Js('Small Gold Framed Mirror')]))
    var.put('jewelry', Js([Js('Ring'), Js('Necklace'), Js('Pendant'), Js('Bracelets'), Js('Bracers'), Js('Tiara'), Js('Earrings'), Js('Amulet'), Js('Chalice'), Js('Ornamental Dagger'), Js('Bowl'), Js('Statuette'), Js('Goblet'), Js('Crown'), Js('Flute'), Js('Holy Symbol'), Js('and Wood Hand Crossbow'), Js('Ceremonial Saber'), Js('and Wood Lute'), Js('and Wood Staff'), Js('and Wood Dragonchess Set'), Js('Hourglass'), Js('Pitcher'), Js('Medallion'), Js('Harp'), Js('Scepter'), Js('Drinking Horn'), Js('Gnome Music Box')]))
    var.put('jewelryAdjectives', Js([Js('Finely-crafted Gold'), Js('Gold'), Js('Jeweled Gold'), Js('Finely-crafted Silver'), Js('Jeweled Copper'), Js('Jeweled Silver'), Js('Jeweled Electrum'), Js('Silver and Ivory')]))
    var.put('jewelryRare', Js([Js('Ring'), Js('Necklace'), Js('Amulet'), Js('Chalice'), Js('Crown'), Js('Tiara'), Js('Goblet'), Js('Pendant'), Js('Ornamental Dagger'), Js('Scepter')]))
    var.put('jewelryAdjectivesRare', Js([Js('Platinum'), Js('Jeweled Gold'), Js('Jeweled Platinum'), Js('Diamond and Silver'), Js('Platinum and Ruby'), Js('Gold and Ruby'), Js('Gold and Sapphire')]))
    var.put('magicUncommon', Js([Js('Bag of Holding'), Js('Boots of Striding and Springing'), Js('Cloak of Elvenkind'), Js('Gloves of Swimming and Climbing'), Js('Goggles of Night'), Js("Keoghtom's Ointment"), Js('Wand of Magic Detection (3 charges)'), Js('Wand of Magic Missiles (7 charges)')]))
    var.put('magicRare', Js([Js('Ring of Evasion (3 charges)'), Js('Ring of Protection'), Js('Ring of Resistance')]))
    var.put('magicVeryRare', Js([Js('Potion of Flying'), Js('Potion of Invisibility'), Js('Potion of Vitality')]))
    var.put('poisonUncommon', Js([Js('Assassin’s blood (Ingested)'), Js('Carrion crawler mucus  (Contact)'), Js('Drow poison  (Injury)'), Js('Essence of ether  (Inhaled)'), Js('Malice  (Inhaled)'), Js('Pale tincture  (Ingested)'), Js('Serpent venom  (Injury)'), Js('Truth serum  (Ingested)')]))
    var.put('Rare', Js([Js('Torpor  (Ingested)'), Js('Burnt othur fumes  (Inhaled)'), Js('Oil of taggit  (Contact)')]))
    var.put('VeryRare', Js([Js('Wyvern  poison (Injury)'), Js('Purple worm poison (Injury)'), Js('Midnight tears  (Ingested)')]))
    var.put('magicWeapon', Js(0.0))
    var.put('bootsOfSS', Js(False))
    var.put('magicArmor', Js(0.0))
    var.put('ringStone', Js([Js('Pearl'), Js('Tourmaline'), Js('Garnet'), Js('Sapphire'), Js('Citrine'), Js('Jet'), Js('Amethyst'), Js('Jade'), Js('Topaz'), Js('Spinel')]))
    var.put('ringResistance', Js([Js('Acid'), Js('Cold'), Js('Fire'), Js('Force'), Js('Lightning'), Js('Necrotic'), Js('Poison'), Js('Psychic'), Js('Radiant'), Js('Thunder')]))
    var.put('ringProtection', Js(0.0))
    var.put('companion', (-Js(1.0)))
    var.put('myMusic', Js([]))
    var.put('myInstrument', Js(''))
    var.put('favored', Js(''))
    var.put('aarName', Js([Js('Aera'), Js('Aial'), Js('Aur'), Js('Deekek'), Js('Errk'), Js('Heehk'), Js('Ikki'), Js('Kleeck'), Js('Oorr'), Js('Ouss'), Js('Quaf'), Js('Quierk'), Js('Salleek'), Js('Urreek'), Js('Zeed')]))
    var.put('gnomeNameM', Js([Js('Alston'), Js('Alvyn'), Js('Boddynock'), Js('Brocc'), Js('Burgell'), Js('Dimble'), Js('Eldon'), Js('Erky'), Js('Fonkin'), Js('Frug'), Js('Gerbo'), Js('Gimble'), Js('Glim'), Js('Jebeddo'), Js('Kellen'), Js('Namfoodle'), Js('Orryn'), Js('Roondar'), Js('Seebo'), Js('Sindri'), Js('Warryn'), Js('Wrenn'), Js('Zook')]))
    var.put('gnomeNameF', Js([Js('Bimpnottin'), Js('Breena'), Js('Caramip'), Js('Carlin'), Js('Donella'), Js('Duvamil'), Js('Ella'), Js('Ellyjobell'), Js('Ellywick'), Js('Lilli'), Js('Loopmottin'), Js('Lorilla'), Js('Mardnab'), Js('Nissa'), Js('Nyx'), Js('Oda'), Js('Orla'), Js('Roywyn'), Js('Shamil'), Js('Tana'), Js('Waywocket'), Js('Zanna')]))
    var.put('gnomeNameLast', Js([Js('Beren'), Js('Daergel'), Js('Folkor'), Js('Garrick'), Js('Nackle'), Js('Murnig'), Js('Ningel'), Js('Raulnor'), Js('Scheppen'), Js('Timbers'), Js('Turen')]))
    var.put('gnomeNicknames', Js([Js('Aleslosh'), Js('Ashhearth'), Js('Badger'), Js('Cloak'), Js('Doublelock'), Js('Filchbatter'), Js('Fnipper'), Js('Ku'), Js('Nim'), Js('Oneshoe'), Js('Pock'), Js('Sparklegem'), Js('Stumbleduck')]))
    var.put('deepGnomeNameM', Js([Js('Belwar'), Js('Brickers'), Js('Durthmeck'), Js('Firble'), Js('Krieger'), Js('Kronthud'), Js('Schneltheck'), Js('Schnicktick'), Js('Thulwar'), Js('Walschud')]))
    var.put('deepGnomeNameF', Js([Js('Beliss'), Js('Durthee'), Js('Frickarti'), Js('Ivridda'), Js('Krivi'), Js('Lulthiss'), Js('Nalvarti'), Js('Schnella'), Js('Thulmarra'), Js('Wirsidda')]))
    var.put('deepGnomeNameLast', Js([Js('Crystalfist'), Js('Gemcutter'), Js('Ironfoot'), Js('Rockhewer'), Js('Seamfinder'), Js('Stonecutter')]))
    var.put('goliathNameBirth', Js([Js('Aukan'), Js('Eglath'), Js('Gae-Al'), Js('Gauthak'), Js('Ilikan'), Js('Keothi'), Js('Kuori'), Js('Lo-Kag'), Js('Manneo'), Js('Maveith'), Js('Nalla'), Js('Orilo'), Js('Paavu'), Js('Pethani'), Js('Thalai'), Js('Thotham'), Js('Uthal'), Js('Vauea'), Js('Vimak')]))
    var.put('goliathNameNick', Js([Js('Bearkiller'), Js('Dawncaller'), Js('Fearless'), Js('Flintfinder'), Js('Horncarver'), Js('Keeneye'), Js('Lonehunter'), Js('Longleaper'), Js('Rootsmasher'), Js('Skywatcher'), Js('Steadyhand'), Js('Threadtwister'), Js('Twice-Orphaned'), Js('Twistedlimb'), Js('Wordpainter')]))
    var.put('goliathNameClan', Js([Js('Anakalathai'), Js('Elanithino'), Js('Gathakanathi'), Js('Kalagiano'), Js('Katho-Olavi'), Js('Kolae-Gileana'), Js('Ogolakanu'), Js('Thuliaga'), Js('Thunukalathi'), Js('Vaimei-Laga')]))
    def PyJs_LONG_2_(var=var):
        return var.put('humanNameM', Js([Js('Ander'), Js('Blath'), Js('Bran'), Js('Frath'), Js('Geth'), Js('Lander'), Js('Luth'), Js('Malcer'), Js('Stor'), Js('Taman'), Js('Urth'), Js('Aseir'), Js('Bardeid'), Js('Haseid'), Js('Khemed'), Js('Mehmen'), Js('Sudeiman'), Js('Zasheir'), Js('Bor'), Js('Fodel'), Js('Glar'), Js('Grigor'), Js('Igan'), Js('Ivor'), Js('Kosef'), Js('Mival'), Js('Orel'), Js('Pavel'), Js('Sergor')]))
    PyJs_LONG_2_()
    var.put('humanNameF', Js([Js('Amafrey'), Js('Betha'), Js('Cefrey'), Js('Kethra'), Js('Mara'), Js('Olga'), Js('Silifrey'), Js('Westra'), Js('Atala'), Js('Ceidil'), Js('Hama'), Js('Jasmal'), Js('Meilil'), Js('Seipora'), Js('Yasheira'), Js('Zasheida'), Js('Alethra'), Js('Kara'), Js('Katernin'), Js('Mara'), Js('Natali'), Js('Olma'), Js('Tana'), Js('Zora')]))
    var.put('humanNameLast', Js([Js('Brightwood'), Js('Helder'), Js('Hornraven'), Js('Lackman'), Js('Stormwind'), Js('Windrivver'), Js('Basha'), Js('Dumein'), Js('Jassan'), Js('Khalid'), Js('Mostana'), Js('Pashar'), Js('Rein'), Js('Bersk'), Js('Chernin'), Js('Dotsk'), Js('Kulenov'), Js('Marsk'), Js('Nemetsk'), Js('Shemov'), Js('Starag')]))
    var.put('orcNameM', Js([Js('Dench'), Js('Feng'), Js('Gell'), Js('Henk'), Js('Holg'), Js('Imsh'), Js('Keth'), Js('Krusk'), Js('Mhurren'), Js('Ront'), Js('Shump'), Js('Thokk')]))
    var.put('orcNameF', Js([Js('Baggi'), Js('Emen'), Js('Engong'), Js('Kansif'), Js('Myev'), Js('Neega'), Js('Ovak'), Js('Ownka'), Js('Shautha'), Js('Sutha'), Js('Vola'), Js('Volen'), Js('Yevelda')]))
    var.put('tieflingNameM', Js([Js('Akmenos'), Js('Amnon'), Js('Barakas'), Js('Damakos'), Js('Ekemon'), Js('Iados'), Js('Kairon'), Js('Leucis'), Js('Melech'), Js('Mordai'), Js('Morthos'), Js('Pelaios'), Js('Skamos'), Js('Therai')]))
    var.put('tieflingNameF', Js([Js('Akta'), Js('Anakis'), Js('Bryseis'), Js('Criella'), Js('Damaia'), Js('Ea'), Js('Kallista'), Js('Lerissa'), Js('Makaria'), Js('Nemeia'), Js('Orianna'), Js('Phelaia'), Js('Rieta')]))
    var.put('tieflingNameLast', Js([Js('Art'), Js('Carrion'), Js('Chant'), Js('Creed'), Js('Despair'), Js('Excellence'), Js('Fear'), Js('Glory'), Js('Hope'), Js('Ideal'), Js('Music'), Js('Nowhere'), Js('Open'), Js('Poetry'), Js('Quest'), Js('Random'), Js('Reverence'), Js('Sorrow'), Js('Temerity'), Js('Torment'), Js('Weary')]))
    var.put('dragonNameM', Js([Js('Arjhan'), Js('Balasar'), Js('Bharash'), Js('Donaar'), Js('Ghesh'), Js('Heskan'), Js('Kriv'), Js('Medrash'), Js('Mehen'), Js('Nadarr'), Js('Pandjed'), Js('Patrin'), Js('Rhogar'), Js('Shamash'), Js('Shedinn'), Js('Tarhun'), Js('Torinn')]))
    var.put('dragonNameF', Js([Js('Akra'), Js('Biri'), Js('Daar'), Js('Farideh'), Js('Harann'), Js('Flavilar'), Js('Jheri'), Js('Kava'), Js('Korinn'), Js('Mishann'), Js('Nala'), Js('Perra'), Js('Raiann'), Js('Sora'), Js('Surina'), Js('Thava'), Js('Uadjit')]))
    var.put('dragonNameLast', Js([Js('Clethtinthiallor'), Js('Daardendrian'), Js('Delmirev'), Js('Drachedandion'), Js('Fenkenkabradon'), Js('Kepeshkmolik'), Js('Kerrhylon'), Js('Kimbatuul'), Js('inxakasendalor'), Js('Myastan'), Js('Nemmonis'), Js('Norixius'), Js('Ophinshtalajiir'), Js('Prexijandilin'), Js('Shestendeliath'), Js('Turnuroth'), Js('Verthisathurgiesh'), Js('Yarjerit')]))
    var.put('halfNameM', Js([Js('Alton'), Js('Ander'), Js('Cade'), Js('Corrin'), Js('Eldon'), Js('Errich'), Js('Finnan'), Js('Garret'), Js('Lindal'), Js('Lyle'), Js('Merric'), Js('Milo'), Js('Osborn'), Js('Perrin'), Js('Reed'), Js('Roscoe'), Js('Wellby')]))
    var.put('halfNameF', Js([Js('Andry'), Js('Bree'), Js('Callie'), Js('Cora'), Js('Euphemia'), Js('Jillian'), Js('Kithri'), Js('Lavinia'), Js('Lidda'), Js('Merla'), Js('Nedda'), Js('Paela'), Js('Portia'), Js('Seraphina'), Js('Shaena'), Js('Trym'), Js('Vani'), Js('Verna')]))
    var.put('halfNameLast', Js([Js('Brushgather'), Js('Goodbarrel'), Js('Greenbottle'), Js('High-hill'), Js('Hilltopple'), Js('Leagallow'), Js('Tealeaf'), Js('Thorngage'), Js('Tosscobble'), Js('Underbough')]))
    def PyJs_LONG_3_(var=var):
        return var.put('elfNameM', Js([Js('Adran'), Js('Aelar'), Js('Aramil'), Js('Arannis'), Js('Aust'), Js('Beiro'), Js('Berrian'), Js('Carric'), Js('Enialis'), Js('Erdan'), Js('Erevan'), Js('Galinndan'), Js('Hadarai'), Js('Heian'), Js('Himo'), Js('Immeral'), Js('Ivellios'), Js('Laucian'), Js('Mindartis'), Js('Paelias'), Js('Peren'), Js('Quarion'), Js('Riardon'), Js('Rolen'), Js('Soveliss'), Js('Thamior'), Js('Tharivol'), Js('Theren'), Js('Varis')]))
    PyJs_LONG_3_()
    def PyJs_LONG_4_(var=var):
        return var.put('elfNameF', Js([Js('Adrie'), Js('Althaea'), Js('Anastrianna'), Js('Andraste'), Js('Antinua'), Js('Bethrynna'), Js('Birel'), Js('Caelynn'), Js('Drusilia'), Js('Enna'), Js('Felosial'), Js('Ielenia'), Js('Jelenneth'), Js('Keyleth'), Js('Leshanna'), Js('Lia'), Js('Meriele'), Js('Mialee'), Js('Naivara'), Js('Quelenna'), Js('Quillathe'), Js('Sariel'), Js('Shanairra'), Js('Shava'), Js('Silaqui'), Js('Theirastra'), Js('Thia'), Js('Vadania'), Js('Valanthe'), Js('Xanaphia')]))
    PyJs_LONG_4_()
    var.put('elfNameLast', Js([Js('Amakiir (Gemflower)'), Js('Amastacia (Starflower)'), Js('Galanodel (Moonwhisper)'), Js('Holimion (Diamonddew)'), Js('Ilphelkiir (Gemblossom)'), Js('Liadon (Silverfrond)'), Js('Meliamne (Oakenheel)'), Js("Nai'lo (Nightbreeze)"), Js('Siannodel (Moonbrook)'), Js('Xiloscient (Goldpetal)')]))
    def PyJs_LONG_5_(var=var):
        return var.put('dwarfNameM', Js([Js('Adrik'), Js('Alberich'), Js('Baern'), Js('Barendd'), Js('Brottor'), Js('Bruenor'), Js('Dain'), Js('Darrak'), Js('Delg'), Js('Eberk'), Js('Einkil'), Js('Fargrim'), Js('Flint'), Js('Gardain'), Js('Harbek'), Js('Kildrak'), Js('Morgran'), Js('Orsik'), Js('Oskar'), Js('Rangrim'), Js('Rurik'), Js('Taklinn'), Js('Thoradin'), Js('Thorin'), Js('Tordek'), Js('Traubon'), Js('Travok'), Js('Ulfgar'), Js('Veit'), Js('Vondal')]))
    PyJs_LONG_5_()
    var.put('dwarfNameF', Js([Js('Amber'), Js('Artin'), Js('Audhild'), Js('Bardryn'), Js('Dagnal'), Js('Diesa'), Js('Eldeth'), Js('Falkrunn'), Js('Finellen'), Js('Gunnloda'), Js('Gurdis'), Js('Helja'), Js('Hlin'), Js('Kathra'), Js('Kristryd'), Js('Ilde'), Js('Liftrasa'), Js('Mardred'), Js('Riswynn'), Js('Sannl'), Js('Torbera'), Js('Torgga'), Js('Vistra')]))
    var.put('dwarfNameLast', Js([Js('Balderk'), Js('Battlehammer'), Js('Brawnanvil'), Js('Dankil'), Js('Fireforge'), Js('Frostbeard'), Js('Gorunn'), Js('Holderhek'), Js('Ironfist'), Js('Loderr'), Js('Lutgehr'), Js('Rumnaheim'), Js('Strakeln'), Js('Torunn'), Js('Ungart')]))
    var.put('name', Js(''))
    var.put('gender', (-Js(1.0)))
    var.put('myWp', Js([]))
    var.put('myAr', Js([]))
    var.put('wpOutput', Js(''))
    var.put('wrOutput', Js(''))
    var.put('arOutput', Js(''))
    var.put('spOutput', Js(''))
    var.put('cOutput', Js(''))
    var.put('bgOutput', Js(''))
    var.put('toOutput', Js(''))
    var.put('mySpells', Js([]))
    var.put('myCantrips', Js([]))
    var.put('bg', Js(0.0))
    var.put('eqOutput', Js(''))
    var.put('weOutput', Js(''))
    var.put('maOutput', Js(''))
    var.put('poOutput', Js(''))
    var.put('temp', Js(''))
    var.put('tempSpells', Js([]))
    var.put('sp1', Js(0.0))
    var.put('sp2', Js(0.0))
    var.put('sp3', Js(0.0))
    var.put('sp4', Js(0.0))
    var.put('sp5', Js(0.0))
    var.put('tempAr', Js([]))
    var.put('st', Js([]))
    var.put('saves', Js([]))
    var.put('bool', Js(False))
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    var.put('gender', (var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(2.0)))+Js(1.0)))
    if (var.get('forceGender')>Js(0.0)):
        var.put('gender', var.get('forceGender'))
    var.put('rollOutput', Js(''))
    var.put('abilRaw', Js([Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0)]))
    var.put('lowest', (-Js(1.0)))
    var.put('bool', Js(False))
    var.put('sum', Js(0.0))
    if (var.get('magicGet')(Js('genMethod'), var.get('possibile')).get('value')==Js('1')):
        var.put('abilRaw', Js([]))
        var.put('x', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('allArrays').get('length'))))
        var.put('abilRaw', var.get('allArrays').get(var.get('x')))
        var.get('console').callprop('log', (Js('Array picked = ')+var.get('abilRaw')))
        var.put('rollOutput', (Js('Random array:  ')+var.get('abilRaw')), '+')
    else:
        if (var.get('magicGet')(Js('genMethod'), var.get('possibile')).get('value')==Js('2')):
            var.put('abilRaw', Js([]))
            var.get('abilRaw').callprop('unshift', (var.get('magicGet')(Js('a1')).get('value')*Js(1.0)))
            var.get('abilRaw').callprop('unshift', (var.get('magicGet')(Js('a2')).get('value')*Js(1.0)))
            var.get('abilRaw').callprop('unshift', (var.get('magicGet')(Js('a3')).get('value')*Js(1.0)))
            var.get('abilRaw').callprop('unshift', (var.get('magicGet')(Js('a4')).get('value')*Js(1.0)))
            var.get('abilRaw').callprop('unshift', (var.get('magicGet')(Js('a5')).get('value')*Js(1.0)))
            var.get('abilRaw').callprop('unshift', (var.get('magicGet')(Js('a6')).get('value')*Js(1.0)))
            @Js
            def PyJs_anonymous_9_(a, b, this, arguments, var=var):
                var = Scope({'this':this, 'a':a, 'b':b, 'arguments':arguments}, var)
                var.registers(['a', 'b'])
                return (var.get('b')-var.get('a'))
            PyJs_anonymous_9_._set_name('anonymous')
            var.get('abilRaw').callprop('sort', PyJs_anonymous_9_)
        else:
            if (var.get('magicGet')(Js('genMethod'), var.get('possibile')).get('value')==Js('3')):
                var.get('abil').put('0', (var.get('magicGet')(Js('a1')).get('value')*Js(1.0)))
                var.get('abil').put('1', (var.get('magicGet')(Js('a2')).get('value')*Js(1.0)))
                var.get('abil').put('2', (var.get('magicGet')(Js('a3')).get('value')*Js(1.0)))
                var.get('abil').put('3', (var.get('magicGet')(Js('a4')).get('value')*Js(1.0)))
                var.get('abil').put('4', (var.get('magicGet')(Js('a5')).get('value')*Js(1.0)))
                var.get('abil').put('5', (var.get('magicGet')(Js('a6')).get('value')*Js(1.0)))
            else:
                var.put('rollOutput', Js('<b>Proficient skills:</b>  ==EOF=='), '+')
                var.put('y', Js(0.0))
                var.put('z', Js(65.0))
                if (var.get('forceAbil')>Js(0.0)):
                    var.put('z', var.get('forceAbil'))
                while (var.get('bool')==Js(False)):
                    (var.put('y',Js(var.get('y').to_number())+Js(1))-Js(1))
                    var.put('i', Js(0.0))
                    #for JS loop
                    var.put('x', Js(0.0))
                    while (var.get('x')<Js(6.0)):
                        try:
                            var.get('abilRaw').put(var.get('x'), var.get('genAbil')())
                            var.put('i', var.get('abilRaw').get(var.get('x')), '+')
                        finally:
                                (var.put('x',Js(var.get('x').to_number())+Js(1))-Js(1))
                    var.put('sum', var.get('i'), '+')
                    @Js
                    def PyJs_anonymous_10_(a, b, this, arguments, var=var):
                        var = Scope({'this':this, 'a':a, 'b':b, 'arguments':arguments}, var)
                        var.registers(['a', 'b'])
                        return (var.get('b')-var.get('a'))
                    PyJs_anonymous_10_._set_name('anonymous')
                    var.get('abilRaw').callprop('sort', PyJs_anonymous_10_)
                    if (var.get('i')>var.get('z')):
                        var.put('bool', Js(True))
                    else:
                        var.put('rollOutput', ((((Js('adds up to ')+var.get('i'))+Js(' ('))+var.get('abilRaw'))+Js(')!  Starting over!  ')), '+')
                var.get('console').callprop('log', var.get('rollOutput'))
                var.get('console').callprop('log', (var.get('y')+Js(' rolls to get an acceptable sum')))
                var.get('console').callprop('log', (Js('average roll = ')+(var.get('sum')/var.get('y'))))
    var.put('exotic', var.get('Math').callprop('floor', ((var.get('Math').callprop('random')*Js(4.0))+Js(1.0))))
    if ((var.get('forceRace')>Js(9.0)) and (var.get('forceRace')<Js(21.0))):
        var.put('exotic', Js(0.0))
    else:
        if (var.get('forceRace')>Js(0.0)):
            var.put('exotic', Js(1.0))
    var.put('racetxt', Js(''))
    if (var.get('exotic')==Js(1.0)):
        var.put('abOutput', Js('<b>Racial Traits:</b> '), '+')
        var.put('ra', var.get('Math').callprop('floor', ((var.get('Math').callprop('random')*Js(14.0))+Js(1.0))))
        if (var.get('ra')>Js(7.0)):
            var.put('ra', Js(13.0), '+')
        if (var.get('forceRace')>Js(0.0)):
            var.put('ra', var.get('forceRace'))
        while 1:
            SWITCHED = False
            CONDITION = (var.get('ra'))
            if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
                SWITCHED = True
                var.put('racetxt', Js('Dragonborn'))
                var.get('abil').put('0', Js(2.0), '+')
                var.get('abil').put('5', Js(1.0), '+')
                var.put('languageOutput', Js('Common, Draconic'))
                var.put('speed', Js(30.0))
                var.put('dragType', Js(''))
                var.put('elemType', Js(''))
                var.put('tempAr', var.get('dragon')())
                var.put('dragType', var.get('tempAr').get('0'))
                var.put('elemType', var.get('tempAr').get('1'))
                var.put('breathType', var.get('tempAr').get('2'))
                var.put('abOutput', ((((((((Js('Draconic Ancestry (')+var.get('dragType'))+Js('), Breath Weapon ('))+var.get('elemType'))+Js(' damage in a '))+var.get('breathType'))+Js('), Damage Resistance ('))+var.get('elemType'))+Js(')')), '+')
                if (var.get('gender')==Js(2.0)):
                    var.put('name', var.get('dragonNameF').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('dragonNameF').get('length')))))
                else:
                    var.put('name', var.get('dragonNameM').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('dragonNameM').get('length')))))
                var.put('name', (Js(' ')+var.get('dragonNameLast').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('dragonNameLast').get('length'))))), '+')
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                SWITCHED = True
                var.put('racetxt', Js('Forest Gnome'))
                var.get('abil').put('3', Js(2.0), '+')
                var.get('abil').put('1', Js(1.0), '+')
                var.put('languageOutput', Js('Common, Gnomish'))
                var.put('speed', Js(25.0))
                var.put('size', Js('Small'))
                var.put('abOutput', Js('Darkvision, Gnome Cunning, Natural Illusionist, Speak with Small Animals'), '+')
                var.get('raceSpells').callprop('push', Js('Minor Illusion'))
                var.put('raceSpellAbility', Js(3.0))
                if (var.get('gender')==Js(2.0)):
                    var.put('name', var.get('gnomeNameF').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('gnomeNameF').get('length')))))
                else:
                    var.put('name', var.get('gnomeNameM').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('gnomeNameM').get('length')))))
                var.put('name', (((Js(' "')+var.get('gnomeNicknames').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('gnomeNicknames').get('length')))))+Js('" '))+var.get('gnomeNameLast').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('gnomeNameLast').get('length'))))), '+')
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js(3.0)):
                SWITCHED = True
                var.put('racetxt', Js('Half-Elf'))
                var.get('abil').put('5', Js(2.0), '+')
                var.put('languageOutput', Js('Common, Elvish'))
                var.put('speed', Js(30.0))
                var.put('moreLang', Js(1.0))
                var.put('abOutput', Js('Darkvision, Fey Ancestry, 2 skills'), '+')
                var.put('mySkills', Js([]))
                if (var.get('Math').callprop('random')>Js(0.5)):
                    if (var.get('gender')==Js(2.0)):
                        var.put('name', var.get('humanNameF').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('humanNameF').get('length')))))
                    else:
                        var.put('name', var.get('humanNameM').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('humanNameM').get('length')))))
                    var.put('name', (Js(' ')+var.get('humanNameLast').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('humanNameLast').get('length'))))), '+')
                else:
                    if (var.get('gender')==Js(2.0)):
                        var.put('name', var.get('elfNameF').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('elfNameF').get('length')))))
                    else:
                        var.put('name', var.get('elfNameM').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('elfNameM').get('length')))))
                    var.put('name', (Js(' ')+var.get('elfNameLast').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('elfNameLast').get('length'))))), '+')
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js(4.0)):
                SWITCHED = True
                var.put('racetxt', Js('Half-Orc'))
                var.get('abil').put('0', Js(2.0), '+')
                var.get('abil').put('2', Js(1.0), '+')
                var.put('speed', Js(30.0))
                var.put('languageOutput', Js('Common, Orc'))
                var.get('skLearn').put('7', Js(True))
                var.get('mySkills').callprop('push', Js(7.0))
                var.put('abOutput', Js('Darkvision, Menacing (Intimidate skill), Relentless Endurance, Savage Attack'), '+')
                if (var.get('Math').callprop('random')>Js(0.5)):
                    if (var.get('gender')==Js(2.0)):
                        var.put('name', var.get('orcNameF').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('orcNameF').get('length')))))
                    else:
                        var.put('name', var.get('orcNameM').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('orcNameM').get('length')))))
                else:
                    if (var.get('gender')==Js(2.0)):
                        var.put('name', var.get('humanNameF').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('humanNameF').get('length')))))
                    else:
                        var.put('name', var.get('humanNameM').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('humanNameM').get('length')))))
                var.put('name', (Js(' ')+var.get('humanNameLast').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('humanNameLast').get('length'))))), '+')
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js(5.0)):
                SWITCHED = True
                var.put('racetxt', Js('Tiefling'))
                var.get('abil').put('3', Js(1.0), '+')
                var.get('abil').put('5', Js(2.0), '+')
                var.put('speed', Js(30.0))
                var.put('languageOutput', Js('Common, Infernal'))
                var.put('abOutput', Js('Darkvision, Hellish Resistance, Infernal Legacy'), '+')
                var.put('raceSpellAbility', Js(5.0))
                var.get('raceSpells').callprop('push', Js('Thaumaturgy'))
                if (var.get('level')>Js(2.0)):
                    var.get('raceSpells').callprop('push', Js('Hellish Rebuke (once a day)'))
                if (var.get('level')>Js(4.0)):
                    var.get('raceSpells').callprop('push', Js('Darkness (once a day)'))
                if (var.get('gender')==Js(2.0)):
                    var.put('name', var.get('tieflingNameF').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tieflingNameF').get('length')))))
                else:
                    var.put('name', var.get('tieflingNameM').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tieflingNameM').get('length')))))
                var.put('name', (Js(' ')+var.get('tieflingNameLast').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tieflingNameLast').get('length'))))), '+')
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js(6.0)):
                SWITCHED = True
                var.put('racetxt', Js('Drow Elf'))
                var.get('abil').put('5', Js(1.0), '+')
                var.get('abil').put('1', Js(2.0), '+')
                var.get('skLearn').put('11', Js(True))
                var.get('mySkills').callprop('push', Js(11.0))
                var.put('raceSpellAbility', Js(5.0))
                var.put('speed', Js(30.0))
                var.put('languageOutput', Js('Common, Elvish'))
                var.put('abOutput', Js('Superior Darkvision (120 ft), Sunlight sensitivity, Drow Magic, Keen Senses, Fey Ancestry, Trance'), '+')
                var.get('raceSpells').callprop('push', Js('Dancing Lights'))
                if (var.get('level')>Js(2.0)):
                    var.get('raceSpells').callprop('push', Js('Faerie Fire (once a day)'))
                if (var.get('level')>Js(4.0)):
                    var.get('raceSpells').callprop('push', Js('Darkness (once a day) '))
                if (var.get('gender')==Js(2.0)):
                    var.put('name', var.get('elfNameF').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('elfNameF').get('length')))))
                else:
                    var.put('name', var.get('elfNameM').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('elfNameM').get('length')))))
                var.put('name', (Js(' ')+var.get('elfNameLast').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('elfNameLast').get('length'))))), '+')
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js(7.0)):
                SWITCHED = True
                var.put('racetxt', Js('Rock Gnome'))
                var.get('abil').put('3', Js(2.0), '+')
                var.put('speed', Js(25.0))
                var.get('abil').put('2', Js(1.0), '+')
                var.put('size', Js('Small'))
                var.put('languageOutput', Js('Common, Gnomish'))
                if (var.get('gender')==Js(2.0)):
                    var.put('name', var.get('gnomeNameF').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('gnomeNameF').get('length')))))
                else:
                    var.put('name', var.get('gnomeNameM').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('gnomeNameM').get('length')))))
                var.put('name', (Js(' ')+var.get('gnomeNameLast').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('gnomeNameLast').get('length'))))), '+')
                var.put('abOutput', Js("Darkvision, Gnome Cunning, Artificer's Lore"), '+')
                var.put('toOutput', Js(", Tinker's tools"), '+')
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js(21.0)):
                SWITCHED = True
                var.put('racetxt', Js('Aarakocra'))
                var.get('abil').put('1', Js(2.0), '+')
                var.put('speed', Js(25.0))
                var.get('abil').put('4', Js(1.0), '+')
                var.put('size', Js('Medium'))
                var.put('languageOutput', Js('Common, Aarakocra, Auran'))
                var.put('abOutput', Js('Flight, Talons'), '+')
                var.put('name', var.get('aarName').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('aarName').get('length')))))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js(22.0)):
                SWITCHED = True
                var.put('racetxt', Js('Deep Gnome (Svirfneblin)'))
                var.get('abil').put('3', Js(2.0), '+')
                var.put('speed', Js(25.0))
                var.get('abil').put('1', Js(1.0), '+')
                var.put('size', Js('Small'))
                var.put('languageOutput', Js('Common, Gnomish, Undercommon'))
                if (var.get('gender')==Js(2.0)):
                    var.put('name', var.get('deepGnomeNameF').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('deepGnomeNameF').get('length')))))
                else:
                    var.put('name', var.get('deepGnomeNameM').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('deepGnomeNameM').get('length')))))
                var.put('name', (Js(' ')+var.get('deepGnomeNameLast').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('deepGnomeNameLast').get('length'))))), '+')
                var.put('abOutput', Js('Superior Darkvision (120 ft), Gnome Cunning, Stone Camouflage'), '+')
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js(23.0)):
                SWITCHED = True
                var.put('racetxt', Js('Air Genasi'))
                var.get('abil').put('1', Js(1.0), '+')
                var.put('abOutput', Js('Unending Breath, Mingle with the Wind'), '+')
                var.get('raceSpells').callprop('push', Js('Levitate (once per long rest)'))
                var.put('raceSpellAbility', Js(2.0))
                var.get('abil').put('2', Js(2.0), '+')
                var.put('speed', Js(30.0))
                var.put('size', Js('Medium'))
                var.put('languageOutput', Js('Common, Primordial'))
                if (var.get('gender')==Js(2.0)):
                    var.put('name', var.get('humanNameF').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('humanNameF').get('length')))))
                else:
                    var.put('name', var.get('humanNameM').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('humanNameM').get('length')))))
                var.put('name', (Js(' ')+var.get('humanNameLast').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('humanNameLast').get('length'))))), '+')
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js(24.0)):
                SWITCHED = True
                var.put('racetxt', Js('Earth Genasi'))
                var.get('abil').put('1', Js(0.0), '+')
                var.put('abOutput', Js('Earth Walk, Merge with Stone'), '+')
                var.get('raceSpells').callprop('push', Js('Pass Without Trace (once per long rest)'))
                var.put('raceSpellAbility', Js(2.0))
                var.get('abil').put('2', Js(2.0), '+')
                var.put('speed', Js(30.0))
                var.put('size', Js('Medium'))
                var.put('languageOutput', Js('Common, Primordial'))
                if (var.get('gender')==Js(2.0)):
                    var.put('name', var.get('humanNameF').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('humanNameF').get('length')))))
                else:
                    var.put('name', var.get('humanNameM').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('humanNameM').get('length')))))
                var.put('name', (Js(' ')+var.get('humanNameLast').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('humanNameLast').get('length'))))), '+')
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js(25.0)):
                SWITCHED = True
                var.put('racetxt', Js('Fire Genasi'))
                var.get('abil').put('3', Js(1.0), '+')
                var.put('abOutput', Js('Darkvision, Fire Resistance, Reach to the Blaze'), '+')
                var.get('raceSpells').callprop('push', Js('Produce Flame'))
                if (var.get('level')>Js(2.0)):
                    var.get('raceSpells').callprop('push', Js('Burning Hands (as a 1st level spell once per long rest)'))
                var.put('raceSpellAbility', Js(2.0))
                var.get('abil').put('2', Js(2.0), '+')
                var.put('speed', Js(30.0))
                var.put('size', Js('Medium'))
                var.put('languageOutput', Js('Common, Primordial'))
                if (var.get('gender')==Js(2.0)):
                    var.put('name', var.get('humanNameF').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('humanNameF').get('length')))))
                else:
                    var.put('name', var.get('humanNameM').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('humanNameM').get('length')))))
                var.put('name', (Js(' ')+var.get('humanNameLast').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('humanNameLast').get('length'))))), '+')
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js(26.0)):
                SWITCHED = True
                var.put('racetxt', Js('Water Genasi'))
                var.get('abil').put('4', Js(1.0), '+')
                var.put('abOutput', Js('Acid Resistance, Amphibious, Swim, Call to the Wave'), '+')
                var.get('raceSpells').callprop('push', Js('Shape Water'))
                if (var.get('level')>Js(2.0)):
                    var.get('raceSpells').callprop('push', Js('Create or Destroy Water (as a 2nd level spell once per long rest)'))
                var.put('raceSpellAbility', Js(2.0))
                var.get('abil').put('2', Js(2.0), '+')
                var.put('speed', Js(30.0))
                var.put('size', Js('Medium'))
                var.put('languageOutput', Js('Common, Primordial'))
                if (var.get('gender')==Js(2.0)):
                    var.put('name', var.get('humanNameF').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('humanNameF').get('length')))))
                else:
                    var.put('name', var.get('humanNameM').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('humanNameM').get('length')))))
                var.put('name', (Js(' ')+var.get('humanNameLast').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('humanNameLast').get('length'))))), '+')
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js(27.0)):
                SWITCHED = True
                var.put('racetxt', Js('Goliath'))
                var.get('abil').put('2', Js(1.0), '+')
                var.put('abOutput', Js("Natural Athlete (Athletics skill), Stone's Endurance, Powerful Build, Mountain Born"), '+')
                var.get('abil').put('0', Js(2.0), '+')
                var.get('mySkills').callprop('push', Js(3.0))
                var.get('skLearn').put('3', Js(True))
                var.put('speed', Js(30.0))
                var.put('size', Js('Medium'))
                var.put('languageOutput', Js('Common, Giant'))
                def PyJs_LONG_11_(var=var):
                    return ((((var.get('goliathNameBirth').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('goliathNameBirth').get('length'))))+Js('  "'))+var.get('goliathNameNick').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('goliathNameNick').get('length')))))+Js('" '))+var.get('goliathNameClan').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('goliathNameClan').get('length')))))
                var.put('name', PyJs_LONG_11_())
                break
            SWITCHED = True
            break
    else:
        var.put('ra', var.get('Math').callprop('floor', ((var.get('Math').callprop('random')*Js(7.0))+Js(1.0))))
        if (var.get('forceRace')>Js(10.0)):
            var.put('ra', (var.get('forceRace')-Js(10.0)))
        if (var.get('ra')!=Js(3.0)):
            var.put('abOutput', Js('<b>Racial Traits:</b> '), '+')
        while 1:
            SWITCHED = False
            CONDITION = (var.get('ra'))
            if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
                SWITCHED = True
                var.put('racetxt', Js('Hill Dwarf'))
                var.get('abil').put('2', Js(2.0), '+')
                var.get('abil').put('4', Js(1.0), '+')
                var.put('languageOutput', Js('Common, Dwarvish'))
                var.put('speed', Js(25.0))
                var.put('abOutput', Js('Darkvision, Dwarven Resilience'), '+')
                var.put('x', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(3.0))))
                while 1:
                    SWITCHED = False
                    CONDITION = (var.get('x'))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(0.0)):
                        SWITCHED = True
                        var.put('toOutput', Js(", Smith's tools"), '+')
                        break
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
                        SWITCHED = True
                        var.put('toOutput', Js(", Brewer's tools"), '+')
                        break
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                        SWITCHED = True
                        var.put('toOutput', Js(", Mason's tools"), '+')
                        break
                    SWITCHED = True
                    break
                var.put('abOutput', Js(', Stonecunning, Dwarven toughness'), '+')
                if (var.get('gender')==Js(2.0)):
                    var.put('name', var.get('dwarfNameF').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('dwarfNameF').get('length')))))
                else:
                    var.put('name', var.get('dwarfNameM').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('dwarfNameM').get('length')))))
                var.put('name', (Js(' ')+var.get('dwarfNameLast').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('dwarfNameLast').get('length'))))), '+')
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                SWITCHED = True
                var.put('racetxt', Js('Mountain Dwarf'))
                var.get('abil').put('0', Js(2.0), '+')
                var.get('abil').put('2', Js(2.0), '+')
                var.put('languageOutput', Js('Common, Dwarvish'))
                var.put('speed', Js(25.0))
                var.put('abOutput', Js('Darkvision, Dwarven Resilience'), '+')
                var.put('x', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(3.0))))
                while 1:
                    SWITCHED = False
                    CONDITION = (var.get('x'))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(0.0)):
                        SWITCHED = True
                        var.put('toOutput', Js(", Smith's tools"), '+')
                        break
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
                        SWITCHED = True
                        var.put('toOutput', Js(", Brewer's tools"), '+')
                        break
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                        SWITCHED = True
                        var.put('toOutput', Js(", Mason's tools"), '+')
                        break
                    SWITCHED = True
                    break
                var.put('abOutput', Js(', Stonecunning'), '+')
                if (var.get('gender')==Js(2.0)):
                    var.put('name', var.get('dwarfNameF').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('dwarfNameF').get('length')))))
                else:
                    var.put('name', var.get('dwarfNameM').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('dwarfNameM').get('length')))))
                var.put('name', (Js(' ')+var.get('dwarfNameLast').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('dwarfNameLast').get('length'))))), '+')
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js(3.0)):
                SWITCHED = True
                var.put('racetxt', Js('Human'))
                #for JS loop
                var.put('x', Js(0.0))
                while (var.get('x')<Js(6.0)):
                    try:
                        var.get('abil').put(var.get('x'), Js(1.0), '+')
                    finally:
                            (var.put('x',Js(var.get('x').to_number())+Js(1))-Js(1))
                var.put('languageOutput', Js('Common'))
                var.put('speed', Js(30.0))
                var.put('moreLang', Js(1.0), '+')
                if (var.get('gender')==Js(2.0)):
                    var.put('name', var.get('humanNameF').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('humanNameF').get('length')))))
                else:
                    var.put('name', var.get('humanNameM').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('humanNameM').get('length')))))
                var.put('name', (Js(' ')+var.get('humanNameLast').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('humanNameLast').get('length'))))), '+')
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js(4.0)):
                SWITCHED = True
                var.put('racetxt', Js('High Elf'))
                var.get('abil').put('1', Js(2.0), '+')
                var.get('abil').put('3', Js(1.0), '+')
                var.put('languageOutput', Js('Common, Elvish'))
                var.put('raceSpellAbility', Js(3.0))
                var.put('speed', Js(30.0))
                var.put('moreLang', Js(1.0), '+')
                var.get('skLearn').put('11', Js(True))
                var.get('mySkills').callprop('push', Js(11.0))
                var.put('abOutput', Js('Darkvision, Keen senses, Fey ancestry, Trance, Cantrip, Extra Language'), '+')
                if (var.get('gender')==Js(2.0)):
                    var.put('name', var.get('elfNameF').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('elfNameF').get('length')))))
                else:
                    var.put('name', var.get('elfNameM').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('elfNameM').get('length')))))
                var.put('name', (Js(' ')+var.get('elfNameLast').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('elfNameLast').get('length'))))), '+')
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js(5.0)):
                SWITCHED = True
                var.put('racetxt', Js('Wood Elf'))
                var.get('abil').put('1', Js(2.0), '+')
                var.get('abil').put('4', Js(1.0), '+')
                var.put('speed', Js(35.0))
                var.put('languageOutput', Js('Common, Elvish'))
                var.put('abOutput', Js('Darkvision, Keen senses, Fey ancestry, Trance, Mask of the Wild'), '+')
                var.get('skLearn').put('11', Js(True))
                var.get('mySkills').callprop('push', Js(11.0))
                if (var.get('gender')==Js(2.0)):
                    var.put('name', var.get('elfNameF').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('elfNameF').get('length')))))
                else:
                    var.put('name', var.get('elfNameM').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('elfNameM').get('length')))))
                var.put('name', (Js(' ')+var.get('elfNameLast').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('elfNameLast').get('length'))))), '+')
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js(6.0)):
                SWITCHED = True
                var.put('racetxt', Js('Stout Halfling'))
                var.get('abil').put('1', Js(2.0), '+')
                var.get('abil').put('2', Js(1.0), '+')
                var.put('size', Js('Small'))
                var.put('languageOutput', Js('Common, Halfling'))
                var.put('abOutput', Js('Lucky, Brave, Halfling Nimbleness, Stout Resilience'), '+')
                var.put('speed', Js(25.0))
                if (var.get('gender')==Js(2.0)):
                    var.put('name', var.get('halfNameF').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('halfNameF').get('length')))))
                else:
                    var.put('name', var.get('halfNameM').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('halfNameM').get('length')))))
                var.put('name', (Js(' ')+var.get('halfNameLast').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('halfNameLast').get('length'))))), '+')
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js(7.0)):
                SWITCHED = True
                var.put('racetxt', Js('Lightfoot Halfling'))
                var.get('abil').put('1', Js(2.0), '+')
                var.get('abil').put('5', Js(1.0), '+')
                var.put('size', Js('Small'))
                var.put('languageOutput', Js('Common, Halfling'))
                var.put('abOutput', Js('Lucky, Brave, Halfling Nimbleness, Naturally Stealthy'), '+')
                var.put('speed', Js(25.0))
                if (var.get('gender')==Js(2.0)):
                    var.put('name', var.get('halfNameF').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('halfNameF').get('length')))))
                else:
                    var.put('name', var.get('halfNameM').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('halfNameM').get('length')))))
                var.put('name', (Js(' ')+var.get('halfNameLast').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('halfNameLast').get('length'))))), '+')
                break
            SWITCHED = True
            break
    if (var.get('racetxt')!=Js('Human')):
        var.put('abOutput', Js('==EOF=='), '+')
    var.put('abOutput', Js('<b>Abilities:</b> '), '+')
    var.get('console').callprop('log', Js('Racial bonuses:'))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(6.0)):
        try:
            var.get('console').callprop('log', ((var.get('abilNames').get(var.get('i'))+Js(': '))+var.get('abil').get(var.get('i'))))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    var.put('cl', var.get('Math').callprop('floor', ((var.get('Math').callprop('random')*Js(15.0))+Js(1.0))))
    var.put('classtxt', Js(''))
    var.put('ab1', Js(0.0))
    var.put('ab2', Js(0.0))
    var.put('ab3', (-Js(1.0)))
    var.put('hd', Js(8.0))
    if (var.get('forceCl')>Js(0.0)):
        var.put('cl', var.get('forceCl'))
    while 1:
        SWITCHED = False
        CONDITION = (var.get('cl'))
        if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
            SWITCHED = True
            var.put('classtxt', Js('Barbarian'))
            var.put('bg', Js(9.0))
            var.put('ab1', Js(0.0))
            var.put('ab2', Js(2.0))
            var.put('ab3', Js(1.0))
            var.put('hd', Js(12.0))
            var.put('st', Js([Js(0.0), Js(2.0)]))
            var.put('x', Js(2.0))
            if (var.get('level')>Js(2.0)):
                var.put('x', Js(3.0))
            if (var.get('level')>Js(5.0)):
                var.put('x', Js(4.0))
            if (var.get('level')>Js(11.0)):
                var.put('x', Js(5.0))
            if (var.get('level')>Js(16.0)):
                var.put('x', Js(6.0))
            var.put('y', Js(2.0))
            if (var.get('level')>Js(8.0)):
                var.put('y', Js(3.0))
            if (var.get('level')>Js(15.0)):
                var.put('y', Js(4.0))
            var.put('abOutput', ((((Js('Rage (')+var.get('x'))+Js(' Rages, '))+var.get('showPlus')(var.get('y')))+Js(' damage), Unarmored Defense')), '+')
            if (var.get('level')>Js(1.0)):
                var.put('abOutput', Js(', Reckless Attack, Danger Sense'), '+')
            if (var.get('level')>Js(2.0)):
                var.put('x', var.get('Math').callprop('random'))
                if (var.get('forceBarb')==Js(0.0)):
                    var.put('x', Js(0.0))
                else:
                    if (var.get('forceBarb')>Js(0.0)):
                        var.put('x', Js(1.0))
                var.put('abOutput', Js(', Primal Path'), '+')
                if (var.get('x')<Js(0.5)):
                    var.put('classtxt', Js(' (Path of the Berserker)'), '+')
                    var.put('abOutput', Js(' (Path of the Berserker)'), '+')
                    var.put('abOutput', Js(', Frenzy'), '+')
                else:
                    var.put('classtxt', Js(' (Path of the Totem Warrior - '), '+')
                    var.put('abOutput', Js(' (Path of the Totem Warrior)'), '+')
                    var.put('abOutput', Js(', Spirit Seeker, Totem Spirit'), '+')
                    var.put('x', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(3.0))))
                    if (var.get('forceBarb')>Js(1.0)):
                        var.put('x', (var.get('forceBarb')-Js(2.0)))
                    if (var.get('x')==Js(0.0)):
                        var.put('abOutput', Js(' (Bear)'), '+')
                        var.put('classtxt', Js('Bear)'), '+')
                    if (var.get('x')==Js(1.0)):
                        var.put('abOutput', Js(' (Eagle)'), '+')
                        var.put('classtxt', Js('Eagle)'), '+')
                    if (var.get('x')==Js(2.0)):
                        var.put('abOutput', Js(' (Wolf)'), '+')
                        var.put('classtxt', Js('Wolf)'), '+')
            if (var.get('level')>Js(4.0)):
                var.put('abOutput', Js(', Extra Attack, Fast Movement'), '+')
                var.put('speed', Js(10.0), '+')
            if (var.get('level')>Js(5.0)):
                var.put('abOutput', Js(', Path Feature'), '+')
            if (var.get('level')>Js(6.0)):
                var.put('abOutput', Js(', Feral Instinct'), '+')
            if (var.get('level')>Js(8.0)):
                var.put('abOutput', Js(', Brutal Critical'), '+')
            if (var.get('level')>Js(9.0)):
                var.put('abOutput', Js(', Spirit Walker'), '+')
            var.put('eqOutput', Js(", Explorer's pack"), '+')
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
            SWITCHED = True
            var.put('classtxt', Js('Bard'))
            var.put('spellAbility', Js(5.0))
            var.put('ab1', Js(5.0))
            var.put('ab2', Js(1.0))
            var.put('bg', Js(4.0))
            var.put('st', Js([Js(1.0), Js(5.0)]))
            var.put('abOutput', Js('Spellcasting, Bardic Inspiration ('), '+')
            if (var.get('level')>Js(9.0)):
                var.put('abOutput', Js('d10)'), '+')
            else:
                if (var.get('level')>Js(4.0)):
                    var.put('abOutput', Js('d8)'), '+')
                else:
                    var.put('abOutput', Js('d6)'), '+')
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<Js(3.0)):
                try:
                    var.put('temp', var.get('music').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('music').get('length')))))
                    if (var.get('Math').callprop('random')<Js(0.5)):
                        var.put('temp', var.get('music').get('0'))
                    while (var.get('myMusic').callprop('indexOf', var.get('temp'))>(-Js(1.0))):
                        var.put('temp', var.get('music').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('music').get('length')))))
                    var.get('myMusic').callprop('push', var.get('temp'))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            var.put('myInstrument', var.get('myMusic').get('0'))
            var.get('myMusic').callprop('sort')
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<Js(3.0)):
                try:
                    var.put('toOutput', (Js(', ')+var.get('myMusic').get(var.get('i'))), '+')
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            if (var.get('level')>Js(1.0)):
                var.put('abOutput', Js(', Jack of all trades, Song of Rest (d'), '+')
                if (var.get('level')>Js(8.0)):
                    var.put('abOutput', Js('8)'), '+')
                else:
                    var.put('abOutput', Js('6)'), '+')
            if (var.get('level')>Js(2.0)):
                var.put('x', var.get('Math').callprop('random'))
                if (var.get('forceBard')==Js(0.0)):
                    var.put('x', Js(1.0))
                else:
                    if (var.get('forceBard')==Js(1.0)):
                        var.put('x', Js(0.0))
                if (var.get('x')>Js(0.5)):
                    var.put('abOutput', Js(', Bard College (Lore), Bonus proficiencies, Cutting words'), '+')
                    var.put('classtxt', Js(' (College of Lore)'), '+')
                    if (var.get('level')>Js(5.0)):
                        var.put('abOutput', Js(', Additional Magical Secrets'), '+')
                else:
                    var.put('abOutput', Js(', Bard College (Valor), Bonus proficiencies (arms), Combat inspiration'), '+')
                    var.put('classtxt', Js(' (College of Valor)'), '+')
                    if (var.get('level')>Js(5.0)):
                        var.put('abOutput', Js(', Extra Attack'), '+')
                var.put('abOutput', Js(', Expertise'), '+')
            if (var.get('level')>Js(4.0)):
                var.put('abOutput', Js(', Font of Inspiration'), '+')
            if (var.get('level')>Js(5.0)):
                var.put('abOutput', Js(', Countercharm'), '+')
            if (var.get('level')>Js(9.0)):
                var.put('abOutput', Js(', Magical Secrets'), '+')
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(3.0)):
            SWITCHED = True
            var.put('classtxt', Js('Cleric ('))
            var.put('spellAbility', Js(4.0))
            var.put('ab1', Js(4.0))
            var.put('ab2', Js(0.0))
            var.put('ab3', Js(2.0))
            var.put('bg', Js(1.0))
            var.put('st', Js([Js(4.0), Js(5.0)]))
            var.put('abOutput', Js('Spellcasting, Divine Domain'), '+')
            var.put('clDomain', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(8.0))))
            if ((var.get('forceDomain')>(-Js(1.0))) and (var.get('magicGet')(Js('selClass'), var.get('possibile')).get('value')==Js(3.0))):
                var.put('clDomain', var.get('forceDomain'))
            while 1:
                SWITCHED = False
                CONDITION = (var.get('clDomain'))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(0.0)):
                    SWITCHED = True
                    var.put('classtxt', Js('Knowledge'), '+')
                    var.put('abOutput', Js(', Blessings of Knowledge'), '+')
                    var.put('moreLang', Js(2.0), '+')
                    #for JS loop
                    var.put('x', Js(2.0))
                    while (var.get('x')>Js(0.0)):
                        try:
                            var.put('y', var.get('pickSome')(Js([Js(2.0), Js(5.0), Js(10.0), Js(14.0)])))
                            var.get('mySkills').callprop('push', var.get('y'))
                            var.get('expertise').callprop('push', var.get('y'))
                        finally:
                                (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
                    if (var.get('level')>Js(1.0)):
                        var.put('abOutput', Js(', Channel Divinity: Turn Undead, Channel Divinity: Knowledge of the Ages'), '+')
                    if (var.get('level')>Js(5.0)):
                        var.put('abOutput', Js(', Channel Divinity: Read Thoughts'), '+')
                    if (var.get('level')>Js(7.0)):
                        var.put('abOutput', Js(', Potent Spellcasting'), '+')
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
                    SWITCHED = True
                    var.put('classtxt', Js('Life'), '+')
                    var.put('abOutput', Js(', Bonus proficiency, Discipline of Life'), '+')
                    if (var.get('level')>Js(1.0)):
                        var.put('abOutput', ((Js(', Channel Divinity: Turn Undead, Channel Divinity: Preserve Life (heals ')+(Js(5.0)*var.get('level')))+Js(' hp)')), '+')
                    if (var.get('level')>Js(5.0)):
                        var.put('abOutput', Js(', Blessed Healer'), '+')
                    if (var.get('level')>Js(7.0)):
                        var.put('abOutput', Js(', Divine Strike +1d8 Radiant dmg'), '+')
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                    SWITCHED = True
                    var.put('classtxt', Js('Light'), '+')
                    var.put('abOutput', Js(', Bonus proficiency, Warding Flare'), '+')
                    var.get('myCantrips').callprop('unshift', Js('Light'))
                    if (var.get('level')>Js(1.0)):
                        var.put('abOutput', Js(', Channel Divinity: Turn Undead, Channel Divinity: Radiance of the Dawn'), '+')
                    if (var.get('level')>Js(5.0)):
                        var.put('abOutput', Js(', Improved Flare'), '+')
                    if (var.get('level')>Js(7.0)):
                        var.put('abOutput', Js(', Potent Spellcasting'), '+')
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js(3.0)):
                    SWITCHED = True
                    var.put('classtxt', Js('Nature'), '+')
                    var.put('abOutput', Js(', Acolyte of Nature, Bonus proficiency'), '+')
                    if (var.get('level')>Js(1.0)):
                        var.put('abOutput', Js(', Channel Divinity: Turn Undead, Channel Divinity: Charm Animals and Plants'), '+')
                    if (var.get('level')>Js(5.0)):
                        var.put('abOutput', Js(', Dampen Elements'), '+')
                    if (var.get('level')>Js(7.0)):
                        var.put('abOutput', Js(', Divine Strike - 1d8 Cold, Fire, or Lighting dmg'), '+')
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js(4.0)):
                    SWITCHED = True
                    var.put('classtxt', Js('Tempest'), '+')
                    var.put('abOutput', Js(', Bonus proficiency, Wrath of the Storm'), '+')
                    if (var.get('level')>Js(1.0)):
                        var.put('abOutput', Js(', Channel Divinity: Turn Undead, Channel Divinity: Destructive Wrath'), '+')
                    if (var.get('level')>Js(5.0)):
                        var.put('abOutput', Js(', Thunderbolt Strike'), '+')
                    if (var.get('level')>Js(7.0)):
                        var.put('abOutput', Js(', Divine Strike - 1d8 Thunder dmg'), '+')
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js(5.0)):
                    SWITCHED = True
                    var.put('classtxt', Js('Trickery'), '+')
                    var.put('abOutput', Js(', Blessing of the Trickster'), '+')
                    if (var.get('level')>Js(1.0)):
                        var.put('abOutput', Js(', Channel Divinity: Turn Undead, Channel Divinity: Invoke Duplicity'), '+')
                    if (var.get('level')>Js(5.0)):
                        var.put('abOutput', Js(', Channel Divinity: Cloak of Shadows'), '+')
                    if (var.get('level')>Js(7.0)):
                        var.put('abOutput', Js(', Divine Strike - 1d8 Poison dmg'), '+')
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js(6.0)):
                    SWITCHED = True
                    var.put('classtxt', Js('War'), '+')
                    var.put('abOutput', Js(', Bonus proficiency, War Priest'), '+')
                    if (var.get('level')>Js(1.0)):
                        var.put('abOutput', Js(', Channel Divinity: Turn Undead, Channel Divinity: Guided Strike'), '+')
                    if (var.get('level')>Js(5.0)):
                        var.put('abOutput', Js(", Channel Divinity: War God's Blessing"), '+')
                    if (var.get('level')>Js(7.0)):
                        var.put('abOutput', Js(', Divine Strike (1d8 Extra Weapon dmg)'), '+')
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js(7.0)):
                    SWITCHED = True
                    var.put('classtxt', Js('Death'), '+')
                    var.put('abOutput', Js(', Bonus proficiency, Reaper'), '+')
                    if (var.get('level')>Js(1.0)):
                        var.put('x', (Js(5.0)+(var.get('level')*Js(2.0))))
                        var.put('abOutput', ((Js(', Channel Divinity: Turn Undead, Channel Divinity: Touch of Death ')+var.get('showPlus')(var.get('x')))+Js('  necrotic damage')), '+')
                    if (var.get('level')>Js(5.0)):
                        var.put('abOutput', Js(', Inescapable Destruction'), '+')
                    if (var.get('level')>Js(7.0)):
                        var.put('abOutput', Js(', Divine Strike +1d8 necrotic damage'), '+')
                    break
                SWITCHED = True
                break
            var.put('classtxt', Js(' domain)'), '+')
            if (var.get('level')>Js(7.0)):
                var.put('abOutput', Js(', Destroy Undead (CR 1)'), '+')
            else:
                if (var.get('level')>Js(4.0)):
                    var.put('abOutput', Js(', Destroy Undead (CR 1/2)'), '+')
            if (var.get('level')>Js(9.0)):
                var.put('abOutput', Js(', Divine Intervention'), '+')
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(4.0)):
            SWITCHED = True
            var.put('classtxt', Js('Druid'))
            var.put('spellAbility', Js(4.0))
            var.put('ab1', Js(4.0))
            var.put('ab2', Js(2.0))
            var.put('bg', Js(6.0))
            var.put('st', Js([Js(3.0), Js(4.0)]))
            var.put('toOutput', Js(', Herbalism kit'), '+')
            var.put('languageOutput', Js(', Druidic'), '+')
            var.put('abOutput', Js('Spellcasting'), '+')
            var.put('xx', (-Js(1.0)))
            if ((var.get('forceCircle')>(-Js(1.0))) and (var.get('magicGet')(Js('selClass'), var.get('possibile')).get('value')==Js(4.0))):
                var.put('xx', var.get('forceCircle'))
            var.put('x', var.get('Math').callprop('random'))
            if (var.get('xx')==Js(0.0)):
                var.put('x', Js(1.0))
            if (var.get('level')>Js(1.0)):
                var.put('abOutput', Js(', Wild Shape'), '+')
                if ((var.get('x')<Js(0.5)) or (var.get('xx')>Js(0.0))):
                    if (var.get('level')<Js(4.0)):
                        var.put('abOutput', Js(' (CR 1/4 creature - No flying or swimming speed)'), '+')
                    else:
                        if (var.get('level')<Js(8.0)):
                            var.put('abOutput', Js(' (CR 1/2 creature - No flying speed)'), '+')
                        else:
                            if (var.get('level')>Js(7.0)):
                                var.put('abOutput', Js(' (CR 1 creature)'), '+')
                    var.put('drCircle', Js(0.0))
                    var.put('x', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(8.0))))
                    if (var.get('xx')>Js(0.0)):
                        var.put('x', (var.get('xx')-Js(1.0)))
                    if (var.get('x')==Js(0.0)):
                        var.put('land', Js('Arctic'), '+')
                        if (var.get('level')>Js(2.0)):
                            var.get('ciSpells').callprop('push', Js('Hold Person'))
                            var.get('ciSpells').callprop('push', Js('Spike Growth'))
                        if (var.get('level')>Js(4.0)):
                            var.get('ciSpells').callprop('push', Js('Sleet Storm'))
                            var.get('ciSpells').callprop('push', Js('Slow'))
                        if (var.get('level')>Js(6.0)):
                            var.get('ciSpells').callprop('push', Js('Freedom of Movement'))
                            var.get('ciSpells').callprop('push', Js('Ice Storm'))
                        if (var.get('level')>Js(8.0)):
                            var.get('ciSpells').callprop('push', Js('Commune with Nature'))
                            var.get('ciSpells').callprop('push', Js('Cone of Cold'))
                    if (var.get('x')==Js(1.0)):
                        var.put('land', Js('Coast'), '+')
                        if (var.get('level')>Js(2.0)):
                            var.get('ciSpells').callprop('push', Js('Mirror Image'))
                            var.get('ciSpells').callprop('push', Js('Misty Step'))
                        if (var.get('level')>Js(4.0)):
                            var.get('ciSpells').callprop('push', Js('Water Breathing'))
                            var.get('ciSpells').callprop('push', Js('Water Walk'))
                        if (var.get('level')>Js(6.0)):
                            var.get('ciSpells').callprop('push', Js('Control Water'))
                            var.get('ciSpells').callprop('push', Js('Freedom of Movement'))
                        if (var.get('level')>Js(8.0)):
                            var.get('ciSpells').callprop('push', Js('Conjure Elemental'))
                            var.get('ciSpells').callprop('push', Js('Scrying'))
                    if (var.get('x')==Js(2.0)):
                        var.put('land', Js('Desert'), '+')
                        if (var.get('level')>Js(2.0)):
                            var.get('ciSpells').callprop('push', Js('Blur'))
                            var.get('ciSpells').callprop('push', Js('Silence'))
                        if (var.get('level')>Js(4.0)):
                            var.get('ciSpells').callprop('push', Js('Create Food and Water'))
                            var.get('ciSpells').callprop('push', Js('Protection from Energy'))
                        if (var.get('level')>Js(6.0)):
                            var.get('ciSpells').callprop('push', Js('Blight'))
                            var.get('ciSpells').callprop('push', Js('Hallucinatory Terrain'))
                        if (var.get('level')>Js(8.0)):
                            var.get('ciSpells').callprop('push', Js('Insect Plague'))
                            var.get('ciSpells').callprop('push', Js('Wall of Stone'))
                    if (var.get('x')==Js(3.0)):
                        var.put('land', Js('Forest'), '+')
                        if (var.get('level')>Js(2.0)):
                            var.get('ciSpells').callprop('push', Js('Barkskin'))
                            var.get('ciSpells').callprop('push', Js('Spider Climb'))
                        if (var.get('level')>Js(4.0)):
                            var.get('ciSpells').callprop('push', Js('Call Lightning'))
                            var.get('ciSpells').callprop('push', Js('Plant Growth'))
                        if (var.get('level')>Js(6.0)):
                            var.get('ciSpells').callprop('push', Js('Divination'))
                            var.get('ciSpells').callprop('push', Js('Freedom of Movement'))
                        if (var.get('level')>Js(8.0)):
                            var.get('ciSpells').callprop('push', Js('Commune with Nature'))
                            var.get('ciSpells').callprop('push', Js('Tree Stride'))
                    if (var.get('x')==Js(4.0)):
                        var.put('land', Js('Grassland'), '+')
                        if (var.get('level')>Js(2.0)):
                            var.get('ciSpells').callprop('push', Js('Invisibility'))
                            var.get('ciSpells').callprop('push', Js('Pass without Trace'))
                        if (var.get('level')>Js(4.0)):
                            var.get('ciSpells').callprop('push', Js('Daylight'))
                            var.get('ciSpells').callprop('push', Js('Haste'))
                        if (var.get('level')>Js(6.0)):
                            var.get('ciSpells').callprop('push', Js('Divination'))
                            var.get('ciSpells').callprop('push', Js('Freedom of Movement'))
                        if (var.get('level')>Js(8.0)):
                            var.get('ciSpells').callprop('push', Js('Dream'))
                            var.get('ciSpells').callprop('push', Js('Insect Plague'))
                    if (var.get('x')==Js(5.0)):
                        var.put('land', Js('Mountain'), '+')
                        if (var.get('level')>Js(2.0)):
                            var.get('ciSpells').callprop('push', Js('Spider Climb'))
                            var.get('ciSpells').callprop('push', Js('Spike Growth'))
                        if (var.get('level')>Js(4.0)):
                            var.get('ciSpells').callprop('push', Js('Lightning Bolt'))
                            var.get('ciSpells').callprop('push', Js('Meld into Stone'))
                        if (var.get('level')>Js(6.0)):
                            var.get('ciSpells').callprop('push', Js('Stone Shape'))
                            var.get('ciSpells').callprop('push', Js('Stoneskin'))
                        if (var.get('level')>Js(8.0)):
                            var.get('ciSpells').callprop('push', Js('Passwall'))
                            var.get('ciSpells').callprop('push', Js('Wall of Stone'))
                    if (var.get('x')==Js(6.0)):
                        var.put('land', Js('Swamp'), '+')
                        if (var.get('level')>Js(2.0)):
                            var.get('ciSpells').callprop('push', Js('Darkness'))
                            var.get('ciSpells').callprop('push', Js("Melf's Acid Arrow"))
                        if (var.get('level')>Js(4.0)):
                            var.get('ciSpells').callprop('push', Js('Water Walk'))
                            var.get('ciSpells').callprop('push', Js('Stinking Cloud'))
                        if (var.get('level')>Js(6.0)):
                            var.get('ciSpells').callprop('push', Js('Freedom of Movement'))
                            var.get('ciSpells').callprop('push', Js('Locate Creature'))
                        if (var.get('level')>Js(8.0)):
                            var.get('ciSpells').callprop('push', Js('Insect Plague'))
                            var.get('ciSpells').callprop('push', Js('Scrying'))
                    if (var.get('x')==Js(7.0)):
                        var.put('land', Js('Underdark'), '+')
                        if (var.get('level')>Js(2.0)):
                            var.get('ciSpells').callprop('push', Js('Spider Climb'))
                            var.get('ciSpells').callprop('push', Js('Web'))
                        if (var.get('level')>Js(4.0)):
                            var.get('ciSpells').callprop('push', Js('Gaseous Form'))
                            var.get('ciSpells').callprop('push', Js('Stinking Cloud'))
                        if (var.get('level')>Js(6.0)):
                            var.get('ciSpells').callprop('push', Js('Greater Invisibility'))
                            var.get('ciSpells').callprop('push', Js('Stone Shape'))
                        if (var.get('level')>Js(8.0)):
                            var.get('ciSpells').callprop('push', Js('Cloudkill'))
                            var.get('ciSpells').callprop('push', Js('Insect Plague'))
                    var.put('classtxt', ((Js(' (Circle of the Land  - ')+var.get('land'))+Js(')')), '+')
                    var.put('abOutput', ((Js(', Druid Circle (')+var.get('land'))+Js('), Bonus Cantrip, Natural Recovery')), '+')
                    if (var.get('level')>Js(5.0)):
                        var.put('abOutput', Js(", Land's Stride"), '+')
                    if (var.get('level')>Js(9.0)):
                        var.put('abOutput', Js(", Nature's Ward"), '+')
                else:
                    var.put('drCircle', Js(1.0))
                    var.put('classtxt', Js(' (Circle of the Moon)'), '+')
                    var.put('abOutput', Js(', Combat Wild Shape, Circle Forms (CR '), '+')
                    var.put('tempTxt', Js('1'))
                    if (var.get('level')>Js(5.0)):
                        var.put('tempTxt', Js('2'))
                    if (var.get('level')>Js(8.0)):
                        var.put('tempTxt', Js('3'))
                    var.put('tempTxt', Js(' creature'), '+')
                    if (var.get('level')<Js(4.0)):
                        var.put('tempTxt', Js(' - No flying or swimming speed)'), '+')
                    else:
                        if (var.get('level')>Js(7.0)):
                            var.put('tempTxt', Js(')'), '+')
                        else:
                            if (var.get('level')>Js(3.0)):
                                var.put('tempTxt', Js(' - No flying speed)'), '+')
                    var.put('abOutput', var.get('tempTxt'), '+')
                    if (var.get('level')>Js(5.0)):
                        var.put('abOutput', Js(', Primal Strike'), '+')
                    if (var.get('level')>Js(9.0)):
                        var.put('abOutput', Js(', Elemental Wild Shape'), '+')
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(5.0)):
            SWITCHED = True
            var.put('classtxt', Js('Fighter'))
            var.put('spellAbility', Js(3.0))
            var.put('ab1', Js(0.0))
            var.put('ab2', Js(3.0))
            var.put('ab3', Js(1.0))
            var.put('hd', Js(10.0))
            var.put('bg', Js(12.0))
            var.put('st', Js([Js(0.0), Js(2.0)]))
            var.put('fiStyle', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(6.0))))
            while 1:
                SWITCHED = False
                CONDITION = (var.get('fiStyle'))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(0.0)):
                    SWITCHED = True
                    var.put('temp', Js('Archery'))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
                    SWITCHED = True
                    var.put('temp', Js('Defense'))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                    SWITCHED = True
                    var.put('temp', Js('Dueling'))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js(3.0)):
                    SWITCHED = True
                    var.put('temp', Js('Great Weapon Fighting'))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js(4.0)):
                    SWITCHED = True
                    var.put('temp', Js('Protection'))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js(5.0)):
                    SWITCHED = True
                    var.put('temp', Js('Two-Weapon Fighting'))
                    break
                SWITCHED = True
                break
            var.put('abOutput', ((Js('Fighting Style (')+var.get('temp'))+Js('), Second Wind')), '+')
            if (var.get('level')>Js(1.0)):
                var.put('abOutput', Js(', Action Surge'), '+')
            if (var.get('level')>Js(2.0)):
                var.put('abOutput', Js(', Martial Archetype (Eldritch Knight), Spellcasting, Weapon Bond'), '+')
                var.put('classtxt', Js(' (Eldritch Knight)'), '+')
            if (var.get('level')>Js(4.0)):
                var.put('abOutput', Js(', Extra Attack'), '+')
            if (var.get('level')>Js(7.0)):
                var.put('abOutput', Js(', War Magic'), '+')
            if (var.get('level')>Js(8.0)):
                var.put('abOutput', Js(', Indomitable (one use)'), '+')
            if (var.get('level')>Js(9.0)):
                var.put('abOutput', Js(', Eldritch Strike'), '+')
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(6.0)):
            SWITCHED = True
            var.put('classtxt', Js('Fighter'))
            var.put('ab1', Js(1.0))
            var.put('ab2', Js(2.0))
            var.put('ab3', Js(0.0))
            var.put('hd', Js(10.0))
            var.put('bg', Js(12.0))
            var.put('st', Js([Js(0.0), Js(2.0)]))
            var.put('x', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(4.0))))
            var.put('fiStyle', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(6.0))))
            while (var.get('fiStyle')==Js(3.0)):
                var.put('fiStyle', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(6.0))))
            while 1:
                SWITCHED = False
                CONDITION = (var.get('fiStyle'))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(0.0)):
                    SWITCHED = True
                    var.put('temp', Js('Archery'))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
                    SWITCHED = True
                    var.put('temp', Js('Defense'))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                    SWITCHED = True
                    var.put('temp', Js('Dueling'))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js(4.0)):
                    SWITCHED = True
                    var.put('temp', Js('Protection'))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js(5.0)):
                    SWITCHED = True
                    var.put('temp', Js('Two-Weapon Fighting'))
                    break
                SWITCHED = True
                break
            var.put('abOutput', ((Js('Fighting Style (')+var.get('temp'))+Js('), Second Wind')), '+')
            if (var.get('level')>Js(1.0)):
                var.put('abOutput', Js(', Action Surge'), '+')
            if (var.get('level')>Js(2.0)):
                var.put('x', var.get('Math').callprop('random'))
                if (var.get('forceFigh')>(-Js(1.0))):
                    var.put('x', var.get('forceFigh'))
                if (var.get('x')<Js(0.5)):
                    var.put('classtxt', Js(' (Champion)'), '+')
                    var.put('abOutput', Js(', Martial Archetype (Champion), Improved Critical'), '+')
                    if (var.get('level')>Js(6.0)):
                        var.put('abOutput', Js(', Remarkable Athlete'), '+')
                    if (var.get('level')>Js(9.0)):
                        var.put('abOutput', Js(', Additional Fighting Style ('), '+')
                        var.put('x', var.get('fiStyle'))
                        while ((var.get('x')==var.get('fiStyle')) or (var.get('x')==Js(3.0))):
                            var.put('x', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(6.0))))
                        while 1:
                            SWITCHED = False
                            CONDITION = (var.get('x'))
                            if SWITCHED or PyJsStrictEq(CONDITION, Js(0.0)):
                                SWITCHED = True
                                var.put('temp', Js('Archery'))
                                var.put('fiStyle2', Js(0.0))
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
                                SWITCHED = True
                                var.put('temp', Js('Defense'))
                                var.put('fiStyle2', Js(1.0))
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                                SWITCHED = True
                                var.put('temp', Js('Dueling'))
                                var.put('fiStyle2', Js(2.0))
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js(4.0)):
                                SWITCHED = True
                                var.put('temp', Js('Protection'))
                                var.put('fiStyle2', Js(4.0))
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js(5.0)):
                                SWITCHED = True
                                var.put('temp', Js('Two-Weapon Fighting'))
                                var.put('fiStyle2', Js(5.0))
                                break
                            SWITCHED = True
                            break
                        var.put('abOutput', (var.get('temp')+Js(')')), '+')
                else:
                    var.put('classtxt', Js(' (Battle Master)'), '+')
                    var.put('x', Js(8.0))
                    if (var.get('level')>Js(9.0)):
                        var.put('x', Js(10.0))
                    var.put('y', Js(4.0))
                    if (var.get('level')>Js(6.0)):
                        var.put('y', Js(5.0))
                    var.put('z', Js(3.0))
                    if (var.get('level')>Js(6.0)):
                        var.put('z', Js(2.0), '+')
                    if (var.get('level')>Js(9.0)):
                        var.put('z', Js(2.0), '+')
                    var.put('abOutput', ((((((Js(', Martial Archetype (Battle Master), ')+var.get('y'))+Js(' Superiority Dice (d'))+var.get('x'))+Js('), '))+var.get('z'))+Js(' Maneuvers ')), '+')
                    var.get('pickManeuvers')(var.get('z'))
                    var.put('z', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('artisans').get('length'))))
                    while (var.get('toOutput').callprop('indexOf', var.get('artisans').get(var.get('z')))>(-Js(1.0))):
                        var.put('z', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('artisans').get('length'))))
                    var.put('toOutput', ((Js(', ')+var.get('artisans').get(var.get('z')))+Js("'s tools")), '+')
                    if (var.get('level')>Js(6.0)):
                        var.put('abOutput', Js(', Know Your Enemy'), '+')
                    if (var.get('level')>Js(9.0)):
                        var.put('abOutput', Js(', Improved Combat Superiority'), '+')
            if (var.get('level')>Js(4.0)):
                var.put('abOutput', Js(', Extra Attack'), '+')
            if (var.get('level')>Js(8.0)):
                var.put('abOutput', Js(', Indomitable (one use)'), '+')
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(7.0)):
            SWITCHED = True
            var.put('classtxt', Js('Fighter'))
            var.put('ab1', Js(0.0))
            var.put('ab2', Js(2.0))
            var.put('ab3', Js(1.0))
            var.put('hd', Js(10.0))
            var.put('bg', Js(12.0))
            var.put('st', Js([Js(0.0), Js(2.0)]))
            if (var.get('Math').callprop('random')>Js(0.93)):
                var.put('temp', Js('Archery'))
                var.put('fiStyle', Js(0.0))
            else:
                var.put('fiStyle', (var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(5.0)))+Js(1.0)))
                while 1:
                    SWITCHED = False
                    CONDITION = (var.get('fiStyle'))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(0.0)):
                        SWITCHED = True
                        var.put('temp', Js('Archery'))
                        break
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
                        SWITCHED = True
                        var.put('temp', Js('Defense'))
                        break
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                        SWITCHED = True
                        var.put('temp', Js('Dueling'))
                        break
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(3.0)):
                        SWITCHED = True
                        var.put('temp', Js('Great Weapon Fighting'))
                        break
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(4.0)):
                        SWITCHED = True
                        var.put('temp', Js('Protection'))
                        break
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(5.0)):
                        SWITCHED = True
                        var.put('temp', Js('Two-Weapon Fighting'))
                        break
                    SWITCHED = True
                    break
            var.put('abOutput', ((Js('Fighting Style (')+var.get('temp'))+Js('), Second Wind')), '+')
            if (var.get('level')>Js(1.0)):
                var.put('abOutput', Js(', Action Surge'), '+')
            if (var.get('level')>Js(2.0)):
                var.put('temp', Js(''))
                var.put('x', var.get('Math').callprop('random'))
                if (var.get('forceFigh')>(-Js(1.0))):
                    var.put('x', var.get('forceFigh'))
                if (var.get('x')<Js(0.5)):
                    var.put('classtxt', Js(' (Champion)'), '+')
                    var.put('abOutput', Js(', Martial Archetype (Champion), Improved Critical'), '+')
                    if (var.get('level')>Js(6.0)):
                        var.put('abOutput', Js(', Remarkable Athlete'), '+')
                    if (var.get('level')>Js(9.0)):
                        var.put('abOutput', Js(', Additional Fighting Style ('), '+')
                        var.put('fiStyle2', var.get('fiStyle'))
                        while (var.get('fiStyle2')==var.get('fiStyle')):
                            var.put('fiStyle2', (var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(5.0)))+Js(1.0)))
                        while 1:
                            SWITCHED = False
                            CONDITION = (var.get('fiStyle2'))
                            if SWITCHED or PyJsStrictEq(CONDITION, Js(0.0)):
                                SWITCHED = True
                                var.put('temp', Js('Archery'))
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
                                SWITCHED = True
                                var.put('temp', Js('Defense'))
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                                SWITCHED = True
                                var.put('temp', Js('Dueling'))
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js(3.0)):
                                SWITCHED = True
                                var.put('temp', Js('Great Weapon Fighting'))
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js(4.0)):
                                SWITCHED = True
                                var.put('temp', Js('Protection'))
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js(5.0)):
                                SWITCHED = True
                                var.put('temp', Js('Two-Weapon Fighting'))
                                break
                            SWITCHED = True
                            break
                        var.put('abOutput', (var.get('temp')+Js(')')), '+')
                else:
                    var.put('classtxt', Js(' (Battle Master)'), '+')
                    var.put('x', Js(8.0))
                    if (var.get('level')>Js(9.0)):
                        var.put('x', Js(10.0))
                    var.put('y', Js(4.0))
                    if (var.get('level')>Js(6.0)):
                        var.put('y', Js(5.0))
                    var.put('z', Js(3.0))
                    if (var.get('level')>Js(6.0)):
                        var.put('z', Js(2.0), '+')
                    if (var.get('level')>Js(9.0)):
                        var.put('z', Js(2.0), '+')
                    var.put('abOutput', ((((((Js(', Martial Archetype (Battle Master), ')+var.get('y'))+Js(' Superiority Dice (d'))+var.get('x'))+Js('), '))+var.get('z'))+Js(' Maneuvers ')), '+')
                    var.get('pickManeuvers')(var.get('z'))
                    var.put('z', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('artisans').get('length'))))
                    while (var.get('toOutput').callprop('indexOf', var.get('artisans').get(var.get('z')))>(-Js(1.0))):
                        var.put('z', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('artisans').get('length'))))
                    var.put('toOutput', ((Js(', ')+var.get('artisans').get(var.get('z')))+Js("'s tools")), '+')
                    if (var.get('level')>Js(6.0)):
                        var.put('abOutput', Js(', Know Your Enemy'), '+')
                    if (var.get('level')>Js(9.0)):
                        var.put('abOutput', Js(', Improved Combat Superiority'), '+')
            if (var.get('level')>Js(4.0)):
                var.put('abOutput', Js(', Extra Attack'), '+')
            if (var.get('level')>Js(8.0)):
                var.put('abOutput', Js(', Indomitable (one use)'), '+')
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(8.0)):
            SWITCHED = True
            var.put('classtxt', Js('Monk'))
            var.put('spellAbility', Js(4.0))
            var.put('ab1', Js(1.0))
            var.put('ab2', Js(4.0))
            var.put('bg', Js(6.0))
            var.put('st', Js([Js(1.0), Js(0.0)]))
            if (var.get('Math').callprop('random')>Js(0.5)):
                var.put('temp', var.get('music').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('music').get('length')))))
                while (var.get('myMusic').callprop('indexOf', var.get('temp'))>(-Js(1.0))):
                    var.put('temp', var.get('music').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('music').get('length')))))
                var.get('myMusic').callprop('push', var.get('temp'))
                var.put('toOutput', (Js(', ')+var.get('myMusic').get('0')), '+')
            else:
                var.put('z', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('artisans').get('length'))))
                while (var.get('toOutput').callprop('indexOf', var.get('artisans').get(var.get('z')))>(-Js(1.0))):
                    var.put('z', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('artisans').get('length'))))
                var.put('toOutput', ((Js(', ')+var.get('artisans').get(var.get('z')))+Js("'s tools")), '+')
            var.put('abOutput', Js('Unarmored Defense, Martial Arts'), '+')
            if (var.get('level')>Js(1.0)):
                var.put('ki', var.get('level'))
                var.put('abOutput', ((Js(', Ki (')+var.get('ki'))+Js(' points), Unarmored Movement (+')), '+')
                var.put('x', Js(10.0))
                if (var.get('level')>Js(5.0)):
                    var.put('x', Js(5.0), '+')
                if (var.get('level')>Js(9.0)):
                    var.put('x', Js(5.0), '+')
                var.put('abOutput', (var.get('x')+Js(' speed)')), '+')
                var.put('speed', var.get('x'), '+')
            if (var.get('level')>Js(2.0)):
                var.put('abOutput', Js(', Deflect Missiles, Monastic Tradition ('), '+')
                var.put('x', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(3.0))))
                if (var.get('forceMonk')>(-Js(1.0))):
                    var.put('x', var.get('forceMonk'))
                while 1:
                    SWITCHED = False
                    CONDITION = (var.get('x'))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(0.0)):
                        SWITCHED = True
                        var.put('abOutput', Js('Way of the Open Hand), Open Hand Technique'), '+')
                        var.put('classtxt', Js(' (Way of the Open Hand)'), '+')
                        break
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
                        SWITCHED = True
                        var.put('abOutput', Js('Way of Shadow), Shadow Arts'), '+')
                        var.get('myCantrips').callprop('unshift', Js('Minor Illusion'))
                        var.put('classtxt', Js(' (Way of Shadow)'), '+')
                        break
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                        SWITCHED = True
                        var.put('abOutput', Js('Way of the Four Elements), Disciple of the Elements (Elemental Attunement'), '+')
                        var.put('classtxt', Js(' (Way of the Four Elements)'), '+')
                        var.put('i', Js(1.0))
                        if (var.get('level')>Js(5.0)):
                            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                        while (var.get('i')>Js(0.0)):
                            var.put('tempTxt', Js(''))
                            var.put('y', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(7.0))))
                            if (var.get('level')>Js(5.0)):
                                var.put('y', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(9.0))))
                            if (var.get('y')==Js(0.0)):
                                var.put('tempTxt', Js(', Fangs of the Fire Snake'), '+')
                            if (var.get('y')==Js(1.0)):
                                var.put('tempTxt', Js(', Fist of Four Thunders'), '+')
                            if (var.get('y')==Js(2.0)):
                                var.put('tempTxt', Js(', Fist of Unbroken Air'), '+')
                            if (var.get('y')==Js(3.0)):
                                var.put('tempTxt', Js(', Rush of the Gale Spirits'), '+')
                            if (var.get('y')==Js(4.0)):
                                var.put('tempTxt', Js(', Shape of the Flowing River'), '+')
                            if (var.get('y')==Js(5.0)):
                                var.put('tempTxt', Js(', Sweeping Cinder Strike'), '+')
                            if (var.get('y')==Js(6.0)):
                                var.put('tempTxt', Js(', Water Whip'), '+')
                            if (var.get('y')==Js(7.0)):
                                var.put('tempTxt', Js(', Clench of the North Wind'), '+')
                            if (var.get('y')==Js(8.0)):
                                var.put('tempTxt', Js(', Gong of Summit'), '+')
                            if (var.get('abOutput').callprop('indexOf', var.get('tempTxt'))==(-Js(1.0))):
                                var.put('abOutput', var.get('tempTxt'), '+')
                                (var.put('i',Js(var.get('i').to_number())-Js(1))+Js(1))
                        var.put('abOutput', Js(')'), '+')
                        break
                    SWITCHED = True
                    break
            if (var.get('level')>Js(3.0)):
                var.put('abOutput', Js(', Slow Fall'), '+')
            if (var.get('level')>Js(4.0)):
                var.put('abOutput', Js(', Extra Attack, Stunning Strike'), '+')
            if (var.get('level')>Js(5.0)):
                var.put('abOutput', Js(', Ki-empowered Strikes'), '+')
            if ((var.get('level')>Js(5.0)) and (var.get('x')==Js(0.0))):
                var.put('abOutput', ((Js(', Wholeness of Body (')+(var.get('level')*Js(3.0)))+Js(' hit points)')), '+')
            if ((var.get('level')>Js(5.0)) and (var.get('x')==Js(1.0))):
                var.put('abOutput', Js(', Shadow Step'), '+')
            if (var.get('level')>Js(6.0)):
                var.put('abOutput', Js(', Evasion'), '+')
            if (var.get('level')>Js(6.0)):
                var.put('abOutput', Js(', Stillness of Mind'), '+')
            if (var.get('level')>Js(8.0)):
                var.put('abOutput', Js(', Unarmored Movement Improvement'), '+')
            if (var.get('level')>Js(9.0)):
                var.put('abOutput', Js(', Purity of Body'), '+')
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(9.0)):
            SWITCHED = True
            var.put('classtxt', Js('Paladin'))
            var.put('spellAbility', Js(5.0))
            var.put('ab1', Js(0.0))
            var.put('ab2', Js(5.0))
            var.put('bg', Js(8.0))
            var.put('hd', Js(10.0))
            var.put('st', Js([Js(4.0), Js(5.0)]))
            var.put('abOutput', ((Js('Divine Sense, Lay on Hands (')+(var.get('level')*Js(5.0)))+Js(' hp)')), '+')
            if (var.get('level')>Js(1.0)):
                var.put('x', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(4.0))))
                while 1:
                    SWITCHED = False
                    CONDITION = (var.get('x'))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(0.0)):
                        SWITCHED = True
                        var.put('temp', Js('Protection'))
                        var.put('fiStyle', Js(4.0))
                        break
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
                        SWITCHED = True
                        var.put('temp', Js('Defense'))
                        var.put('fiStyle', Js(1.0))
                        break
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                        SWITCHED = True
                        var.put('temp', Js('Dueling'))
                        var.put('fiStyle', Js(2.0))
                        break
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(3.0)):
                        SWITCHED = True
                        var.put('temp', Js('Great Weapon Fighting'))
                        var.put('fiStyle', Js(3.0))
                        break
                    SWITCHED = True
                    break
                var.put('abOutput', ((Js(', Fighting Style (')+var.get('temp'))+Js('),  Spellcasting, Divine Smite')), '+')
            if (var.get('level')>Js(2.0)):
                var.put('abOutput', Js(', Divine Health, Sacred Oath (Oath of '), '+')
                var.put('x', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(3.0))))
                if (var.get('forcePala')>(-Js(1.0))):
                    var.put('x', var.get('forcePala'))
                while 1:
                    SWITCHED = False
                    CONDITION = (var.get('x'))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(0.0)):
                        SWITCHED = True
                        var.put('abOutput', Js('Devotion), Sacred Weapon, Turn the Unholy'), '+')
                        var.get('oaSpells').callprop('push', Js('Protection from Evil and Good'))
                        var.get('oaSpells').callprop('push', Js('Sanctuary'))
                        if (var.get('level')>Js(4.0)):
                            var.get('oaSpells').callprop('push', Js('Lesser Restoration'))
                            var.get('oaSpells').callprop('push', Js('Zone of Truth'))
                        if (var.get('level')>Js(6.0)):
                            var.put('abOutput', Js(', Aura of Devotion'), '+')
                        if (var.get('level')>Js(8.0)):
                            var.get('oaSpells').callprop('push', Js('Beacon of Hope'))
                            var.get('oaSpells').callprop('push', Js('Dispel Magic'))
                        var.put('classtxt', Js(' (Oath of Devotion)'), '+')
                        break
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
                        SWITCHED = True
                        var.put('abOutput', Js("the Ancients), Nature's Wrath, Turn the Faithless"), '+')
                        var.get('oaSpells').callprop('push', Js('Ensnaring Strike'))
                        var.get('oaSpells').callprop('push', Js('Speak with Animals'))
                        if (var.get('level')>Js(4.0)):
                            var.get('oaSpells').callprop('push', Js('Moonbeam'))
                            var.get('oaSpells').callprop('push', Js('Misty Step'))
                        if (var.get('level')>Js(6.0)):
                            var.put('abOutput', Js(', Aura of Warding'), '+')
                        if (var.get('level')>Js(8.0)):
                            var.get('oaSpells').callprop('push', Js('Plant Growth'))
                            var.get('oaSpells').callprop('push', Js('Protection from Energy'))
                        var.put('classtxt', Js(' (Oath of the Ancients)'), '+')
                        break
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                        SWITCHED = True
                        var.put('abOutput', Js('Vengeance), Abjure Enemy, Vow of Enmity'), '+')
                        var.get('oaSpells').callprop('push', Js('Bane'))
                        var.get('oaSpells').callprop('push', Js("Hunter's Mark"))
                        if (var.get('level')>Js(4.0)):
                            var.get('oaSpells').callprop('push', Js('Hold Person'))
                            var.get('oaSpells').callprop('push', Js('Misty Step'))
                        if (var.get('level')>Js(6.0)):
                            var.put('abOutput', Js(', Relentless Avenger'), '+')
                        if (var.get('level')>Js(8.0)):
                            var.get('oaSpells').callprop('push', Js('Haste'))
                            var.get('oaSpells').callprop('push', Js('Protection from Energy'))
                        var.put('classtxt', Js(' (Oath of Vengeance)'), '+')
                        break
                    SWITCHED = True
                    break
            if (var.get('level')>Js(4.0)):
                var.put('abOutput', Js(', Extra Attack'), '+')
            if (var.get('level')>Js(5.0)):
                var.put('abOutput', Js(', Aura of Protection'), '+')
            if (var.get('level')>Js(9.0)):
                var.put('abOutput', Js(', Aura of Courage'), '+')
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(10.0)):
            SWITCHED = True
            var.put('classtxt', Js('Ranger'))
            var.put('spellAbility', Js(4.0))
            var.put('ab1', Js(1.0))
            var.put('ab2', Js(4.0))
            var.put('bg', Js(9.0))
            var.put('hd', Js(10.0))
            var.put('st', Js([Js(1.0), Js(0.0)]))
            var.put('i', Js(1.0))
            if (var.get('level')>Js(5.0)):
                var.put('i', Js(2.0))
            while (var.get('i')>Js(0.0)):
                if (var.get('Math').callprop('random')>Js(0.33)):
                    var.put('x', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('humanoids').get('length'))))
                    while (var.get('favored').callprop('indexOf', var.get('humanoids').get(var.get('x')))>(-Js(1.0))):
                        var.put('x', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('humanoids').get('length'))))
                    var.put('favored', (var.get('humanoids').get(var.get('x'))+Js(', ')), '+')
                    var.put('y', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('humanoids').get('length'))))
                    while (var.get('favored').callprop('indexOf', var.get('humanoids').get(var.get('y')))>(-Js(1.0))):
                        var.put('y', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('humanoids').get('length'))))
                    var.put('favored', var.get('humanoids').get(var.get('y')), '+')
                    if (var.get('i')==Js(2.0)):
                        var.put('favored', Js(', '), '+')
                    if (var.get('languageOutput').callprop('indexOf', var.get('humLangs').get(var.get('x')))==(-Js(1.0))):
                        var.put('languageOutput', (Js(', ')+var.get('humLangs').get(var.get('x'))), '+')
                    else:
                        if (var.get('languageOutput').callprop('indexOf', var.get('humLangs').get(var.get('y')))==(-Js(1.0))):
                            var.put('languageOutput', (Js(', ')+var.get('humLangs').get(var.get('y'))), '+')
                    (var.put('i',Js(var.get('i').to_number())-Js(1))+Js(1))
                else:
                    var.put('x', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('enemies').get('length'))))
                    while (var.get('favored').callprop('indexOf', var.get('enemies').get(var.get('x')))>(-Js(1.0))):
                        var.put('x', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('enemies').get('length'))))
                    var.put('favored', var.get('enemies').get(var.get('x')), '+')
                    if (var.get('favored').get('length')>Js(0.0)):
                        if (var.get('languageOutput').callprop('indexOf', var.get('enLangs').get(var.get('x')))==(-Js(1.0))):
                            var.put('languageOutput', (Js(', ')+var.get('enLangs').get(var.get('x'))), '+')
                    if (var.get('i')==Js(2.0)):
                        var.put('favored', Js(', '), '+')
                    (var.put('i',Js(var.get('i').to_number())-Js(1))+Js(1))
            var.put('i', Js(1.0))
            if (var.get('level')>Js(5.0)):
                var.put('i', Js(2.0))
            if (var.get('level')>Js(9.0)):
                var.put('i', Js(3.0))
            while (var.get('i')>Js(0.0)):
                var.put('x', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(8.0))))
                if (var.get('x')==Js(0.0)):
                    var.put('tempTxt', Js('Arctic'))
                if (var.get('x')==Js(1.0)):
                    var.put('tempTxt', Js('Coast'))
                if (var.get('x')==Js(2.0)):
                    var.put('tempTxt', Js('Desert'))
                if (var.get('x')==Js(3.0)):
                    var.put('tempTxt', Js('Forest'))
                if (var.get('x')==Js(4.0)):
                    var.put('tempTxt', Js('Grassland'))
                if (var.get('x')==Js(5.0)):
                    var.put('tempTxt', Js('Mountain'))
                if (var.get('x')==Js(6.0)):
                    var.put('tempTxt', Js('Swamp'))
                if (var.get('x')==Js(7.0)):
                    var.put('tempTxt', Js('Underdark'))
                if (var.get('land').callprop('indexOf', var.get('tempTxt'))==(-Js(1.0))):
                    var.put('land', var.get('tempTxt'), '+')
                    (var.put('i',Js(var.get('i').to_number())-Js(1))+Js(1))
                    if (var.get('i')>Js(0.0)):
                        var.put('land', Js(', '), '+')
            var.put('abOutput', ((((Js('Favored Enemy (')+var.get('favored'))+Js('), Natural Explorer ('))+var.get('land'))+Js(')')), '+')
            if (var.get('level')>Js(1.0)):
                var.put('x', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(4.0))))
                while 1:
                    SWITCHED = False
                    CONDITION = (var.get('x'))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(0.0)):
                        SWITCHED = True
                        var.put('temp', Js('Archery'))
                        var.put('fiStyle', Js(0.0))
                        break
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
                        SWITCHED = True
                        var.put('temp', Js('Defense'))
                        var.put('fiStyle', Js(1.0))
                        break
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                        SWITCHED = True
                        var.put('temp', Js('Dueling'))
                        var.put('fiStyle', Js(2.0))
                        break
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(3.0)):
                        SWITCHED = True
                        var.put('temp', Js('Two-weapon Fighting'))
                        var.put('fiStyle', Js(5.0))
                        break
                    SWITCHED = True
                    break
                var.put('abOutput', ((Js(', Fighting Style (')+var.get('temp'))+Js('), Spellcasting')), '+')
            if (var.get('level')>Js(2.0)):
                var.put('x', var.get('Math').callprop('random'))
                if (var.get('forceRang')>(-Js(1.0))):
                    var.put('x', var.get('forceRang'))
                if (var.get('x')<Js(0.5)):
                    var.put('classtxt', Js(' (Hunter)'), '+')
                    var.put('temp', Js('Hunter),  '))
                    var.put('x', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(3.0))))
                    if (var.get('x')==Js(0.0)):
                        var.put('temp', Js('Colossus Slayer'), '+')
                    if (var.get('x')==Js(1.0)):
                        var.put('temp', Js('Giant Killer'), '+')
                    if (var.get('x')==Js(2.0)):
                        var.put('temp', Js('Horde Breaker'), '+')
                    if (var.get('level')>Js(6.0)):
                        var.put('x', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(3.0))))
                        if (var.get('x')==Js(0.0)):
                            var.put('temp', Js(', Escape the Hoard'), '+')
                        if (var.get('x')==Js(1.0)):
                            var.put('temp', Js(', Multiattack Defense'), '+')
                        if (var.get('x')==Js(2.0)):
                            var.put('temp', Js(', Steel Will'), '+')
                else:
                    var.put('classtxt', Js(' (Beast Master)'), '+')
                    var.put('companion', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('companions').get('length'))))
                    var.put('companion', (var.get('companion')*Js(1.0)))
                    var.put('temp', Js('Beast Master)'))
                    if (var.get('level')>Js(6.0)):
                        var.put('temp', Js(', Exceptional Training'), '+')
                var.put('abOutput', ((Js(', Ranger Archetype (')+var.get('temp'))+Js(', Primeval Awareness')), '+')
            if (var.get('level')>Js(4.0)):
                var.put('abOutput', Js(', Extra Attack'), '+')
            if (var.get('level')>Js(7.0)):
                var.put('abOutput', Js(", Land's Stride"), '+')
            if (var.get('level')>Js(9.0)):
                var.put('abOutput', Js(', Hide in Plain Sight'), '+')
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(11.0)):
            SWITCHED = True
            var.put('classtxt', Js('Rogue'))
            var.put('ab1', Js(1.0))
            var.put('st', Js([Js(1.0), Js(3.0)]))
            if (var.get('Math').callprop('random')>Js(0.5)):
                var.put('ab2', Js(5.0))
            else:
                var.put('ab2', Js(3.0))
                var.put('ab3', Js(5.0))
            var.put('x', var.get('Math').callprop('random'))
            if (var.get('x')<Js(0.33)):
                var.put('bg', Js(2.0))
            else:
                if (var.get('x')<Js(0.66)):
                    var.put('bg', Js(3.0))
                else:
                    var.put('bg', Js(13.0))
            if (var.get('Math').callprop('random')<Js(0.5)):
                var.put('burglar', Js(True))
            var.put('x', Js(1.0))
            if (var.get('level')>Js(2.0)):
                var.put('x', Js(2.0))
            if (var.get('level')>Js(4.0)):
                var.put('x', Js(3.0))
            if (var.get('level')>Js(6.0)):
                var.put('x', Js(4.0))
            if (var.get('level')>Js(8.0)):
                var.put('x', Js(5.0))
            var.put('abOutput', ((Js('Expertise, Sneak Attack (')+var.get('x'))+Js("d6), Thieves' Cant")), '+')
            var.put('languageOutput', Js(", Thieves' Cant"), '+')
            if (var.get('level')>Js(1.0)):
                var.put('abOutput', Js(', Cunning Action'), '+')
            if (var.get('level')>Js(2.0)):
                var.put('x', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(2.0))))
                var.put('x', var.get('Math').callprop('random'))
                if (var.get('forceRogu')>(-Js(1.0))):
                    var.put('x', var.get('forceRogu'))
                if (var.get('x')==Js(0.0)):
                    var.put('temp', Js('Thief), Fast Hands, Second-Story Work'), '+')
                    var.put('classtxt', Js(' (Thief)'), '+')
                    if (var.get('level')>Js(8.0)):
                        var.put('temp', Js(', Supreme Sneak'), '+')
                if (var.get('x')==Js(1.0)):
                    var.put('temp', Js('Assassin), Assassinate'), '+')
                    var.put('toOutput', Js(", Disguise kit, Poisoner's kit"), '+')
                    var.put('classtxt', Js(' (Assassin)'), '+')
                    if (var.get('level')>Js(8.0)):
                        var.put('temp', Js(', Infiltration Expertise'), '+')
                var.put('abOutput', (Js(', Roguish Archetype (')+var.get('temp')), '+')
            if (var.get('level')>Js(4.0)):
                var.put('abOutput', Js(', Uncanny Dodge'), '+')
            if (var.get('level')>Js(5.0)):
                var.put('abOutput', Js(', Expertise'), '+')
            if (var.get('level')>Js(6.0)):
                var.put('abOutput', Js(', Evasion'), '+')
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(12.0)):
            SWITCHED = True
            var.put('classtxt', Js('Rogue'))
            var.put('spellAbility', Js(3.0))
            var.put('ab1', Js(1.0))
            var.put('ab2', Js(3.0))
            var.put('bg', Js(2.0))
            var.put('st', Js([Js(1.0), Js(3.0)]))
            if (var.get('Math').callprop('random')<Js(0.5)):
                var.put('burglar', Js(True))
            var.put('x', Js(1.0))
            if (var.get('level')>Js(2.0)):
                var.put('x', Js(2.0))
            if (var.get('level')>Js(4.0)):
                var.put('x', Js(3.0))
            if (var.get('level')>Js(6.0)):
                var.put('x', Js(4.0))
            if (var.get('level')>Js(8.0)):
                var.put('x', Js(5.0))
            var.put('abOutput', ((Js('Expertise, Sneak Attack (')+var.get('x'))+Js("d6), Thieves' Cant")), '+')
            var.put('languageOutput', Js(", Thieves' Cant"), '+')
            if (var.get('level')>Js(1.0)):
                var.put('abOutput', Js(', Cunning Action'), '+')
            if (var.get('level')>Js(2.0)):
                var.put('classtxt', Js(' (Arcane Trickster)'), '+')
                var.put('abOutput', Js(', Roguish Archetype (Arcane Trickster), Spellcasting'), '+')
                if (var.get('level')>Js(8.0)):
                    var.put('abOutput', Js(', Magical Ambush'), '+')
            if (var.get('level')>Js(4.0)):
                var.put('abOutput', Js(', Uncanny Dodge'), '+')
            if (var.get('level')>Js(5.0)):
                var.put('abOutput', Js(', Expertise'), '+')
            if (var.get('level')>Js(6.0)):
                var.put('abOutput', Js(', Evasion'), '+')
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(13.0)):
            SWITCHED = True
            var.put('classtxt', Js('Sorcerer ('))
            var.put('ab1', Js(5.0))
            var.put('spellAbility', Js(5.0))
            var.put('ab2', Js(2.0))
            var.put('bg', Js(6.0))
            var.put('hd', Js(6.0))
            var.put('st', Js([Js(5.0), Js(2.0)]))
            var.put('abOutput', Js('Spellcasting'), '+')
            var.put('soOrigin', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(2.0))))
            if (var.get('forceSorc')>(-Js(1.0))):
                var.put('soOrigin', var.get('forceSorc'))
            while 1:
                SWITCHED = False
                CONDITION = (var.get('soOrigin'))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(0.0)):
                    SWITCHED = True
                    var.put('classtxt', Js('Draconic Bloodline)'), '+')
                    if (var.get('racetxt')!=Js('Dragonborn')):
                        var.put('tempAr', var.get('dragon')())
                        var.put('dragType', var.get('tempAr').get('0'))
                        var.put('elemType', var.get('tempAr').get('1'))
                        var.put('abOutput', ((((Js(', Draconic Ancestry (')+var.get('dragType'))+Js(', '))+var.get('elemType'))+Js(' damage)')), '+')
                    var.put('abOutput', Js(', Draconic Resilience'), '+')
                    var.put('languageOutput', Js(', Draconic'), '+')
                    if (var.get('level')>Js(5.0)):
                        var.put('abOutput', Js(', Elemental Affinity'), '+')
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
                    SWITCHED = True
                    var.put('classtxt', Js('Wild Magic)'), '+')
                    var.put('abOutput', Js(', Wild Magic Surge, Tides of Chaos'), '+')
                    if (var.get('level')>Js(5.0)):
                        var.put('abOutput', Js(', Bend Luck'), '+')
                    break
                SWITCHED = True
                break
            if (var.get('level')>Js(1.0)):
                var.put('abOutput', Js(', Font of Magic'), '+')
            if (var.get('level')>Js(2.0)):
                var.put('abOutput', Js(', Metamagic '), '+')
                var.get('pickMeta')()
            if (var.get('level')>Js(1.0)):
                var.put('abOutput', ((Js(', ')+var.get('level'))+Js(' sorcery points')), '+')
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(14.0)):
            SWITCHED = True
            var.put('classtxt', Js('Warlock ('))
            var.put('ab1', Js(5.0))
            var.put('spellAbility', Js(5.0))
            if (var.get('Math').callprop('random')<Js(0.5)):
                var.put('ab3', Js(1.0))
            else:
                var.put('ab3', Js(0.0))
            var.put('ab2', Js(2.0))
            var.put('bg', Js(2.0))
            var.put('st', Js([Js(4.0), Js(5.0)]))
            var.put('abOutput', Js('Otherworldly Patron ('), '+')
            var.put('waPatron', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(3.0))))
            if (var.get('forceWarl')>(-Js(1.0))):
                var.put('waPatron', var.get('forceWarl'))
            while 1:
                SWITCHED = False
                CONDITION = (var.get('waPatron'))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(0.0)):
                    SWITCHED = True
                    var.put('classtxt', Js('Archfey'), '+')
                    var.get('patronSpells1').callprop('push', Js('Faerie Fire'))
                    var.get('patronSpells1').callprop('push', Js('Sleep'))
                    var.get('patronSpells2').callprop('push', Js('Calm Emotions'))
                    var.get('patronSpells2').callprop('push', Js('Phantasmal Force'))
                    var.get('patronSpells3').callprop('push', Js('Blink'))
                    var.get('patronSpells3').callprop('push', Js('Plant Growth'))
                    var.get('patronSpells4').callprop('push', Js('Dominate Beast'))
                    var.get('patronSpells4').callprop('push', Js('Greater Invisibility'))
                    var.get('patronSpells5').callprop('push', Js('Dominate Person'))
                    var.get('patronSpells5').callprop('push', Js('Seeming'))
                    var.get('patronSpells1').callprop('push', Js('Faerie Fire'))
                    var.get('patronSpells1').callprop('push', Js('Sleep'))
                    var.get('patronSpells2').callprop('push', Js('Calm Emotions'))
                    var.get('patronSpells2').callprop('push', Js('Phantasmal Force'))
                    var.get('patronSpells3').callprop('push', Js('Blink'))
                    var.get('patronSpells3').callprop('push', Js('Plant Growth'))
                    var.get('patronSpells4').callprop('push', Js('Dominate Beast'))
                    var.get('patronSpells4').callprop('push', Js('Greater Invisibility'))
                    var.get('patronSpells5').callprop('push', Js('Dominate Person'))
                    var.get('patronSpells5').callprop('push', Js('Seeming'))
                    var.put('abOutput', Js('Archfey), Fey Presence'), '+')
                    if (var.get('level')>Js(5.0)):
                        var.put('abOutput', Js(', Misty Escape'), '+')
                    if (var.get('level')>Js(9.0)):
                        var.put('abOutput', Js(', Beguiling Defenses'), '+')
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
                    SWITCHED = True
                    var.put('classtxt', Js('Fiend'), '+')
                    var.get('patronSpells1').callprop('push', Js('Burning Hands'))
                    var.get('patronSpells1').callprop('push', Js('Command'))
                    var.get('patronSpells2').callprop('push', Js('Blindness/Deafness'))
                    var.get('patronSpells2').callprop('push', Js('Scorching Ray'))
                    var.get('patronSpells3').callprop('push', Js('Fireball'))
                    var.get('patronSpells3').callprop('push', Js('Stinking Cloud'))
                    var.get('patronSpells4').callprop('push', Js('Fire Shield'))
                    var.get('patronSpells4').callprop('push', Js('Wall of Fire'))
                    var.get('patronSpells5').callprop('push', Js('Flame Strike'))
                    var.get('patronSpells5').callprop('push', Js('Hallow'))
                    var.get('patronSpells1').callprop('push', Js('Burning Hands'))
                    var.get('patronSpells1').callprop('push', Js('Command'))
                    var.get('patronSpells2').callprop('push', Js('Blindness/Deafness'))
                    var.get('patronSpells2').callprop('push', Js('Scorching Ray'))
                    var.get('patronSpells3').callprop('push', Js('Fireball'))
                    var.get('patronSpells3').callprop('push', Js('Stinking Cloud'))
                    var.get('patronSpells4').callprop('push', Js('Fire Shield'))
                    var.get('patronSpells4').callprop('push', Js('Wall of Fire'))
                    var.get('patronSpells5').callprop('push', Js('Flame Strike'))
                    var.get('patronSpells5').callprop('push', Js('Hallow'))
                    var.put('abOutput', Js("Fiend), Dark One's Blessing"), '+')
                    if (var.get('level')>Js(5.0)):
                        var.put('abOutput', Js(", Dark One's Own Luck"), '+')
                    if (var.get('level')>Js(9.0)):
                        var.put('abOutput', Js(', Fiendish Resilience'), '+')
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                    SWITCHED = True
                    var.put('classtxt', Js('Great Old One'), '+')
                    var.get('patronSpells1').callprop('push', Js('Dissonant Whispers'))
                    var.get('patronSpells1').callprop('push', Js("Tasha's Hideous Laughter"))
                    var.get('patronSpells2').callprop('push', Js('Detect Thoughts'))
                    var.get('patronSpells2').callprop('push', Js('Phantasmal Force'))
                    var.get('patronSpells3').callprop('push', Js('Clairvoyance'))
                    var.get('patronSpells3').callprop('push', Js('Sending'))
                    var.get('patronSpells4').callprop('push', Js('Dominate Beast'))
                    var.get('patronSpells4').callprop('push', Js("Evard's Black Tentacles"))
                    var.get('patronSpells5').callprop('push', Js('Dominate Person'))
                    var.get('patronSpells5').callprop('push', Js('Telekinesis'))
                    var.get('patronSpells1').callprop('push', Js('Dissonant Whispers'))
                    var.get('patronSpells1').callprop('push', Js("Tasha's Hideous Laughter"))
                    var.get('patronSpells2').callprop('push', Js('Detect Thoughts'))
                    var.get('patronSpells2').callprop('push', Js('Phantasmal Force'))
                    var.get('patronSpells3').callprop('push', Js('Clairvoyance'))
                    var.get('patronSpells3').callprop('push', Js('Sending'))
                    var.get('patronSpells4').callprop('push', Js('Dominate Beast'))
                    var.get('patronSpells4').callprop('push', Js("Evard's Black Tentacles"))
                    var.get('patronSpells5').callprop('push', Js('Dominate Person'))
                    var.get('patronSpells5').callprop('push', Js('Telekinesis'))
                    var.put('abOutput', Js('Great Old One), Awakened Mind'), '+')
                    if (var.get('level')>Js(5.0)):
                        var.put('abOutput', Js(', Entropic Ward'), '+')
                    if (var.get('level')>Js(9.0)):
                        var.put('abOutput', Js(', Thought Shield'), '+')
                    break
                SWITCHED = True
                break
            var.put('classtxt', Js(' Patron'), '+')
            var.put('abOutput', Js(', Pact Magic'), '+')
            if (var.get('level')>Js(2.0)):
                var.put('tempTxt', Js(', Pact Boon (Pact of the '), '+')
                var.put('x', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(3.0))))
                if (var.get('forceWarlPact')>(-Js(1.0))):
                    var.put('x', var.get('forceWarlPact'))
                while 1:
                    SWITCHED = False
                    CONDITION = (var.get('x'))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(0.0)):
                        SWITCHED = True
                        var.put('classtxt', Js(', Chain Pact'), '+')
                        var.put('tempTxt', Js('Chain)'), '+')
                        if (var.get('waPatron')==Js(0.0)):
                            if (var.get('Math').callprop('random')<Js(0.5)):
                                var.put('familiar', Js('Sprite - 2 hit points, 15 AC, <i>Heart Sight, Invisibility</i>, Longsword +2 to hit (1 dmg), Shortbow +6 to hit (1 dmg, check if poisoned) Range 40/160'))
                            else:
                                var.put('familiar', Js('Pseudodragon - 7 hit points, 13 AC, <i>Keen Senses, Magic Resistance, Limited Telepathy</i>, Bite +4 to hit (1d4 +2 dmg), Sting +4 to hit (1d4 +2 dmg, check if poisoned)'))
                        if (var.get('waPatron')==Js(1.0)):
                            if (var.get('Math').callprop('random')<Js(0.5)):
                                var.put('familiar', Js('Quasit - 7 hit points, 13 AC, <i>Shapechanger, Magic Resistance, Scare, Invisibility,</i> Claws +4 to hit (1d4+3 dmg, check if poisoned)'))
                            else:
                                var.put('familiar', Js("Imp  - 10 hit points, 13 AC, <i>Shapechanger, Devil's Sight, Magic Resistance, Invisibility</i>, Sting +5 to hit (1d4 +3 dmg, check for 3d6 poison dmg)"))
                        if (var.get('waPatron')==Js(2.0)):
                            var.put('y', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(4.0))))
                            if (var.get('y')==Js(0.0)):
                                var.put('familiar', Js("Imp  - 10 hit points, 13 AC, <i>Shapechanger, Devil's Sight, Magic Resistance, Invisibility</i>, Sting +5 to hit (1d4 +3 dmg, check for 3d6 poison dmg)"))
                            if (var.get('y')==Js(1.0)):
                                var.put('familiar', Js('Pseudodragon - 7 hit points, 13 AC, <i>Keen Senses, Magic Resistance, Limited Telepathy</i>, Bite +4 to hit (1d4 +2 dmg), Sting +4 to hit (1d4 +2 dmg, check if poisoned)'))
                            if (var.get('y')==Js(2.0)):
                                var.put('familiar', Js('Quasit - 7 hit points, 13 AC, <i>Shapechanger, Magic Resistance, Scare, Invisibility,</i> Claws +4 to hit (1d4+3 dmg, check if poisoned)'))
                            if (var.get('y')==Js(3.0)):
                                var.put('familiar', Js('Sprite - 2 hit points, 15 AC, <i>Heart Sight, Invisibility</i>, Longsword +2 to hit (1 dmg), Shortbow +6 to hit (1 dmg, check if poisoned) Range 40/160'))
                        var.get('mySpells').callprop('push', Js('Find Familiar'))
                        break
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
                        SWITCHED = True
                        var.put('classtxt', Js(', Blade Pact'), '+')
                        var.put('tempTxt', Js('Blade)'), '+')
                        break
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                        SWITCHED = True
                        var.put('classtxt', Js(', Tome Pact'), '+')
                        var.put('tempTxt', Js('Tome)'), '+')
                        var.put('tome', Js(True))
                        break
                    SWITCHED = True
                    break
            var.put('classtxt', Js(')'), '+')
            if (var.get('level')>Js(1.0)):
                var.put('abOutput', Js(', Eldritch Invocations '), '+')
                var.put('tempAr', var.get('pickEldritch')())
                if (var.get('tempAr').callprop('indexOf', Js('Beguiling Influence'))>(-Js(1.0))):
                    var.get('skLearn').put('4', Js(True))
                    var.get('mySkills').callprop('push', Js(4.0))
                    var.get('mySkills').callprop('push', Js(13.0))
                    var.get('skLearn').put('13', Js(True))
                if (var.get('tempAr').callprop('indexOf', Js('Eldritch Sight'))>(-Js(1.0))):
                    var.get('waSpells').callprop('push', Js('Detect Magic'))
                if (var.get('tempAr').callprop('indexOf', Js('Armor of Shadows'))>(-Js(1.0))):
                    var.get('waSpells').callprop('push', Js('Mage Armor'))
                if (var.get('tempAr').callprop('indexOf', Js('Agonizing Blast'))>(-Js(1.0))):
                    var.put('eblast', Js(True))
                if (var.get('tempAr').callprop('indexOf', Js('Eldritch Spear'))>(-Js(1.0))):
                    var.put('eblast', Js(True))
                if (var.get('tempAr').callprop('indexOf', Js('Repelling Blast'))>(-Js(1.0))):
                    var.put('eblast', Js(True))
                if (var.get('tempAr').callprop('indexOf', Js('Beast Speech'))>(-Js(1.0))):
                    var.get('waSpells').callprop('push', Js('Speak with Animals'))
                if (var.get('tempAr').callprop('indexOf', Js('Fiendish Vigor'))>(-Js(1.0))):
                    var.get('waSpells').callprop('push', Js('False Life'))
                if (var.get('tempAr').callprop('indexOf', Js('Many Faces'))>(-Js(1.0))):
                    var.get('waSpells').callprop('push', Js('Disguise Self'))
                if (var.get('tempAr').callprop('indexOf', Js('Misty Visions'))>(-Js(1.0))):
                    var.get('waSpells').callprop('push', Js('Silent Image'))
                if (var.get('tempAr').callprop('indexOf', Js('Whispers of the Grave'))>(-Js(1.0))):
                    var.get('waSpells').callprop('push', Js('Speak with Dead'))
                if (var.get('tempAr').callprop('indexOf', Js('Otherworldly Leap'))>(-Js(1.0))):
                    var.get('waSpells').callprop('push', Js('Jump'))
                if (var.get('tempAr').callprop('indexOf', Js('Ascendant Step'))>(-Js(1.0))):
                    var.get('waSpells').callprop('push', Js('Levitate (on self)'))
                if (var.get('tempAr').callprop('indexOf', Js('Thief of Five Fates'))>(-Js(1.0))):
                    var.get('waSpells').callprop('push', Js('Bane (once per long rest)'))
                if (var.get('tempAr').callprop('indexOf', Js('Mire the Mind'))>(-Js(1.0))):
                    var.get('waSpells').callprop('push', Js('Slow (once per long rest)'))
                if (var.get('tempAr').callprop('indexOf', Js('Ill Omen'))>(-Js(1.0))):
                    var.get('waSpells').callprop('push', Js('Bestow Curse (once per long rest)'))
                if (var.get('tempAr').callprop('indexOf', Js('Bewitching Whispers'))>(-Js(1.0))):
                    var.get('waSpells').callprop('push', Js('Compulsion (once per long rest)'))
                if (var.get('tempAr').callprop('indexOf', Js('Dreadful Word'))>(-Js(1.0))):
                    var.get('waSpells').callprop('push', Js('Confusion (once per long rest, uses a spell slot)'))
                if (var.get('tempAr').callprop('indexOf', Js('Minions of Chaos'))>(-Js(1.0))):
                    var.get('waSpells').callprop('push', Js('Conjure Elemental (once per long rest, uses a spell slot)'))
                if (var.get('tempAr').callprop('indexOf', Js('Sculptor of Flesh'))>(-Js(1.0))):
                    var.get('waSpells').callprop('push', Js('Polymorph (once per long rest, uses a spell slot)'))
                var.put('abOutput', var.get('tempTxt'), '+')
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(15.0)):
            SWITCHED = True
            var.put('classtxt', Js('Wizard'))
            var.put('spellAbility', Js(3.0))
            var.put('ab1', Js(3.0))
            var.put('ab2', Js(1.0))
            var.put('hd', Js(6.0))
            var.put('bg', Js(10.0))
            var.put('st', Js([Js(3.0), Js(4.0)]))
            var.put('abOutput', Js('Spellcasting, Arcane Recovery'), '+')
            if (var.get('level')>Js(1.0)):
                var.put('schools', Js([Js('Abjuration'), Js('Conjuration'), Js('Divination'), Js('Enchantment'), Js('Evocation'), Js('Illusion'), Js('Necromancy'), Js('Transmutation')]))
                var.put('wiSchool', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('schools').get('length'))))
                if ((var.get('forceSchool')>(-Js(1.0))) and (var.get('magicGet')(Js('selClass'), var.get('possibile')).get('value')==Js(15.0))):
                    var.put('wiSchool', var.get('forceSchool'))
                var.put('classtxt', ((Js(' (')+var.get('schools').get(var.get('wiSchool')))+Js(' school)')), '+')
                var.put('abOutput', ((Js(', Arcane Tradition (')+var.get('schools').get(var.get('wiSchool')))+Js(' school)')), '+')
                while 1:
                    SWITCHED = False
                    CONDITION = (var.get('wiSchool'))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(0.0)):
                        SWITCHED = True
                        var.put('abOutput', Js(', Abjuration Savant, Arcane Ward'), '+')
                        if (var.get('level')>Js(5.0)):
                            var.put('abOutput', Js(', Projected Ward'), '+')
                        if (var.get('level')>Js(9.0)):
                            var.put('abOutput', Js(', Improved Abjuration'), '+')
                        break
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
                        SWITCHED = True
                        var.put('abOutput', Js(', Conjuration Savant, Minor Conjuration'), '+')
                        if (var.get('level')>Js(5.0)):
                            var.put('abOutput', Js(', Benign Transposition'), '+')
                        if (var.get('level')>Js(9.0)):
                            var.put('abOutput', Js(', Focused Conjuration'), '+')
                        break
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                        SWITCHED = True
                        var.put('abOutput', Js(', Divination Savant, Portent'), '+')
                        if (var.get('level')>Js(5.0)):
                            var.put('abOutput', Js(', Expert Divination'), '+')
                        if (var.get('level')>Js(9.0)):
                            var.put('abOutput', Js(', The Third Eye'), '+')
                        break
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(3.0)):
                        SWITCHED = True
                        var.put('abOutput', Js(', Enchantment Savant, Hypnotic Gaze'), '+')
                        if (var.get('level')>Js(5.0)):
                            var.put('abOutput', Js(', Instinctive Charm'), '+')
                        if (var.get('level')>Js(9.0)):
                            var.put('abOutput', Js(', Split Enchantment'), '+')
                        break
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(4.0)):
                        SWITCHED = True
                        var.put('abOutput', Js(', Evocation Savant, Sculpt Spells'), '+')
                        if (var.get('level')>Js(5.0)):
                            var.put('abOutput', Js(', Potent Cantrip'), '+')
                        if (var.get('level')>Js(9.0)):
                            var.put('abOutput', Js(', Empowered Evocation'), '+')
                        break
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(5.0)):
                        SWITCHED = True
                        var.put('abOutput', Js(', Illusion Savant, Improved Minor Illusion'), '+')
                        var.get('mySpells').callprop('unshift', Js('Minor Illusion'))
                        if (var.get('level')>Js(5.0)):
                            var.put('abOutput', Js(', Malleable Illusions'), '+')
                        if (var.get('level')>Js(9.0)):
                            var.put('abOutput', Js(', Illusory Self'), '+')
                        break
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(6.0)):
                        SWITCHED = True
                        var.put('abOutput', Js(', Necromancy Savant, Grim Harvest'), '+')
                        if (var.get('level')>Js(5.0)):
                            var.put('abOutput', Js(', Undead Thralls'), '+')
                        if (var.get('level')>Js(9.0)):
                            var.put('abOutput', Js(', Inured to Undeath'), '+')
                        break
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(7.0)):
                        SWITCHED = True
                        var.put('abOutput', Js(', Transmutation Savant, Minor Alchemy'), '+')
                        if (var.get('level')>Js(5.0)):
                            var.put('abOutput', Js(", Transmuter's Stone"), '+')
                        if (var.get('level')>Js(9.0)):
                            var.put('abOutput', Js(', Shapechanger'), '+')
                        break
                    SWITCHED = True
                    break
            break
        SWITCHED = True
        break
    if (var.get('magicGet')(Js('genMethod'), var.get('possibile')).get('value')!=Js('3')):
        var.get('abil').put(var.get('ab1'), var.get('abilRaw').callprop('shift'), '+')
        var.get('abil').put(var.get('ab2'), var.get('abilRaw').callprop('shift'), '+')
        if (var.get('ab3')>(-Js(1.0))):
            var.get('abil').put(var.get('ab3'), var.get('abilRaw').callprop('shift'), '+')
        if (var.get('abil').get('2')<Js(3.0)):
            var.get('abil').put('2', var.get('abilRaw').callprop('shift'), '+')
        while (var.get('abilRaw').get('length')>Js(0.0)):
            var.put('x', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(6.0))))
            if (var.get('abil').get(var.get('x'))<Js(3.0)):
                var.get('abil').put(var.get('x'), var.get('abilRaw').callprop('shift'), '+')
    var.get('console').callprop('log', Js('1st level abilities before any increases:'))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(6.0)):
        try:
            var.get('console').callprop('log', ((var.get('abilNames').get(var.get('i'))+Js(': '))+var.get('abil').get(var.get('i'))))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    var.put('i', Js(0.0))
    if (var.get('level')>Js(3.0)):
        var.put('abOutput', Js(', Ability Score Improvement (4th'), '+')
        var.get('console').callprop('log', Js('4th level ability bonus +2'))
        var.put('x', Js(2.0))
        if (((var.get('cl')==Js(5.0)) or (var.get('cl')==Js(6.0))) or (var.get('cl')==Js(7.0))):
            if (var.get('level')>Js(7.0)):
                var.put('abOutput', Js(', 6th and 8th levels'), '+')
            else:
                if (var.get('level')>Js(5.0)):
                    var.put('abOutput', Js(' and 6th levels'), '+')
                else:
                    var.put('abOutput', Js(' level'), '+')
        else:
            if ((var.get('cl')==Js(11.0)) or (var.get('cl')==Js(12.0))):
                if (var.get('level')>Js(9.0)):
                    var.put('abOutput', Js(', 8th and 10th levels'), '+')
                else:
                    if (var.get('level')>Js(7.0)):
                        var.put('abOutput', Js(' and 8th levels'), '+')
                    else:
                        var.put('abOutput', Js(' level'), '+')
            else:
                if (var.get('level')>Js(7.0)):
                    var.put('abOutput', Js(' and 8th levels'), '+')
                else:
                    var.put('abOutput', Js(' level'), '+')
        if ((var.get('level')>Js(5.0)) and (((var.get('cl')==Js(5.0)) or (var.get('cl')==Js(6.0))) or (var.get('cl')==Js(7.0)))):
            var.put('x', (var.get('x')+Js(2.0)))
        if (var.get('level')>Js(7.0)):
            var.put('x', (var.get('x')+Js(2.0)))
        if ((var.get('level')>Js(9.0)) and ((var.get('cl')==Js(11.0)) or (var.get('cl')==Js(12.0)))):
            var.put('x', (var.get('x')+Js(2.0)))
        var.put('abOutput', Js(' '), '+')
        while (var.get('x')>Js(0.0)):
            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            if (var.get('i')>Js(500.0)):
                var.get('alert')(Js('500 tries adding  ability bonus'))
            var.put('xx', Js(0.0))
            if ((var.get('abil').get(var.get('ab1'))%Js(2.0))==Js(1.0)):
                var.put('xx', Js(1.0))
            else:
                if ((var.get('abil').get(var.get('ab2'))%Js(2.0))==Js(1.0)):
                    var.put('xx', Js(2.0))
                else:
                    if ((var.get('abil').get('2')%Js(2.0))==Js(1.0)):
                        var.put('xx', Js(3.0))
                    else:
                        if (var.get('Math').callprop('random')>Js(0.6)):
                            var.put('xx', Js(5.0))
                        else:
                            if ((var.get('abil').get(var.get('ab3'))%Js(2.0))==Js(1.0)):
                                var.put('xx', Js(6.0))
                            else:
                                if (var.get('abil').get(var.get('ab1'))<Js(20.0)):
                                    var.put('xx', Js(1.0))
                                else:
                                    if (var.get('abil').get(var.get('ab2'))<Js(20.0)):
                                        var.put('xx', Js(2.0))
                                    else:
                                        var.put('xx', Js(4.0))
            if (var.get('xx')==Js(1.0)):
                var.get('abil').put(var.get('ab1'), (var.get('abil').get(var.get('ab1'))+Js(1.0)))
                (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
                var.get('console').callprop('log', ((Js('primary class abil, ')+var.get('abilNames').get(var.get('ab1')))+Js(' +1 point')))
                var.get('abilIncrease').put(var.get('ab1'), (var.get('abilIncrease').get(var.get('ab1'))+Js(1.0)))
            else:
                if (var.get('xx')==Js(2.0)):
                    var.get('abil').put(var.get('ab2'), (var.get('abil').get(var.get('ab2'))+Js(1.0)))
                    (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
                    var.get('console').callprop('log', ((Js('secondary class abil, ')+var.get('abilNames').get(var.get('ab2')))+Js('+1 point')))
                    var.get('abilIncrease').put(var.get('ab2'), (var.get('abilIncrease').get(var.get('ab2'))+Js(1.0)))
                else:
                    if (var.get('xx')==Js(3.0)):
                        var.get('abil').put('2', (var.get('abil').get('2')+Js(1.0)))
                        (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
                        var.get('console').callprop('log', ((Js('constitution, ')+var.get('abilNames').get('2'))+Js('+1 point')))
                        var.get('abilIncrease').put('2', (var.get('abilIncrease').get('2')+Js(1.0)))
                    else:
                        if (var.get('xx')==Js(4.0)):
                            var.put('y', Js(20.0))
                            #for JS loop
                            var.put('z', Js(0.0))
                            while (var.get('z')<Js(6.0)):
                                try:
                                    if (var.get('abil').get(var.get('z'))<var.get('y')):
                                        var.put('y', var.get('abil').get(var.get('z')))
                                finally:
                                        (var.put('z',Js(var.get('z').to_number())+Js(1))-Js(1))
                            var.get('console').callprop('log', (Js('lowest score = ')+var.get('y')))
                            var.put('bool', Js(False))
                            var.put('z', Js(0.0))
                            while (var.get('bool')==Js(False)):
                                if (var.get('abil').get(var.get('z'))==var.get('y')):
                                    var.get('abil').put(var.get('z'), (var.get('abil').get(var.get('z'))+Js(1.0)))
                                    var.get('console').callprop('log', (var.get('abilNames').get(var.get('z'))+Js(' +1 point')))
                                    (var.get('abilIncrease').put(var.get('z'),Js(var.get('abilIncrease').get(var.get('z')).to_number())+Js(1))-Js(1))
                                    var.put('bool', Js(True))
                                    (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
                                (var.put('z',Js(var.get('z').to_number())+Js(1))-Js(1))
                        else:
                            if (var.get('xx')==Js(5.0)):
                                var.put('y', Js(10.0))
                                #for JS loop
                                var.put('z', Js(0.0))
                                while (var.get('z')<Js(6.0)):
                                    try:
                                        if ((var.get('abil').get(var.get('z'))<var.get('y')) and ((var.get('abil').get(var.get('z'))%Js(2.0))==Js(1.0))):
                                            var.put('y', var.get('abil').get(var.get('z')))
                                            var.put('yy', var.get('z'))
                                    finally:
                                            (var.put('z',Js(var.get('z').to_number())+Js(1))-Js(1))
                                var.get('console').callprop('log', (Js('lowest odd # score = ')+var.get('y')))
                                if (var.get('y')<Js(10.0)):
                                    var.get('abil').put(var.get('yy'), (var.get('abil').get(var.get('yy'))+Js(1.0)))
                                    var.get('console').callprop('log', (var.get('abilNames').get(var.get('yy'))+Js(' +1 point')))
                                    (var.get('abilIncrease').put(var.get('yy'),Js(var.get('abilIncrease').get(var.get('yy')).to_number())+Js(1))-Js(1))
                                    (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
                            else:
                                if (var.get('xx')==Js(6.0)):
                                    var.get('abil').put(var.get('ab3'), (var.get('abil').get(var.get('ab3'))+Js(1.0)))
                                    (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
                                    var.get('console').callprop('log', ((Js('third class abil because it was odd, ')+var.get('abilNames').get(var.get('ab3')))+Js(' +1 point')))
                                    var.get('abilIncrease').put(var.get('ab3'), (var.get('abilIncrease').get(var.get('ab3'))+Js(1.0)))
        var.put('bool', Js(False))
        #for JS loop
        var.put('x', Js(0.0))
        while (var.get('x')<Js(6.0)):
            try:
                if (var.get('abilIncrease').get(var.get('x'))>Js(0.0)):
                    if (var.get('bool')==Js(True)):
                        var.put('abOutput', Js(', '), '+')
                    var.put('abOutput', ((var.get('showPlus')(var.get('abilIncrease').get(var.get('x')))+Js(' '))+var.get('abilNames').get(var.get('x'))), '+')
                    var.put('bool', Js(True))
            finally:
                    (var.put('x',Js(var.get('x').to_number())+Js(1))-Js(1))
        var.put('abOutput', Js(')'), '+')
    var.get('console').callprop('log', var.get('abilIncrease'))
    if (var.get('racetxt')==Js('Half-Elf')):
        var.get('console').callprop('log', Js('Half elf ability bonus +2'))
        var.put('i', Js(0.0))
        var.put('x', Js(2.0))
        while (var.get('x')>Js(0.0)):
            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            if (var.get('i')>Js(500.0)):
                var.get('alert')(Js('500 tries adding half elf ability bonus'))
            if (((var.get('abil').get(var.get('ab1'))<Js(20.0)) and (var.get('ab1')!=Js(5.0))) and (var.get('firstIncrease')!=var.get('ab1'))):
                var.get('abil').put(var.get('ab1'), (var.get('abil').get(var.get('ab1'))+Js(1.0)))
                (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
                var.get('console').callprop('log', ((Js('main class ability, ')+var.get('abilNames').get(var.get('ab1')))+Js(' +1 point')))
                (var.get('abilIncrease').put(var.get('ab1'),Js(var.get('abilIncrease').get(var.get('ab1')).to_number())+Js(1))-Js(1))
                var.put('firstIncrease', var.get('ab1'))
            else:
                if (((var.get('abil').get(var.get('ab2'))<Js(20.0)) and (var.get('ab2')!=Js(5.0))) and (var.get('firstIncrease')!=var.get('ab2'))):
                    var.get('abil').put(var.get('ab2'), (var.get('abil').get(var.get('ab2'))+Js(1.0)))
                    (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
                    var.get('console').callprop('log', ((Js('secondary class ability, ')+var.get('abilNames').get(var.get('ab2')))+Js(' +1 point')))
                    (var.get('abilIncrease').put(var.get('ab2'),Js(var.get('abilIncrease').get(var.get('ab2')).to_number())+Js(1))-Js(1))
                    var.put('firstIncrease', var.get('ab2'))
                else:
                    var.put('y', Js(20.0))
                    #for JS loop
                    var.put('z', Js(0.0))
                    while (var.get('z')<Js(6.0)):
                        try:
                            if (var.get('abil').get(var.get('z'))<var.get('y')):
                                var.put('y', var.get('abil').get(var.get('z')))
                        finally:
                                (var.put('z',Js(var.get('z').to_number())+Js(1))-Js(1))
                    var.get('console').callprop('log', (Js('lowest score = ')+var.get('y')))
                    var.put('bool', Js(False))
                    var.put('z', Js(0.0))
                    while (var.get('bool')==Js(False)):
                        if (var.get('abil').get(var.get('z'))==var.get('y')):
                            var.get('abil').put(var.get('z'), (var.get('abil').get(var.get('z'))+Js(1.0)))
                            var.get('console').callprop('log', (var.get('abilNames').get(var.get('z'))+Js(' +1 point')))
                            (var.get('abilIncrease').put(var.get('z'),Js(var.get('abilIncrease').get(var.get('z')).to_number())+Js(1))-Js(1))
                            var.put('bool', Js(True))
                            (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
                        (var.put('z',Js(var.get('z').to_number())+Js(1))-Js(1))
        var.get('console').callprop('log', (Js('half elf increases:  ')+var.get('abilIncrease')))
    #for JS loop
    var.put('x', Js(0.0))
    while (var.get('x')<Js(6.0)):
        try:
            var.get('mod').put(var.get('x'), var.get('modNum')(var.get('abil').get(var.get('x'))))
        finally:
                (var.put('x',Js(var.get('x').to_number())+Js(1))-Js(1))
    var.put('output', ((((((((Js('')+var.get('name'))+Js(' - Level '))+var.get('level'))+Js(' '))+var.get('racetxt'))+Js(' '))+var.get('classtxt'))+Js('==EOF==')), '+')
    var.put('hp', (var.get('hd')+var.get('mod').get('2')))
    var.get('console').callprop('log', (Js('1st level hp:  ')+var.get('hp')))
    if (var.get('level')>Js(1.0)):
        var.put('hpgain', Js(0.0))
        while 1:
            SWITCHED = False
            CONDITION = (var.get('hd'))
            if SWITCHED or PyJsStrictEq(CONDITION, Js(6.0)):
                SWITCHED = True
                var.put('hpgain', Js(4.0))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js(10.0)):
                SWITCHED = True
                var.put('hpgain', Js(6.0))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js(12.0)):
                SWITCHED = True
                var.put('hpgain', Js(7.0))
                break
            if True:
                SWITCHED = True
                var.put('hpgain', Js(5.0))
                break
            SWITCHED = True
            break
        var.put('hp', ((var.get('level')-Js(1.0))*var.get('hpgain')), '+')
        var.put('hp', ((var.get('level')-Js(1.0))*var.get('mod').get('2')), '+')
    var.get('console').callprop('log', (Js('levels & con bonus:  ')+var.get('hp')))
    if (var.get('racetxt').callprop('indexOf', Js('Hill Dwarf'))>(-Js(1.0))):
        var.put('hp', var.get('level'), '+')
    if ((var.get('cl')==Js(13.0)) and (var.get('soOrigin')==Js(0.0))):
        var.put('hp', var.get('level'), '+')
    var.get('console').callprop('log', (Js('grand total hp:  ')+var.get('hp')))
    var.put('x', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(10.0))))
    if (var.get('x')<Js(4.0)):
        var.put('bg', var.get('Math').callprop('floor', ((var.get('Math').callprop('random')*Js(13.0))+Js(1.0))))
    if (var.get('forceBg')>Js(0.0)):
        var.put('bg', var.get('forceBg'))
    var.put('personality', var.get('Math').callprop('floor', ((var.get('Math').callprop('random')*Js(8.0))+Js(1.0))))
    var.put('ideal', var.get('Math').callprop('floor', ((var.get('Math').callprop('random')*Js(6.0))+Js(1.0))))
    var.put('bond', var.get('Math').callprop('floor', ((var.get('Math').callprop('random')*Js(6.0))+Js(1.0))))
    var.put('flaw', var.get('Math').callprop('floor', ((var.get('Math').callprop('random')*Js(6.0))+Js(1.0))))
    var.put('bgText', Js(''))
    var.put('bgOutput', Js('<b>Background:</b> '), '+')
    while 1:
        SWITCHED = False
        CONDITION = (var.get('bg'))
        if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
            SWITCHED = True
            var.get('skLearn').put('6', Js(True))
            var.get('skLearn').put('14', Js(True))
            var.get('mySkills').callprop('push', Js(6.0))
            var.get('mySkills').callprop('push', Js(14.0))
            var.put('moreLang', Js(2.0), '+')
            var.put('bgOutput', Js('Acolyte'), '+')
            var.put('myLifestyle', Js(3.0))
            var.put('bgOutput', Js(''), '+')
            if (var.get('eqOutput').callprop('indexOf', Js('Holy symbol'))==(-Js(1.0))):
                var.put('eqOutput', Js(', Holy symbol'), '+')
            var.put('eqOutput', Js(', Prayer book, Common clothes'), '+')
            var.put('abOutput', Js(''), '+')
            var.put('gold', Js(15.0), '+')
            var.put('bgText', Js('==EOF==<b>Personality:</b> '), '+')
            var.put('i', Js(0.0))
            var.put('x', var.get('personality'))
            while (var.get('i')<Js(2.0)):
                if (var.get('personality')==Js(1.0)):
                    var.put('bgText', Js('I idolize a particular hero of my faith, and constantly refer to that person’s deeds and example. '), '+')
                if (var.get('personality')==Js(2.0)):
                    var.put('bgText', Js('I can find common ground between the fiercest enemies, empathizing with them and always working towards peace. '), '+')
                if (var.get('personality')==Js(3.0)):
                    var.put('bgText', Js('I see omens in every event and action. The gods try to speak to us, we just need to listen. '), '+')
                if (var.get('personality')==Js(4.0)):
                    var.put('bgText', Js('Nothing can shake my optimistic attitude. '), '+')
                if (var.get('personality')==Js(5.0)):
                    var.put('bgText', Js('I quote (or misquote) sacred texts and proverbs in almost every situation. '), '+')
                if (var.get('personality')==Js(6.0)):
                    var.put('bgText', Js('I am tolerant (or intolerant) of other faiths and respect (or condemn) the worship of other gods. '), '+')
                if (var.get('personality')==Js(7.0)):
                    var.put('bgText', Js("I've enjoyed fine food, drink, and high society among my temple’s elite. Rough living grates on me. "), '+')
                if (var.get('personality')==Js(8.0)):
                    var.put('bgText', Js('I’ve spent so long in the temple that I have little practical experience dealing with people in the outside world. '), '+')
                while (var.get('x')==var.get('personality')):
                    var.put('personality', var.get('Math').callprop('floor', ((var.get('Math').callprop('random')*Js(8.0))+Js(1.0))))
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                if (var.get('i')==Js(1.0)):
                    var.put('bgText', Js('==EOF=='), '+')
            var.put('bgText', Js('==EOF==<b>Ideal:</b> '), '+')
            if (var.get('ideal')==Js(1.0)):
                var.put('bgText', Js('Tradition. The ancient traditions of worship and sacrifice must be preserved and upheld. (Lawful)==EOF=='), '+')
            if (var.get('ideal')==Js(2.0)):
                var.put('bgText', Js('Charity. I always try to help those in need, no matter what the personal cost. (Good)==EOF=='), '+')
            if (var.get('ideal')==Js(3.0)):
                var.put('bgText', Js('Change. We must help bring about the changes the gods are constantly working in the world. (Chaotic)==EOF=='), '+')
            if (var.get('ideal')==Js(4.0)):
                var.put('bgText', Js('Power. I hope to one day rise to the top of my faith’s religious hierarchy. (Lawful)==EOF=='), '+')
            if (var.get('ideal')==Js(5.0)):
                var.put('bgText', Js('Faith. I trust that my deity will guide my actions, I have faith that if I work hard, things will go well. (Lawful)==EOF=='), '+')
            if (var.get('ideal')==Js(6.0)):
                var.put('bgText', Js('Aspiration. I seek to prove myself worthy of my god’s favor by matching my actions against his or her teachings. (Any)==EOF=='), '+')
            var.put('bgText', Js('<b>Bond:</b>  '), '+')
            if (var.get('bond')==Js(1.0)):
                var.put('bgText', Js('I would die to recover an ancient relic of my faith that was lost long ago.==EOF=='), '+')
            if (var.get('bond')==Js(2.0)):
                var.put('bgText', Js('I will someday get revenge on the corrupt temple hierarchy who branded me a heretic.==EOF=='), '+')
            if (var.get('bond')==Js(3.0)):
                var.put('bgText', Js('I owe my life to the priest who took me in when my parents died.==EOF=='), '+')
            if (var.get('bond')==Js(4.0)):
                var.put('bgText', Js('Everything I do is for the common people.==EOF=='), '+')
            if (var.get('bond')==Js(5.0)):
                var.put('bgText', Js('I will do anything to protect the temple where I served.==EOF=='), '+')
            if (var.get('bond')==Js(6.0)):
                var.put('bgText', Js('I seek to preserve a sacred text that my enemies consider heretical and seek to destroy.==EOF=='), '+')
            var.put('bgText', Js('<b>Flaw:</b>  '), '+')
            if (var.get('flaw')==Js(1.0)):
                var.put('bgText', Js('I judge others harshly, and myself even more severely.'), '+')
            if (var.get('flaw')==Js(2.0)):
                var.put('bgText', Js('I put too much trust in those who wield power within my temple’s hierarchy.'), '+')
            if (var.get('flaw')==Js(3.0)):
                var.put('bgText', Js('My piety sometimes leads me to blindly trust those that profess faith in my god.'), '+')
            if (var.get('flaw')==Js(4.0)):
                var.put('bgText', Js('I am inflexible in my thinking.'), '+')
            if (var.get('flaw')==Js(5.0)):
                var.put('bgText', Js('I am suspicious of strangers and expect the worst of them.'), '+')
            if (var.get('flaw')==Js(6.0)):
                var.put('bgText', Js('Once I pick a goal, I become obsessed with it to the detriment of everything else in my life.'), '+')
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
            SWITCHED = True
            var.get('skLearn').put('15', Js(True))
            var.get('skLearn').put('4', Js(True))
            var.get('mySkills').callprop('push', Js(15.0))
            var.get('mySkills').callprop('push', Js(4.0))
            var.put('myLifestyle', Js(4.0))
            var.put('bgOutput', Js('Charlatan '), '+')
            var.put('bgOutput', Js(''), '+')
            var.put('x', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(6.0))))
            if (var.get('x')==Js(0.0)):
                var.put('bgOutput', Js('(I cheat at games of chance.)'), '+')
            if (var.get('x')==Js(1.0)):
                var.put('bgOutput', Js('(I shave coins or forge documents.)'), '+')
            if (var.get('x')==Js(2.0)):
                var.put('bgOutput', Js('(I insinuate myself into people’s lives to prey on their weakness and secure their fortunes.)'), '+')
            if (var.get('x')==Js(3.0)):
                var.put('bgOutput', Js('(I put on new identities like clothes.)'), '+')
            if (var.get('x')==Js(4.0)):
                var.put('bgOutput', Js('(I run sleight-of-hand cons on street corners.)'), '+')
            if (var.get('x')==Js(5.0)):
                var.put('bgOutput', Js('(I convince people that worthless junk is worth their hard-earned money.)'), '+')
            var.put('eqOutput', Js(', Fine clothes, Disguise kit, Weighted dice'), '+')
            var.put('toOutput', Js(', Disguise kit, Forgery kit'), '+')
            var.put('gold', Js(15.0), '+')
            var.put('bgText', Js('==EOF==<b>Personality:</b> '), '+')
            var.put('i', Js(0.0))
            var.put('x', var.get('personality'))
            while (var.get('i')<Js(2.0)):
                if (var.get('personality')==Js(1.0)):
                    var.put('bgText', Js('I fall in and out of love easily, and am always pursuing someone. '), '+')
                if (var.get('personality')==Js(2.0)):
                    var.put('bgText', Js('I have a joke for every occasion, especially occasions where humor is inappropriate. '), '+')
                if (var.get('personality')==Js(3.0)):
                    var.put('bgText', Js('Flattery is my preferred trick for getting what I want. '), '+')
                if (var.get('personality')==Js(4.0)):
                    var.put('bgText', Js("I’m a born gambler who can't resist taking a risk for a potential payoff. "), '+')
                if (var.get('personality')==Js(5.0)):
                    var.put('bgText', Js('I lie about almost everything, even when there’s no good reason to. '), '+')
                if (var.get('personality')==Js(6.0)):
                    var.put('bgText', Js('Sarcasm and insults are my weapons of choice. '), '+')
                if (var.get('personality')==Js(7.0)):
                    var.put('bgText', Js('I keep multiple holy symbols on me and invoke whatever deity might come in useful at any given moment. '), '+')
                if (var.get('personality')==Js(8.0)):
                    var.put('bgText', Js('I pocket anything I see that might have some value. '), '+')
                while (var.get('x')==var.get('personality')):
                    var.put('personality', var.get('Math').callprop('floor', ((var.get('Math').callprop('random')*Js(8.0))+Js(1.0))))
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                if (var.get('i')==Js(1.0)):
                    var.put('bgText', Js('==EOF=='), '+')
            var.put('bgText', Js('==EOF==<b>Ideal:</b> '), '+')
            if (var.get('ideal')==Js(1.0)):
                var.put('bgText', Js('Independence. I am a free spirit— no one tells me what to do. (Chaotic)'), '+')
            if (var.get('ideal')==Js(2.0)):
                var.put('bgText', Js('Fairness. I never target people who can’t afford to lose a few coins. (Lawful)'), '+')
            if (var.get('ideal')==Js(3.0)):
                var.put('bgText', Js('Charity. I distribute the money I acquire to the people who really need it. (Good)'), '+')
            if (var.get('ideal')==Js(4.0)):
                var.put('bgText', Js('Creativity. I never run the same con twice. (Chaotic)'), '+')
            if (var.get('ideal')==Js(5.0)):
                var.put('bgText', Js('Friendship. Material goods come and go. Bonds of friendship last forever. (Good)'), '+')
            if (var.get('ideal')==Js(6.0)):
                var.put('bgText', Js('Aspiration. I’m determined to make something of myself. (Any)'), '+')
            var.put('bgText', Js('==EOF==<b>Bond:</b> '), '+')
            if (var.get('bond')==Js(1.0)):
                var.put('bgText', Js('I owe everything to my mentor—a horrible person who’s probably rotting in jail somewhere.'), '+')
            if (var.get('bond')==Js(2.0)):
                var.put('bgText', Js('Somewhere out there, I have a child who doesn’t know me. I’m making the world better for him or her.'), '+')
            if (var.get('bond')==Js(3.0)):
                var.put('bgText', Js('I come from a noble family, and one day I’ll reclaim my lands and title from those who stole them from me.'), '+')
            if (var.get('bond')==Js(4.0)):
                var.put('bgText', Js('A powerful person killed someone I love. Some day soon, I’ll have my revenge.'), '+')
            if (var.get('bond')==Js(5.0)):
                var.put('bgText', Js('I swindled and ruined a person who didn’t deserve it. I seek to atone for my misdeeds but might never be able to forgive myself.'), '+')
            if (var.get('bond')==Js(6.0)):
                var.put('bgText', Js('I fleeced the wrong person and must work to ensure that this individual never crosses paths with me or those I care about.'), '+')
            var.put('bgText', Js('==EOF==<b>Flaw:</b> '), '+')
            if (var.get('flaw')==Js(1.0)):
                var.put('bgText', Js('I can’t resist a pretty face.'), '+')
            if (var.get('flaw')==Js(2.0)):
                var.put('bgText', Js("I'm always in debt. I spend my ill-gotten gains on decadent luxuries faster than I bring them in.."), '+')
            if (var.get('flaw')==Js(3.0)):
                var.put('bgText', Js('I’m convinced that no one could ever fool me the way I fool others.'), '+')
            if (var.get('flaw')==Js(4.0)):
                var.put('bgText', Js('I’m too greedy for my own good. I can’t resist taking a risk if there’s money involved.'), '+')
            if (var.get('flaw')==Js(5.0)):
                var.put('bgText', Js('I can’t resist swindling people who are more powerful than me.'), '+')
            if (var.get('flaw')==Js(6.0)):
                var.put('bgText', Js("I hate to admit it and will hate myself for it, but I'll run and preserve my own hide if the going gets tough."), '+')
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(3.0)):
            SWITCHED = True
            var.get('skLearn').put('4', Js(True))
            var.get('skLearn').put('16', Js(True))
            var.get('mySkills').callprop('push', Js(4.0))
            var.get('mySkills').callprop('push', Js(16.0))
            var.put('myLifestyle', Js(2.0))
            var.put('eqOutput', Js(', Crowbar, Dark common clothes'), '+')
            var.put('tempTxt', var.get('gaming').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('gaming').get('length')))))
            var.put('toOutput', (Js(", Thieves' tools, ")+var.get('tempTxt')), '+')
            var.put('gold', Js(15.0), '+')
            var.put('bgOutput', Js('Criminal '), '+')
            var.put('bgOutput', Js(''), '+')
            var.put('x', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(8.0))))
            if (var.get('x')==Js(0.0)):
                var.put('bgOutput', Js('(Blackmailer)'), '+')
            if (var.get('x')==Js(1.0)):
                var.put('bgOutput', Js('(Burglar)'), '+')
            if (var.get('x')==Js(2.0)):
                var.put('bgOutput', Js('(Enforcer)'), '+')
            if (var.get('x')==Js(3.0)):
                var.put('bgOutput', Js('(Fence)'), '+')
            if (var.get('x')==Js(4.0)):
                var.put('bgOutput', Js('(Highway robber)'), '+')
            if (var.get('x')==Js(5.0)):
                var.put('bgOutput', Js('(Hired Killer)'), '+')
            if (var.get('x')==Js(6.0)):
                var.put('bgOutput', Js('(Pickpocket)'), '+')
            if (var.get('x')==Js(7.0)):
                var.put('bgOutput', Js('(Smuggler)'), '+')
            var.put('bgText', Js('==EOF==<b>Personality:</b> '), '+')
            var.put('i', Js(0.0))
            var.put('x', var.get('personality'))
            while (var.get('i')<Js(2.0)):
                if (var.get('personality')==Js(1.0)):
                    var.put('bgText', Js('I always have a plan for what to do when things go wrong. '), '+')
                if (var.get('personality')==Js(2.0)):
                    var.put('bgText', Js('I am always calm, no matter what the situation. I never raise my voice or let my emotions control me. '), '+')
                if (var.get('personality')==Js(3.0)):
                    var.put('bgText', Js('The first thing I do in a new place is note the locations of everything valuable - or where such things could be hidden '), '+')
                if (var.get('personality')==Js(4.0)):
                    var.put('bgText', Js('I would rather make a new friend than a new enemy. '), '+')
                if (var.get('personality')==Js(5.0)):
                    var.put('bgText', Js('I am incredibly slow to trust. Those who seem the fairest often have the most to hide. '), '+')
                if (var.get('personality')==Js(6.0)):
                    var.put('bgText', Js("I don't pay attention to the risks in a situation. Never tell me the odds. "), '+')
                if (var.get('personality')==Js(7.0)):
                    var.put('bgText', Js("The best way to get me to do something is to tell me I can't do it. "), '+')
                if (var.get('personality')==Js(8.0)):
                    var.put('bgText', Js('I blow up at the slightest insult. '), '+')
                while (var.get('x')==var.get('personality')):
                    var.put('personality', var.get('Math').callprop('floor', ((var.get('Math').callprop('random')*Js(8.0))+Js(1.0))))
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                if (var.get('i')==Js(1.0)):
                    var.put('bgText', Js('==EOF=='), '+')
            var.put('bgText', Js('==EOF==<b>Ideal:</b> '), '+')
            if (var.get('ideal')==Js(1.0)):
                var.put('bgText', Js('Honor. I don’t steal from others in the trade. (Lawful)'), '+')
            if (var.get('ideal')==Js(2.0)):
                var.put('bgText', Js('Freedom. Chains are meant to be broken, as are those who would forge them. (Chaotic)'), '+')
            if (var.get('ideal')==Js(3.0)):
                var.put('bgText', Js('Charity. I steal from the wealthy so that I can help people in need. (Good)'), '+')
            if (var.get('ideal')==Js(4.0)):
                var.put('bgText', Js('Greed.  I will do whatever it takes to become wealthy. (Evil)'), '+')
            if (var.get('ideal')==Js(5.0)):
                var.put('bgText', Js('People. I’m loyal to my friends, not to any ideals, and everyone else can take a trip down the Styx for all I care. (Neutral)'), '+')
            if (var.get('ideal')==Js(6.0)):
                var.put('bgText', Js('Redemption. There’s a spark of good in everyone. (Good)'), '+')
            var.put('bgText', Js('==EOF==<b>Bond:</b> '), '+')
            if (var.get('bond')==Js(1.0)):
                var.put('bgText', Js('I’m trying to pay off an old debt I owe to a generous benefactor.'), '+')
            if (var.get('bond')==Js(2.0)):
                var.put('bgText', Js('My ill-gotten gains go to support my family.'), '+')
            if (var.get('bond')==Js(3.0)):
                var.put('bgText', Js('Something important was taken from me, and I aim to steal it back.'), '+')
            if (var.get('bond')==Js(4.0)):
                var.put('bgText', Js('I will become the greatest thief that ever lived.'), '+')
            if (var.get('bond')==Js(5.0)):
                var.put('bgText', Js('I’m guilty of a terrible crime. I hope I can redeem myself for it.'), '+')
            if (var.get('bond')==Js(6.0)):
                var.put('bgText', Js('Someone I loved died because of a mistake I made. That will never happen again.'), '+')
            var.put('bgText', Js('==EOF==<b>Flaw:</b> '), '+')
            if (var.get('flaw')==Js(1.0)):
                var.put('bgText', Js('When I see something valuable, I can’t think about anything but how to steal it.'), '+')
            if (var.get('flaw')==Js(2.0)):
                var.put('bgText', Js('When faced with a choice between money and my friends, I usually choose the money.'), '+')
            if (var.get('flaw')==Js(3.0)):
                var.put('bgText', Js('If there’s a plan, I’ll forget it. If I don’t forget it, I’ll ignore it.'), '+')
            if (var.get('flaw')==Js(4.0)):
                var.put('bgText', Js("I have a “tell” that reveals when I'm lying."), '+')
            if (var.get('flaw')==Js(5.0)):
                var.put('bgText', Js('I turn tail and run when things look bad.'), '+')
            if (var.get('flaw')==Js(6.0)):
                var.put('bgText', Js('An innocent person is in prison for a crime that I committed. I’m okay with that.'), '+')
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(4.0)):
            SWITCHED = True
            var.get('skLearn').put('0', Js(True))
            var.get('skLearn').put('12', Js(True))
            var.get('mySkills').callprop('push', Js(0.0))
            var.get('mySkills').callprop('push', Js(12.0))
            var.put('myLifestyle', Js(3.0))
            var.put('temp', var.get('music').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('music').get('length')))))
            while (var.get('myMusic').callprop('indexOf', var.get('temp'))>(-Js(1.0))):
                var.put('temp', var.get('music').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('music').get('length')))))
            var.put('toOutput', ((Js(', ')+var.get('temp'))+Js(', Disguise kit')), '+')
            var.put('eqOutput', ((Js(', ')+var.get('temp'))+Js(', Costume')), '+')
            var.put('gold', Js(15.0), '+')
            var.put('bgOutput', Js('Entertainer'), '+')
            var.put('bgOutput', Js(''), '+')
            var.put('bgText', Js('==EOF==<b>Personality:</b> '), '+')
            var.put('i', Js(0.0))
            var.put('x', var.get('personality'))
            while (var.get('i')<Js(2.0)):
                if (var.get('personality')==Js(1.0)):
                    var.put('bgText', Js('I know a story relevant to almost every situation. '), '+')
                if (var.get('personality')==Js(2.0)):
                    var.put('bgText', Js('Whenever I come to a new place, I collect local rumors and spread gossip. '), '+')
                if (var.get('personality')==Js(3.0)):
                    var.put('bgText', Js('I’m a hopeless romantic, always searching for that “special someone.” '), '+')
                if (var.get('personality')==Js(4.0)):
                    var.put('bgText', Js('Nobody stays angry at me or around me for long, since I can defuse any amount of tension. '), '+')
                if (var.get('personality')==Js(5.0)):
                    var.put('bgText', Js('I love a good insult, even one directed at me. '), '+')
                if (var.get('personality')==Js(6.0)):
                    var.put('bgText', Js('I get bitter if I’m not the center of attention. '), '+')
                if (var.get('personality')==Js(7.0)):
                    var.put('bgText', Js('I’ll settle for nothing less than perfection. '), '+')
                if (var.get('personality')==Js(8.0)):
                    var.put('bgText', Js('I change my mood or my mind as quickly as I change key in a song. '), '+')
                while (var.get('x')==var.get('personality')):
                    var.put('personality', var.get('Math').callprop('floor', ((var.get('Math').callprop('random')*Js(8.0))+Js(1.0))))
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                if (var.get('i')==Js(1.0)):
                    var.put('bgText', Js('==EOF=='), '+')
            var.put('bgText', Js('==EOF==<b>Ideal:</b> '), '+')
            if (var.get('ideal')==Js(1.0)):
                var.put('bgText', Js('Beauty. When I perform, I make the world better than it was. (Good)'), '+')
            if (var.get('ideal')==Js(2.0)):
                var.put('bgText', Js('Tradition. The stories, legends, and songs of the past must never be forgotten, for they teach us who we are. (Lawful)'), '+')
            if (var.get('ideal')==Js(3.0)):
                var.put('bgText', Js('Creativity. The world is in need of new ideas and bold action. (Chaotic)'), '+')
            if (var.get('ideal')==Js(4.0)):
                var.put('bgText', Js('Greed. I’m only in it for the money and fame. (Evil)'), '+')
            if (var.get('ideal')==Js(5.0)):
                var.put('bgText', Js('People. I like seeing the smiles on people’s faces when I perform. That’s all that matters. (Neutral)'), '+')
            if (var.get('ideal')==Js(6.0)):
                var.put('bgText', Js('Honesty. Art should reflect the soul; it should come from within and reveal who we really are. (Any)'), '+')
            var.put('bgText', Js('==EOF==<b>Bond:</b> '), '+')
            if (var.get('bond')==Js(1.0)):
                var.put('bgText', Js('My instrument is my most treasured possession, and it reminds me of someone I love.'), '+')
            if (var.get('bond')==Js(2.0)):
                var.put('bgText', Js('Someone stole my precious instrument, and someday I’ll get it back.'), '+')
            if (var.get('bond')==Js(3.0)):
                var.put('bgText', Js('I want to be famous, whatever it takes.'), '+')
            if (var.get('bond')==Js(4.0)):
                var.put('bgText', Js('I idolize a hero of the old tales and measure my deeds against that person’s.'), '+')
            if (var.get('bond')==Js(5.0)):
                var.put('bgText', Js('I will do anything to prove myself superior to my hated rival.'), '+')
            if (var.get('bond')==Js(6.0)):
                var.put('bgText', Js('I would do anything for the other members of my old troupe.'), '+')
            var.put('bgText', Js('==EOF==<b>Flaw:</b> '), '+')
            if (var.get('flaw')==Js(1.0)):
                var.put('bgText', Js('I’ll do anything to win fame and renown.'), '+')
            if (var.get('flaw')==Js(2.0)):
                var.put('bgText', Js('I’m a sucker for a pretty face.'), '+')
            if (var.get('flaw')==Js(3.0)):
                var.put('bgText', Js('A scandal prevents me from ever going home again. That kind of trouble seems to follow me around.'), '+')
            if (var.get('flaw')==Js(4.0)):
                var.put('bgText', Js('I once satirized a noble who still wants my head. It was a mistake that I will likely repeat.'), '+')
            if (var.get('flaw')==Js(5.0)):
                var.put('bgText', Js('I have trouble keeping my true feelings hidden. My sharp tongue lands me in trouble.'), '+')
            if (var.get('flaw')==Js(6.0)):
                var.put('bgText', Js('Despite my best efforts, I am unreliable to my friends.'), '+')
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(5.0)):
            SWITCHED = True
            var.get('skLearn').put('6', Js(True))
            var.get('skLearn').put('13', Js(True))
            var.get('mySkills').callprop('push', Js(6.0))
            var.get('mySkills').callprop('push', Js(13.0))
            var.put('myLifestyle', Js(4.0))
            var.put('temp', var.get('artisans').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('artisans').get('length')))))
            if (var.get('toOutput').callprop('indexOf', var.get('temp'))>(-Js(1.0))):
                var.put('eqOutput', ((Js(', ')+var.get('temp'))+Js("'s tools, Guild letter, Traveler's clothes")), '+')
            else:
                var.put('eqOutput', ((Js(', ')+var.get('temp'))+Js("'s tools, Guild letter, Traveler's clothes")), '+')
                var.put('toOutput', ((Js(', ')+var.get('temp'))+Js("'s tools")), '+')
            var.put('moreLang', Js(1.0), '+')
            var.put('gold', Js(15.0), '+')
            var.put('bgOutput', ((Js('Guild Artisan (')+var.get('temp'))+Js(')')), '+')
            var.put('bgOutput', Js(''), '+')
            var.put('bgText', Js('==EOF==<b>Personality:</b> '), '+')
            var.put('i', Js(0.0))
            var.put('x', var.get('personality'))
            while (var.get('i')<Js(2.0)):
                if (var.get('personality')==Js(1.0)):
                    var.put('bgText', Js('I  believe that anything worth doing is worth doing right. I can’t help it— I’m a perfectionist. '), '+')
                if (var.get('personality')==Js(2.0)):
                    var.put('bgText', Js('I’m a snob who looks down on those who can’t appreciate fine art. '), '+')
                if (var.get('personality')==Js(3.0)):
                    var.put('bgText', Js('I always want to know how things work and what makes people tick. '), '+')
                if (var.get('personality')==Js(4.0)):
                    var.put('bgText', Js('I’m full of witty aphorisms and have a proverb for every occasion. '), '+')
                if (var.get('personality')==Js(5.0)):
                    var.put('bgText', Js('I’m rude to people who lack my commitment to hard work and fair play. '), '+')
                if (var.get('personality')==Js(6.0)):
                    var.put('bgText', Js(' I like to talk at length about my profession. '), '+')
                if (var.get('personality')==Js(7.0)):
                    var.put('bgText', Js(' I don’t part with my money easily and will haggle tirelessly to get the best deal possible. '), '+')
                if (var.get('personality')==Js(8.0)):
                    var.put('bgText', Js("I’m well known for my work, and I want to make sure everyone appreciates it. I'm always taken aback when people haven’t heard of me. "), '+')
                while (var.get('x')==var.get('personality')):
                    var.put('personality', var.get('Math').callprop('floor', ((var.get('Math').callprop('random')*Js(8.0))+Js(1.0))))
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                if (var.get('i')==Js(1.0)):
                    var.put('bgText', Js('==EOF=='), '+')
            var.put('bgText', Js('==EOF==<b>Ideal:</b> '), '+')
            if (var.get('ideal')==Js(1.0)):
                var.put('bgText', Js('Community. It is the duty of all civilized people to strengthen the bonds of community and the security of civilization. (Lawful)'), '+')
            if (var.get('ideal')==Js(2.0)):
                var.put('bgText', Js('Generosity. My talents were given to me so that I could use them to benefit the world. (Good)'), '+')
            if (var.get('ideal')==Js(3.0)):
                var.put('bgText', Js('Freedom. Everyone should be free to pursue his or her own livelihood. (Chaotic)'), '+')
            if (var.get('ideal')==Js(4.0)):
                var.put('bgText', Js('Greed. I’m only in it for the money. (Evil)'), '+')
            if (var.get('ideal')==Js(5.0)):
                var.put('bgText', Js('People. I’m committed to the people I care about, not to ideals. (Neutral)'), '+')
            if (var.get('ideal')==Js(6.0)):
                var.put('bgText', Js('Aspiration. I work hard to be the best there is at my craft.'), '+')
            var.put('bgText', Js('==EOF==<b>Bond:</b> '), '+')
            if (var.get('bond')==Js(1.0)):
                var.put('bgText', Js('The workshop where I learned my trade is the most important place in the world to me.'), '+')
            if (var.get('bond')==Js(2.0)):
                var.put('bgText', Js('I created a great work for someone, and then found them unworthy to receive it. I’m still looking for someone worthy.'), '+')
            if (var.get('bond')==Js(3.0)):
                var.put('bgText', Js('I owe my guild a great debt for forging me into the person I am today.'), '+')
            if (var.get('bond')==Js(4.0)):
                var.put('bgText', Js('I pursue wealth to secure someone’s love.'), '+')
            if (var.get('bond')==Js(5.0)):
                var.put('bgText', Js('One day I will return to my guild and prove that I am the greatest artisan of them all.'), '+')
            if (var.get('bond')==Js(6.0)):
                var.put('bgText', Js('I will get revenge on the evil forces that destroyed my place of business and ruined my livelihood.'), '+')
            var.put('bgText', Js('==EOF==<b>Flaw:</b> '), '+')
            if (var.get('flaw')==Js(1.0)):
                var.put('bgText', Js('I’ll do anything to get my hands on something rare or priceless.'), '+')
            if (var.get('flaw')==Js(2.0)):
                var.put('bgText', Js('I’m quick to assume that someone is trying to cheat me.'), '+')
            if (var.get('flaw')==Js(3.0)):
                var.put('bgText', Js('No one must ever learn that I once stole money from guild coffers.'), '+')
            if (var.get('flaw')==Js(4.0)):
                var.put('bgText', Js('I’m never satisfied with what I have— I always want more.'), '+')
            if (var.get('flaw')==Js(5.0)):
                var.put('bgText', Js('I would kill to acquire a noble title.'), '+')
            if (var.get('flaw')==Js(6.0)):
                var.put('bgText', Js('I’m horribly jealous of anyone who can outshine my handiwork. Everywhere I go, I’m surrounded by rivals.'), '+')
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(6.0)):
            SWITCHED = True
            var.get('skLearn').put('9', Js(True))
            var.get('skLearn').put('14', Js(True))
            var.get('mySkills').callprop('push', Js(9.0))
            var.get('mySkills').callprop('push', Js(14.0))
            var.put('myLifestyle', Js(2.0))
            if (var.get('toOutput').callprop('indexOf', Js('Herbalism kit'))==(-Js(1.0))):
                var.put('toOutput', Js(', Herbalism kit'), '+')
            var.put('eqOutput', Js(', Record of Hermit studies, Common clothes, Herbalism kit'), '+')
            var.put('gold', Js(5.0), '+')
            var.put('moreLang', Js(1.0), '+')
            var.put('bgOutput', Js('Hermit '), '+')
            var.put('bgOutput', Js(''), '+')
            var.put('x', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(8.0))))
            if (var.get('x')==Js(0.0)):
                var.put('bgOutput', Js('(I was searching for spiritual enlightenment.)'), '+')
            if (var.get('x')==Js(1.0)):
                var.put('bgOutput', Js('(I was partaking of communal living in accordance with the dictates of a religious order.)'), '+')
            if (var.get('x')==Js(2.0)):
                var.put('bgOutput', Js('(I was exiled for a crime I didn’t commit.)'), '+')
            if (var.get('x')==Js(3.0)):
                var.put('bgOutput', Js('(I retreated from society after a life-altering event.)'), '+')
            if (var.get('x')==Js(4.0)):
                var.put('bgOutput', Js('(I needed a quiet place to work on my art, literature, music, or manifesto.)'), '+')
            if (var.get('x')==Js(5.0)):
                var.put('bgOutput', Js('(I needed to commune with nature, far from civilization.)'), '+')
            if (var.get('x')==Js(6.0)):
                var.put('bgOutput', Js('(I was the caretaker of an ancient ruin or relic.)'), '+')
            if (var.get('x')==Js(7.0)):
                var.put('bgOutput', Js('(I was a pilgrim in search of a person, place, or relic of spiritual significance.)'), '+')
            var.put('bgText', Js('==EOF==<b>Personality:</b> '), '+')
            var.put('i', Js(0.0))
            var.put('x', var.get('personality'))
            while (var.get('i')<Js(2.0)):
                if (var.get('personality')==Js(1.0)):
                    var.put('bgText', Js('I’ve been isolated for so long that I rarely speak, preferring gestures and the occasional grunt. '), '+')
                if (var.get('personality')==Js(2.0)):
                    var.put('bgText', Js('I am utterly serene, even in the face of disaster. '), '+')
                if (var.get('personality')==Js(3.0)):
                    var.put('bgText', Js('The leader of my community had something wise to say on every topic, and I am eager to share that wisdom. '), '+')
                if (var.get('personality')==Js(4.0)):
                    var.put('bgText', Js('I feel tremendous empathy for all who suffer. '), '+')
                if (var.get('personality')==Js(5.0)):
                    var.put('bgText', Js('I’m oblivious to etiquette and social expectations. '), '+')
                if (var.get('personality')==Js(6.0)):
                    var.put('bgText', Js('I connect everything that happens to me to a grand, cosmic plan. '), '+')
                if (var.get('personality')==Js(7.0)):
                    var.put('bgText', Js('I often get lost in my own thoughts and contemplation, becoming oblivious to my surroundings. '), '+')
                if (var.get('personality')==Js(8.0)):
                    var.put('bgText', Js('I am working on a grand philosophical theory and love sharing my ideas. '), '+')
                while (var.get('x')==var.get('personality')):
                    var.put('personality', var.get('Math').callprop('floor', ((var.get('Math').callprop('random')*Js(8.0))+Js(1.0))))
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                if (var.get('i')==Js(1.0)):
                    var.put('bgText', Js('==EOF=='), '+')
            var.put('bgText', Js('==EOF==<b>Ideal:</b> '), '+')
            if (var.get('ideal')==Js(1.0)):
                var.put('bgText', Js('Greater Good. My gifts are meant to be shared with all, not used for my own benefit. (Good)'), '+')
            if (var.get('ideal')==Js(2.0)):
                var.put('bgText', Js('Logic. Emotions must not cloud our sense of what is right and true, or our logical thinking. (Lawful)'), '+')
            if (var.get('ideal')==Js(3.0)):
                var.put('bgText', Js('Free Thinking. Inquiry and curiosity are the pillars of progress. (Chaotic)'), '+')
            if (var.get('ideal')==Js(4.0)):
                var.put('bgText', Js('Power. Solitude and contemplation are paths toward mystical or magical power. (Evil)'), '+')
            if (var.get('ideal')==Js(5.0)):
                var.put('bgText', Js('Live and Let Live. Meddling in the affairs of others only causes trouble. (Neutral)'), '+')
            if (var.get('ideal')==Js(6.0)):
                var.put('bgText', Js('Self-Knowledge. If you know yourself, there’s nothing left to know. (Any)'), '+')
            var.put('bgText', Js('==EOF==<b>Bond:</b> '), '+')
            if (var.get('bond')==Js(1.0)):
                var.put('bgText', Js('Nothing is more important than the other members of my hermitage, order, or association.'), '+')
            if (var.get('bond')==Js(2.0)):
                var.put('bgText', Js('I entered seclusion to hide from the ones who might still be hunting me. I must someday confront them.'), '+')
            if (var.get('bond')==Js(3.0)):
                var.put('bgText', Js('I’m still seeking the enlightenment I pursued in my seclusion, and it still eludes me.'), '+')
            if (var.get('bond')==Js(4.0)):
                var.put('bgText', Js('I entered seclusion because I loved someone I could not have.'), '+')
            if (var.get('bond')==Js(5.0)):
                var.put('bgText', Js('Should my discovery come to light, it could bring ruin to the world.'), '+')
            if (var.get('bond')==Js(6.0)):
                var.put('bgText', Js('My isolation gave me great insight into a great evil that only I can destroy.'), '+')
            var.put('bgText', Js('==EOF==<b>Flaw:</b> '), '+')
            if (var.get('flaw')==Js(1.0)):
                var.put('bgText', Js("Now that I've returned to the world, I enjoy its delights a little too much."), '+')
            if (var.get('flaw')==Js(2.0)):
                var.put('bgText', Js('I harbor dark, bloodthirsty thoughts that my isolation and meditation failed to quell.'), '+')
            if (var.get('flaw')==Js(3.0)):
                var.put('bgText', Js('I am dogmatic in my thoughts and philosophy.'), '+')
            if (var.get('flaw')==Js(4.0)):
                var.put('bgText', Js('I let my need to win arguments overshadow friendships and harmony.'), '+')
            if (var.get('flaw')==Js(5.0)):
                var.put('bgText', Js('I’d risk too much to uncover a lost bit of knowledge.'), '+')
            if (var.get('flaw')==Js(6.0)):
                var.put('bgText', Js('I like keeping secrets and won’t share them with anyone.'), '+')
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(7.0)):
            SWITCHED = True
            var.get('skLearn').put('1', Js(True))
            var.get('skLearn').put('17', Js(True))
            var.get('mySkills').callprop('push', Js(1.0))
            var.get('mySkills').callprop('push', Js(17.0))
            var.put('myLifestyle', Js(3.0))
            var.put('temp', var.get('artisans').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('artisans').get('length')))))
            var.put('toOutput', ((Js(', ')+var.get('temp'))+Js("'s tools, Land vehicles")), '+')
            var.put('eqOutput', ((Js(', ')+var.get('temp'))+Js("'s tools, Common clothes")), '+')
            var.put('gold', Js(10.0), '+')
            var.put('bgOutput', Js('Folk Hero '), '+')
            var.put('bgOutput', Js(''), '+')
            var.put('x', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(10.0))))
            if (var.get('x')==Js(0.0)):
                var.put('bgOutput', Js('(I stood up to a tyrant’s agents.)'), '+')
            if (var.get('x')==Js(1.0)):
                var.put('bgOutput', Js('(I saved people during a natural disaster.)'), '+')
            if (var.get('x')==Js(2.0)):
                var.put('bgOutput', Js('(I stood alone against a terrible monster.)'), '+')
            if (var.get('x')==Js(3.0)):
                var.put('bgOutput', Js('(I stole from a corrupt merchant to help the poor.)'), '+')
            if (var.get('x')==Js(4.0)):
                var.put('bgOutput', Js('(I led a militia to fight off an invading army.)'), '+')
            if (var.get('x')==Js(5.0)):
                var.put('bgOutput', Js('(I broke into a tyrant’s castle and stole weapons to arm the people.)'), '+')
            if (var.get('x')==Js(6.0)):
                var.put('bgOutput', Js('(I trained the peasantry to use farm implements as weapons against a tyrant’s soldiers.)'), '+')
            if (var.get('x')==Js(7.0)):
                var.put('bgOutput', Js('(A lord rescinded an unpopular decree after I led a symbolic act of protest against it.)'), '+')
            if (var.get('x')==Js(8.0)):
                var.put('bgOutput', Js('(A celestial, fey, or similar creature gave me a blessing or revealed my secret origin.)'), '+')
            if (var.get('x')==Js(9.0)):
                var.put('bgOutput', Js('(Recruited into a lord’s army, I rose to leadership and was commended for my heroism.)'), '+')
            var.put('bgText', Js('==EOF==<b>Personality:</b> '), '+')
            var.put('i', Js(0.0))
            var.put('x', var.get('personality'))
            while (var.get('i')<Js(2.0)):
                if (var.get('personality')==Js(1.0)):
                    var.put('bgText', Js('I judge people by their actions, not their words. '), '+')
                if (var.get('personality')==Js(2.0)):
                    var.put('bgText', Js('If someone is in trouble, I’m always ready to lend help. '), '+')
                if (var.get('personality')==Js(3.0)):
                    var.put('bgText', Js('When I set my mind to something, I follow through no matter what gets in my way. '), '+')
                if (var.get('personality')==Js(4.0)):
                    var.put('bgText', Js('I have a strong sense of fair play and always try to find the most equitable solution to arguments. '), '+')
                if (var.get('personality')==Js(5.0)):
                    var.put('bgText', Js('I’m confident in my own abilities and do what I can to instill confidence in others. '), '+')
                if (var.get('personality')==Js(6.0)):
                    var.put('bgText', Js('Thinking is for other people. I prefer action. '), '+')
                if (var.get('personality')==Js(7.0)):
                    var.put('bgText', Js('I misuse long words in an attempt to sound smarter. '), '+')
                if (var.get('personality')==Js(8.0)):
                    var.put('bgText', Js('I get bored easily. When am I going to get on with my destiny? '), '+')
                while (var.get('x')==var.get('personality')):
                    var.put('personality', var.get('Math').callprop('floor', ((var.get('Math').callprop('random')*Js(8.0))+Js(1.0))))
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                if (var.get('i')==Js(1.0)):
                    var.put('bgText', Js('==EOF=='), '+')
            var.put('bgText', Js('==EOF==<b>Ideal:</b> '), '+')
            if (var.get('ideal')==Js(1.0)):
                var.put('bgText', Js('Respect. People deserve to be treated with dignity and respect. (Good)'), '+')
            if (var.get('ideal')==Js(2.0)):
                var.put('bgText', Js('Fairness. No one should get preferential treatment before the law, and no one is above the law. (Lawful)'), '+')
            if (var.get('ideal')==Js(3.0)):
                var.put('bgText', Js('Freedom. Tyrants must not be allowed to oppress the people. (Chaotic)'), '+')
            if (var.get('ideal')==Js(4.0)):
                var.put('bgText', Js('Might. If I become strong, I can take what I want— what I deserve. (Evil)'), '+')
            if (var.get('ideal')==Js(5.0)):
                var.put('bgText', Js('Sincerity. There’s no good in pretending to be something I’m not. (Neutral)'), '+')
            if (var.get('ideal')==Js(6.0)):
                var.put('bgText', Js('Destiny. Nothing and no one can steer me away from my higher calling. (Any)'), '+')
            var.put('bgText', Js('==EOF==<b>Bond:</b> '), '+')
            if (var.get('bond')==Js(1.0)):
                var.put('bgText', Js('I have a family, but I have no idea where they are. One day, I hope to see them again.'), '+')
            if (var.get('bond')==Js(2.0)):
                var.put('bgText', Js('I worked the land, I love the land, and I will protect the land.'), '+')
            if (var.get('bond')==Js(3.0)):
                var.put('bgText', Js('A proud noble once gave me a horrible beating, and I will take my revenge on any bully I encounter.'), '+')
            if (var.get('bond')==Js(4.0)):
                var.put('bgText', Js('My tools are symbols of my past life, and I carry them so that I will never forget my roots.'), '+')
            if (var.get('bond')==Js(5.0)):
                var.put('bgText', Js('I protect those who cannot protect themselves.'), '+')
            if (var.get('bond')==Js(6.0)):
                var.put('bgText', Js('I wish my childhood sweetheart had come with me to pursue my destiny.'), '+')
            var.put('bgText', Js('==EOF==<b>Flaw:</b> '), '+')
            if (var.get('flaw')==Js(1.0)):
                var.put('bgText', Js('The tyrant who rules my land will stop at nothing to see me killed.'), '+')
            if (var.get('flaw')==Js(2.0)):
                var.put('bgText', Js('I’m convinced of the significance of my destiny, and blind to my shortcomings and the risk of failure.'), '+')
            if (var.get('flaw')==Js(3.0)):
                var.put('bgText', Js('The people who knew me when I was young know my shameful secret, so I can never go home again.'), '+')
            if (var.get('flaw')==Js(4.0)):
                var.put('bgText', Js('I have a weakness for the vices of the city, especially hard drink.'), '+')
            if (var.get('flaw')==Js(5.0)):
                var.put('bgText', Js('Secretly, I believe that things would be better if I were a tyrant lording over the land.'), '+')
            if (var.get('flaw')==Js(6.0)):
                var.put('bgText', Js('I have trouble trusting in my allies.'), '+')
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(8.0)):
            SWITCHED = True
            var.get('skLearn').put('5', Js(True))
            var.get('skLearn').put('13', Js(True))
            var.get('mySkills').callprop('push', Js(5.0))
            var.get('mySkills').callprop('push', Js(13.0))
            var.put('myLifestyle', Js(5.0))
            var.put('tempTxt', var.get('gaming').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('gaming').get('length')))))
            var.put('toOutput', (Js(', ')+var.get('tempTxt')), '+')
            var.put('eqOutput', Js(', Fine clothes, Signet ring, Scroll of pedigree'), '+')
            var.put('gold', Js(25.0), '+')
            var.put('moreLang', Js(1.0), '+')
            var.put('bgOutput', Js('Noble'), '+')
            var.put('bgOutput', Js(''), '+')
            var.put('bgText', Js('==EOF==<b>Personality:</b> '), '+')
            var.put('i', Js(0.0))
            var.put('x', var.get('personality'))
            while (var.get('i')<Js(2.0)):
                if (var.get('personality')==Js(1.0)):
                    var.put('bgText', Js('My eloquent flattery makes everyone I talk to feel like the most wonderful and important person in the world. '), '+')
                if (var.get('personality')==Js(2.0)):
                    var.put('bgText', Js('The common folk love me for my kindness and generosity. '), '+')
                if (var.get('personality')==Js(3.0)):
                    var.put('bgText', Js('No one could doubt by looking at my regal bearing that I am a cut above the unwashed masses. '), '+')
                if (var.get('personality')==Js(4.0)):
                    var.put('bgText', Js('I take great pains to always look my best and follow the latest fashions. '), '+')
                if (var.get('personality')==Js(5.0)):
                    var.put('bgText', Js('I don’t like to get my hands dirty, and I won’t be caught dead in unsuitable accommodations. '), '+')
                if (var.get('personality')==Js(6.0)):
                    var.put('bgText', Js('Despite my noble birth, I do not place myself above other folk. We all have the same blood. '), '+')
                if (var.get('personality')==Js(7.0)):
                    var.put('bgText', Js('My favor, once lost, is lost forever. '), '+')
                if (var.get('personality')==Js(8.0)):
                    var.put('bgText', Js('If you do me an injury, I will crush you, ruin your name, and salt your fields. '), '+')
                while (var.get('x')==var.get('personality')):
                    var.put('personality', var.get('Math').callprop('floor', ((var.get('Math').callprop('random')*Js(8.0))+Js(1.0))))
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                if (var.get('i')==Js(1.0)):
                    var.put('bgText', Js('==EOF=='), '+')
            var.put('bgText', Js('==EOF==<b>Ideal:</b> '), '+')
            if (var.get('ideal')==Js(1.0)):
                var.put('bgText', Js('Respect. Respect is due to me because of my position, but all people regardless of station deserve to be treated with dignity.  (Good)'), '+')
            if (var.get('ideal')==Js(2.0)):
                var.put('bgText', Js('Responsibility. It is my duty to respect the authority of those above me, just as those below me must respect mine.  (Lawful)'), '+')
            if (var.get('ideal')==Js(3.0)):
                var.put('bgText', Js('Independence. I must prove that I can handle myself without the coddling of my family.  (Chaotic)'), '+')
            if (var.get('ideal')==Js(4.0)):
                var.put('bgText', Js('Power. If I  can attain more power, no one will tell me what to do.  (Evil)'), '+')
            if (var.get('ideal')==Js(5.0)):
                var.put('bgText', Js('Family. Blood runs thicker than water.  (Any)'), '+')
            if (var.get('ideal')==Js(6.0)):
                var.put('bgText', Js('Noble Obligation. It is my duty to protect and care for the people beneath me.  (Good)'), '+')
            var.put('bgText', Js('==EOF==<b>Bond:</b> '), '+')
            if (var.get('bond')==Js(1.0)):
                var.put('bgText', Js('I will face any challenge to win the approval of my family.'), '+')
            if (var.get('bond')==Js(2.0)):
                var.put('bgText', Js('My house’s alliance with another noble family must be sustained at all costs.'), '+')
            if (var.get('bond')==Js(3.0)):
                var.put('bgText', Js('Nothing is more important than the other members of my family.'), '+')
            if (var.get('bond')==Js(4.0)):
                var.put('bgText', Js('I am in love with the heir of a family that my family despises.'), '+')
            if (var.get('bond')==Js(5.0)):
                var.put('bgText', Js('My loyalty to my sovereign is unwavering.'), '+')
            if (var.get('bond')==Js(6.0)):
                var.put('bgText', Js('The common folk must see me as a hero of the people.'), '+')
            var.put('bgText', Js('==EOF==<b>Flaw:</b> '), '+')
            if (var.get('flaw')==Js(1.0)):
                var.put('bgText', Js('I secretly believe that everyone is beneath me.'), '+')
            if (var.get('flaw')==Js(2.0)):
                var.put('bgText', Js('I hide a truly scandalous secret that could ruin my family forever.'), '+')
            if (var.get('flaw')==Js(3.0)):
                var.put('bgText', Js('I too often hear veiled insults and threats in every word addressed to me, and I’m quick to anger.'), '+')
            if (var.get('flaw')==Js(4.0)):
                var.put('bgText', Js('I  have an insatiable desire for carnal pleasures.'), '+')
            if (var.get('flaw')==Js(5.0)):
                var.put('bgText', Js('In fact, the world does revolve around me.'), '+')
            if (var.get('flaw')==Js(6.0)):
                var.put('bgText', Js('By my words and actions,  I often bring shame to my family.'), '+')
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(9.0)):
            SWITCHED = True
            var.get('skLearn').put('3', Js(True))
            var.get('skLearn').put('17', Js(True))
            var.get('mySkills').callprop('push', Js(3.0))
            var.get('mySkills').callprop('push', Js(17.0))
            var.put('myLifestyle', Js(2.0))
            var.put('temp', var.get('music').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('music').get('length')))))
            while (var.get('myMusic').callprop('indexOf', var.get('temp'))>(-Js(1.0))):
                var.put('temp', var.get('music').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('music').get('length')))))
            var.put('toOutput', (Js(', ')+var.get('temp')), '+')
            var.put('eqOutput', Js(", Hunting trap, Animal trophy, Traveler's clothes"), '+')
            var.put('gold', Js(10.0), '+')
            var.put('moreLang', Js(1.0), '+')
            var.put('bgOutput', Js('Outlander '), '+')
            var.put('bgOutput', Js(''), '+')
            var.put('x', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(10.0))))
            if (var.get('x')==Js(0.0)):
                var.put('bgOutput', Js('(Forester)'), '+')
            if (var.get('x')==Js(1.0)):
                var.put('bgOutput', Js('(Trapper)'), '+')
            if (var.get('x')==Js(2.0)):
                var.put('bgOutput', Js('(Homesteader)'), '+')
            if (var.get('x')==Js(3.0)):
                var.put('bgOutput', Js('(Guide)'), '+')
            if (var.get('x')==Js(4.0)):
                var.put('bgOutput', Js('(Exile or outcast)'), '+')
            if (var.get('x')==Js(5.0)):
                var.put('bgOutput', Js('(Bounty hunter)'), '+')
            if (var.get('x')==Js(6.0)):
                var.put('bgOutput', Js('(Pilgrim)'), '+')
            if (var.get('x')==Js(7.0)):
                var.put('bgOutput', Js('(Tribal nomad)'), '+')
            if (var.get('x')==Js(8.0)):
                var.put('bgOutput', Js('(Hunter-gatherer)'), '+')
            if (var.get('x')==Js(9.0)):
                var.put('bgOutput', Js('(Tribal marauder)'), '+')
            var.put('bgText', Js('==EOF==<b>Personality:</b> '), '+')
            var.put('i', Js(0.0))
            var.put('x', var.get('personality'))
            while (var.get('i')<Js(2.0)):
                if (var.get('personality')==Js(1.0)):
                    var.put('bgText', Js('I’m driven by a wanderlust that led me away from home. '), '+')
                if (var.get('personality')==Js(2.0)):
                    var.put('bgText', Js('I watch over my friends as if they were a litter of newborn pups. '), '+')
                if (var.get('personality')==Js(3.0)):
                    var.put('bgText', Js('I once ran twenty-five miles without stopping to warn to my clan of an approaching orc horde. I’d do it again if I had to. '), '+')
                if (var.get('personality')==Js(4.0)):
                    var.put('bgText', Js('I place no stock in wealthy or well-mannered folk. Money and manners won’t save you from a hungry owlbear. '), '+')
                if (var.get('personality')==Js(5.0)):
                    var.put('bgText', Js('I have a lesson for every situation, drawn from observing nature. '), '+')
                if (var.get('personality')==Js(6.0)):
                    var.put('bgText', Js('I’m always picking things up, absently fiddling with them, and sometimes accidentally breaking them. '), '+')
                if (var.get('personality')==Js(7.0)):
                    var.put('bgText', Js('I feel far more comfortable around animals than people. '), '+')
                if (var.get('personality')==Js(8.0)):
                    var.put('bgText', Js('I was, in fact, raised by wolves. '), '+')
                while (var.get('x')==var.get('personality')):
                    var.put('personality', var.get('Math').callprop('floor', ((var.get('Math').callprop('random')*Js(8.0))+Js(1.0))))
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                if (var.get('i')==Js(1.0)):
                    var.put('bgText', Js('==EOF=='), '+')
            var.put('bgText', Js('==EOF==<b>Ideal:</b> '), '+')
            if (var.get('ideal')==Js(1.0)):
                var.put('bgText', Js('Change. Life is like the seasons, in constant change, and we must change with it. (Chaotic)'), '+')
            if (var.get('ideal')==Js(2.0)):
                var.put('bgText', Js('Greater Good. It is each person’s responsibility to make the most happiness for the whole tribe. (Good)'), '+')
            if (var.get('ideal')==Js(3.0)):
                var.put('bgText', Js('Honor. If I dishonor myself, I dishonor my whole clan. (Lawful)'), '+')
            if (var.get('ideal')==Js(4.0)):
                var.put('bgText', Js('Might. The strongest are meant to rule. (Evil)'), '+')
            if (var.get('ideal')==Js(5.0)):
                var.put('bgText', Js('Nature. The natural world is more important than all the constructs of civilization. (Neutral)'), '+')
            if (var.get('ideal')==Js(6.0)):
                var.put('bgText', Js('Glory. I must earn glory in battle, for myself and my clan. (Any)'), '+')
            var.put('bgText', Js('==EOF==<b>Bond:</b> '), '+')
            if (var.get('bond')==Js(1.0)):
                var.put('bgText', Js('My family, clan, or tribe is the most important thing in my life, even when they are far from me.'), '+')
            if (var.get('bond')==Js(2.0)):
                var.put('bgText', Js('An injury to the unspoiled wilderness of my home is an injury to me.'), '+')
            if (var.get('bond')==Js(3.0)):
                var.put('bgText', Js('I will bring terrible wrath down on the evildoers who destroyed my homeland.'), '+')
            if (var.get('bond')==Js(4.0)):
                var.put('bgText', Js('I am the last of my tribe, and it is up to me to ensure their names enter legend.'), '+')
            if (var.get('bond')==Js(5.0)):
                var.put('bgText', Js('I suffer awful visions of a coming disaster and will do anything to prevent it.'), '+')
            if (var.get('bond')==Js(6.0)):
                var.put('bgText', Js('It is my duty to provide children to sustain my tribe.'), '+')
            var.put('bgText', Js('==EOF==<b>Flaw:</b> '), '+')
            if (var.get('flaw')==Js(1.0)):
                var.put('bgText', Js('I am too enamored of ale, wine, and other intoxicants.'), '+')
            if (var.get('flaw')==Js(2.0)):
                var.put('bgText', Js('There’s no room for caution in a life lived to the fullest.'), '+')
            if (var.get('flaw')==Js(3.0)):
                var.put('bgText', Js('I remember every insult I’ve received and nurse a silent resentment toward anyone who’s ever wronged me.'), '+')
            if (var.get('flaw')==Js(4.0)):
                var.put('bgText', Js('I am slow to trust members of other races, tribes, and societies.'), '+')
            if (var.get('flaw')==Js(5.0)):
                var.put('bgText', Js('Violence is my answer to almost any challenge.'), '+')
            if (var.get('flaw')==Js(6.0)):
                var.put('bgText', Js('Don’t expect me to save those who can’t save themselves. It is nature’s way that the strong thrive and the weak perish.'), '+')
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(10.0)):
            SWITCHED = True
            var.get('skLearn').put('2', Js(True))
            var.get('skLearn').put('5', Js(True))
            var.get('mySkills').callprop('push', Js(2.0))
            var.get('mySkills').callprop('push', Js(5.0))
            var.put('myLifestyle', Js(3.0))
            var.put('eqOutput', Js(", Black ink, Quill, Colleague's letter, Common clothes"), '+')
            var.put('moreLang', Js(2.0), '+')
            var.put('gold', Js(10.0), '+')
            var.put('bgOutput', Js('Sage '), '+')
            var.put('bgOutput', Js(''), '+')
            var.put('x', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(8.0))))
            if (var.get('x')==Js(0.0)):
                var.put('bgOutput', Js('(Alchemist)'), '+')
            if (var.get('x')==Js(1.0)):
                var.put('bgOutput', Js('(Astronomer)'), '+')
            if (var.get('x')==Js(2.0)):
                var.put('bgOutput', Js('(Discredited academic)'), '+')
            if (var.get('x')==Js(3.0)):
                var.put('bgOutput', Js('(Librarian)'), '+')
            if (var.get('x')==Js(4.0)):
                var.put('bgOutput', Js('(Professor)'), '+')
            if (var.get('x')==Js(5.0)):
                var.put('bgOutput', Js('(Researcher)'), '+')
            if (var.get('x')==Js(6.0)):
                var.put('bgOutput', Js("(Wizard's apprentice)"), '+')
            if (var.get('x')==Js(7.0)):
                var.put('bgOutput', Js('(Scribe)'), '+')
            var.put('bgText', Js('==EOF==<b>Personality:</b> '), '+')
            var.put('i', Js(0.0))
            var.put('x', var.get('personality'))
            while (var.get('i')<Js(2.0)):
                if (var.get('personality')==Js(1.0)):
                    var.put('bgText', Js('I use polysyllabic words that convey the impression of great erudition. '), '+')
                if (var.get('personality')==Js(2.0)):
                    var.put('bgText', Js("I've read every book in the world’s greatest libraries—or I like to boast that I have. "), '+')
                if (var.get('personality')==Js(3.0)):
                    var.put('bgText', Js("I'm used to helping out those who aren’t as smart as I am, and I patiently explain anything and everything to others. "), '+')
                if (var.get('personality')==Js(4.0)):
                    var.put('bgText', Js('There’s nothing I like more than a good mystery. '), '+')
                if (var.get('personality')==Js(5.0)):
                    var.put('bgText', Js('I’m willing to listen to every side of an argument before I make my own judgment. '), '+')
                if (var.get('personality')==Js(6.0)):
                    var.put('bgText', Js('I . . . speak . . . slowly .  . . when talking .  .  . to idiots, . . . which . . . almost . . . everyone . .  . is . . . compared . . . to me. '), '+')
                if (var.get('personality')==Js(7.0)):
                    var.put('bgText', Js('I am horribly, horribly awkward in social situations. '), '+')
                if (var.get('personality')==Js(8.0)):
                    var.put('bgText', Js('I’m convinced that people are always trying to steal my secrets. '), '+')
                while (var.get('x')==var.get('personality')):
                    var.put('personality', var.get('Math').callprop('floor', ((var.get('Math').callprop('random')*Js(8.0))+Js(1.0))))
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                if (var.get('i')==Js(1.0)):
                    var.put('bgText', Js('==EOF=='), '+')
            var.put('bgText', Js('==EOF==<b>Ideal:</b> '), '+')
            if (var.get('ideal')==Js(1.0)):
                var.put('bgText', Js('Knowledge. The path to power and self-improvement is through knowledge. (Neutral)'), '+')
            if (var.get('ideal')==Js(2.0)):
                var.put('bgText', Js('Beauty. What is beautiful points us beyond itself toward what is true. (Good)'), '+')
            if (var.get('ideal')==Js(3.0)):
                var.put('bgText', Js('Logic. Emotions must not cloud our logical thinking. (Lawful)'), '+')
            if (var.get('ideal')==Js(4.0)):
                var.put('bgText', Js('No Limits. Nothing should fetter the infinite possibility inherent in all existence. (Chaotic)'), '+')
            if (var.get('ideal')==Js(5.0)):
                var.put('bgText', Js('Power. Knowledge is the path to power and domination. (Evil)'), '+')
            if (var.get('ideal')==Js(6.0)):
                var.put('bgText', Js('Self-Improvement. The goal of a life of study is the betterment of oneself. (Any)'), '+')
            var.put('bgText', Js('==EOF==<b>Bond:</b> '), '+')
            if (var.get('bond')==Js(1.0)):
                var.put('bgText', Js('It is my duty to protect my students.'), '+')
            if (var.get('bond')==Js(2.0)):
                var.put('bgText', Js('I have an ancient text that holds terrible secrets that must not fall into the wrong hands.'), '+')
            if (var.get('bond')==Js(3.0)):
                var.put('bgText', Js('I work to preserve a library, university, scriptorium, or monastery.'), '+')
            if (var.get('bond')==Js(4.0)):
                var.put('bgText', Js('My life’s work is a series of tomes related to a specific field of lore.'), '+')
            if (var.get('bond')==Js(5.0)):
                var.put('bgText', Js("I've been searching my whole life for the answer to a certain question."), '+')
            if (var.get('bond')==Js(6.0)):
                var.put('bgText', Js('I sold my soul for knowledge. I hope to do great deeds and win it back.'), '+')
            var.put('bgText', Js('==EOF==<b>Flaw:</b> '), '+')
            if (var.get('flaw')==Js(1.0)):
                var.put('bgText', Js('I am easily distracted by the promise of information.'), '+')
            if (var.get('flaw')==Js(2.0)):
                var.put('bgText', Js('Most people scream and run when they see a demon. I stop and take notes on its anatomy.'), '+')
            if (var.get('flaw')==Js(3.0)):
                var.put('bgText', Js('Unlocking an ancient mystery is worth the price of a civilization.'), '+')
            if (var.get('flaw')==Js(4.0)):
                var.put('bgText', Js('I overlook obvious solutions in favor of complicated ones.'), '+')
            if (var.get('flaw')==Js(5.0)):
                var.put('bgText', Js('I speak without really thinking through my words, invariably insulting others.'), '+')
            if (var.get('flaw')==Js(6.0)):
                var.put('bgText', Js('I can’t keep a secret to save my life, or anyone else’s.'), '+')
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(11.0)):
            SWITCHED = True
            var.get('skLearn').put('3', Js(True))
            var.get('skLearn').put('11', Js(True))
            var.get('mySkills').callprop('push', Js(3.0))
            var.get('mySkills').callprop('push', Js(11.0))
            var.put('myLifestyle', Js(3.0))
            var.put('toOutput', Js(", Navigator's tools, Water vehicles"), '+')
            var.put('eqOutput', Js(', 50 feet silk rope, Lucky charm, Trinket, Common clothes'), '+')
            var.put('gold', Js(10.0), '+')
            var.put('bgOutput', Js('Sailor'), '+')
            var.put('bgOutput', Js(''), '+')
            var.put('bgText', Js('==EOF==<b>Personality:</b> '), '+')
            var.put('i', Js(0.0))
            var.put('x', var.get('personality'))
            while (var.get('i')<Js(2.0)):
                if (var.get('personality')==Js(1.0)):
                    var.put('bgText', Js('My friends know they can rely on me, no matter what. '), '+')
                if (var.get('personality')==Js(2.0)):
                    var.put('bgText', Js('I work hard so that I can play hard when the work is done. '), '+')
                if (var.get('personality')==Js(3.0)):
                    var.put('bgText', Js('I enjoy sailing into new ports and making new friends over a flagon of ale. '), '+')
                if (var.get('personality')==Js(4.0)):
                    var.put('bgText', Js('I stretch the truth for the sake of a good story. '), '+')
                if (var.get('personality')==Js(5.0)):
                    var.put('bgText', Js('To me, a tavern brawl is a nice way to get to know a new city. '), '+')
                if (var.get('personality')==Js(6.0)):
                    var.put('bgText', Js('I never pass up a friendly wager. '), '+')
                if (var.get('personality')==Js(7.0)):
                    var.put('bgText', Js('My language is as foul as an otyugh nest. '), '+')
                if (var.get('personality')==Js(8.0)):
                    var.put('bgText', Js('I like a job well done, especially if I can convince someone else to do it. '), '+')
                while (var.get('x')==var.get('personality')):
                    var.put('personality', var.get('Math').callprop('floor', ((var.get('Math').callprop('random')*Js(8.0))+Js(1.0))))
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                if (var.get('i')==Js(1.0)):
                    var.put('bgText', Js('==EOF=='), '+')
            var.put('bgText', Js('==EOF==<b>Ideal:</b> '), '+')
            if (var.get('ideal')==Js(1.0)):
                var.put('bgText', Js('Respect. The thing that keeps a ship together is mutual respect between captain and crew. (Good)'), '+')
            if (var.get('ideal')==Js(2.0)):
                var.put('bgText', Js('Fairness. We all do the work, so we all share in the rewards. (Lawful)'), '+')
            if (var.get('ideal')==Js(3.0)):
                var.put('bgText', Js('Freedom. The sea is freedom—the freedom to go anywhere and do anything. (Chaotic)'), '+')
            if (var.get('ideal')==Js(4.0)):
                var.put('bgText', Js('Mastery. I’m a predator, and the other ships on the sea are my prey. (Evil)'), '+')
            if (var.get('ideal')==Js(5.0)):
                var.put('bgText', Js('People. I’m committed to my crewmates, not to ideals. (Neutral)'), '+')
            if (var.get('ideal')==Js(6.0)):
                var.put('bgText', Js('Aspiration. Someday I’ll own my own ship and chart my own destiny. (Any)'), '+')
            var.put('bgText', Js('==EOF==<b>Bond:</b> '), '+')
            if (var.get('bond')==Js(1.0)):
                var.put('bgText', Js('I’m loyal to my captain first, everything else second.'), '+')
            if (var.get('bond')==Js(2.0)):
                var.put('bgText', Js('The ship is most important—crewmates and captains come and go.'), '+')
            if (var.get('bond')==Js(3.0)):
                var.put('bgText', Js('I’ll always remember my first ship.'), '+')
            if (var.get('bond')==Js(4.0)):
                var.put('bgText', Js('In a harbor town, I have a paramour whose eyes nearly stole me from the sea.'), '+')
            if (var.get('bond')==Js(5.0)):
                var.put('bgText', Js('I was cheated out of my fair share of the profits, and I want to get my due.'), '+')
            if (var.get('bond')==Js(6.0)):
                var.put('bgText', Js('Ruthless pirates murdered my captain and crewmates, plundered our ship, and left me to die. Vengeance will be mine.'), '+')
            var.put('bgText', Js('==EOF==<b>Flaw:</b> '), '+')
            if (var.get('flaw')==Js(1.0)):
                var.put('bgText', Js('I follow orders, even if I think they’re wrong.'), '+')
            if (var.get('flaw')==Js(2.0)):
                var.put('bgText', Js('I’ll say anything to avoid having to do extra work.'), '+')
            if (var.get('flaw')==Js(3.0)):
                var.put('bgText', Js('Once someone questions my courage, I never back down no matter how dangerous the situation.'), '+')
            if (var.get('flaw')==Js(4.0)):
                var.put('bgText', Js('Once I start drinking, it’s hard for me to stop.'), '+')
            if (var.get('flaw')==Js(5.0)):
                var.put('bgText', Js('I can’t help but pocket loose coins and other trinkets I come across.'), '+')
            if (var.get('flaw')==Js(6.0)):
                var.put('bgText', Js('My pride will probably lead to my destruction.'), '+')
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(12.0)):
            SWITCHED = True
            var.get('skLearn').put('3', Js(True))
            var.get('skLearn').put('7', Js(True))
            var.get('mySkills').callprop('push', Js(3.0))
            var.get('mySkills').callprop('push', Js(7.0))
            var.put('myLifestyle', Js(3.0))
            var.put('tempTxt', var.get('gaming').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('gaming').get('length')))))
            var.put('toOutput', ((Js(', ')+var.get('tempTxt'))+Js(', Land vehicles')), '+')
            var.put('eqOutput', Js(', Insignia of rank, War trophy, Bone dice, Common clothes'), '+')
            var.put('gold', Js(10.0), '+')
            var.put('bgOutput', Js('Soldier '), '+')
            var.put('bgOutput', Js(''), '+')
            var.put('x', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(8.0))))
            if (var.get('x')==Js(0.0)):
                var.put('bgOutput', Js('(Officer)'), '+')
            if (var.get('x')==Js(1.0)):
                var.put('bgOutput', Js('(Scout)'), '+')
            if (var.get('x')==Js(2.0)):
                var.put('bgOutput', Js('(Infantry)'), '+')
            if (var.get('x')==Js(3.0)):
                var.put('bgOutput', Js('(Cavalry)'), '+')
            if (var.get('x')==Js(4.0)):
                var.put('bgOutput', Js('(Healer)'), '+')
            if (var.get('x')==Js(5.0)):
                var.put('bgOutput', Js('(Quartermaster)'), '+')
            if (var.get('x')==Js(6.0)):
                var.put('bgOutput', Js('(Standard bearer)'), '+')
            if (var.get('x')==Js(7.0)):
                var.put('bgOutput', Js('(Support staff)'), '+')
            var.put('bgText', Js('==EOF==<b>Personality:</b> '), '+')
            var.put('i', Js(0.0))
            var.put('x', var.get('personality'))
            while (var.get('i')<Js(2.0)):
                if (var.get('personality')==Js(1.0)):
                    var.put('bgText', Js("I'm always polite and respectful. "), '+')
                if (var.get('personality')==Js(2.0)):
                    var.put('bgText', Js('I’m haunted by memories of war. I can’t get the images of violence out of my mind. '), '+')
                if (var.get('personality')==Js(3.0)):
                    var.put('bgText', Js('I’ve lost too many friends, and I’m slow to make new ones. '), '+')
                if (var.get('personality')==Js(4.0)):
                    var.put('bgText', Js('I’m full of inspiring and cautionary tales from my military experience relevant to almost every combat situation. '), '+')
                if (var.get('personality')==Js(5.0)):
                    var.put('bgText', Js('I can stare down a hell hound without flinching. '), '+')
                if (var.get('personality')==Js(6.0)):
                    var.put('bgText', Js('I enjoy being strong and like breaking things. '), '+')
                if (var.get('personality')==Js(7.0)):
                    var.put('bgText', Js('I have a crude sense of humor. '), '+')
                if (var.get('personality')==Js(8.0)):
                    var.put('bgText', Js('I face problems head-on. A simple, direct solution is the best path to success. '), '+')
                while (var.get('x')==var.get('personality')):
                    var.put('personality', var.get('Math').callprop('floor', ((var.get('Math').callprop('random')*Js(8.0))+Js(1.0))))
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                if (var.get('i')==Js(1.0)):
                    var.put('bgText', Js('==EOF=='), '+')
            var.put('bgText', Js('==EOF==<b>Ideal:</b> '), '+')
            if (var.get('ideal')==Js(1.0)):
                var.put('bgText', Js('Greater Good. Our lot is to lay down our lives in defense of others. (Good)'), '+')
            if (var.get('ideal')==Js(2.0)):
                var.put('bgText', Js('Responsibility. I do what I must and obey just authority. (Lawful)'), '+')
            if (var.get('ideal')==Js(3.0)):
                var.put('bgText', Js('Independence. When people follow orders blindly, they embrace a kind of tyranny. (Chaotic)'), '+')
            if (var.get('ideal')==Js(4.0)):
                var.put('bgText', Js('Might. In life as in war, the stronger force wins. (Evil)'), '+')
            if (var.get('ideal')==Js(5.0)):
                var.put('bgText', Js('Live and Let Live. Ideals aren’t worth killing over or going to war for. (Neutral)'), '+')
            if (var.get('ideal')==Js(6.0)):
                var.put('bgText', Js('Nation. My city, nation, or people are all that matter. (Any)'), '+')
            var.put('bgText', Js('==EOF==<b>Bond:</b> '), '+')
            if (var.get('bond')==Js(1.0)):
                var.put('bgText', Js('I would still lay down my life for the people I served with.'), '+')
            if (var.get('bond')==Js(2.0)):
                var.put('bgText', Js('Someone saved my life on the battlefield. To this day, I will never leave a friend behind.'), '+')
            if (var.get('bond')==Js(3.0)):
                var.put('bgText', Js('My honor is my life.'), '+')
            if (var.get('bond')==Js(4.0)):
                var.put('bgText', Js('I’ll never forget the crushing defeat my company suffered or the enemies who dealt it.'), '+')
            if (var.get('bond')==Js(5.0)):
                var.put('bgText', Js('Those who fight beside me are those worth dying for.'), '+')
            if (var.get('bond')==Js(6.0)):
                var.put('bgText', Js('I fight for those who cannot fight for themselves.'), '+')
            var.put('bgText', Js('==EOF==<b>Flaw:</b> '), '+')
            if (var.get('flaw')==Js(1.0)):
                var.put('bgText', Js('The monstrous enemy we faced in battle still leaves me quivering with fear.'), '+')
            if (var.get('flaw')==Js(2.0)):
                var.put('bgText', Js('I have little respect for anyone who is not a proven warrior.'), '+')
            if (var.get('flaw')==Js(3.0)):
                var.put('bgText', Js('I made a terrible mistake in battle cost many lives— and I would do anything to keep that mistake secret.'), '+')
            if (var.get('flaw')==Js(4.0)):
                var.put('bgText', Js('My hatred of my enemies is blind and unreasoning.'), '+')
            if (var.get('flaw')==Js(5.0)):
                var.put('bgText', Js('I obey the law, even if the law causes misery.'), '+')
            if (var.get('flaw')==Js(6.0)):
                var.put('bgText', Js('I’d rather eat my armor than admit when I’m wrong.'), '+')
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(13.0)):
            SWITCHED = True
            var.get('skLearn').put('15', Js(True))
            var.get('skLearn').put('16', Js(True))
            var.get('mySkills').callprop('push', Js(15.0))
            var.get('mySkills').callprop('push', Js(16.0))
            var.put('myLifestyle', Js(3.0))
            var.put('toOutput', Js(",  Disguise kit,  Thieves' tools"), '+')
            var.put('eqOutput', Js(', Token, Common clothes'), '+')
            var.put('gold', Js(10.0), '+')
            var.put('bgOutput', Js('Urchin'), '+')
            var.put('bgOutput', Js(''), '+')
            var.put('bgText', Js('==EOF==<b>Personality:</b> '), '+')
            var.put('i', Js(0.0))
            var.put('x', var.get('personality'))
            while (var.get('i')<Js(2.0)):
                if (var.get('personality')==Js(1.0)):
                    var.put('bgText', Js('I hide scraps of food and trinkets away in my pockets. '), '+')
                if (var.get('personality')==Js(2.0)):
                    var.put('bgText', Js('I ask a lot of questions. '), '+')
                if (var.get('personality')==Js(3.0)):
                    var.put('bgText', Js('I like to squeeze into small places where no one else can get to me. '), '+')
                if (var.get('personality')==Js(4.0)):
                    var.put('bgText', Js('I sleep with my back to a wall or tree, with everything I own wrapped in a bundle in my arms. '), '+')
                if (var.get('personality')==Js(5.0)):
                    var.put('bgText', Js('I eat like a pig and have bad manners. '), '+')
                if (var.get('personality')==Js(6.0)):
                    var.put('bgText', Js('I think anyone who’s nice to me is hiding evil intent. '), '+')
                if (var.get('personality')==Js(7.0)):
                    var.put('bgText', Js('I don’t like to bathe. '), '+')
                if (var.get('personality')==Js(8.0)):
                    var.put('bgText', Js('I bluntly say what other people are hinting at or hiding. '), '+')
                while (var.get('x')==var.get('personality')):
                    var.put('personality', var.get('Math').callprop('floor', ((var.get('Math').callprop('random')*Js(8.0))+Js(1.0))))
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                if (var.get('i')==Js(1.0)):
                    var.put('bgText', Js('==EOF=='), '+')
            var.put('bgText', Js('==EOF==<b>Ideal:</b> '), '+')
            if (var.get('ideal')==Js(1.0)):
                var.put('bgText', Js('Respect. All people, rich or poor, deserve respect. (Good)'), '+')
            if (var.get('ideal')==Js(2.0)):
                var.put('bgText', Js('Community. We have to take care of each other, because no one else is going to do it. (Lawful)'), '+')
            if (var.get('ideal')==Js(3.0)):
                var.put('bgText', Js('Change. The low are lifted up, and the high and mighty are brought down. Change is the nature of things. (Chaotic)'), '+')
            if (var.get('ideal')==Js(4.0)):
                var.put('bgText', Js('Retribution. The rich need to be shown what life and death are like in the gutters. (Evil)'), '+')
            if (var.get('ideal')==Js(5.0)):
                var.put('bgText', Js('People. I help the people who help me—that’s what keeps us alive. (Neutral)'), '+')
            if (var.get('ideal')==Js(6.0)):
                var.put('bgText', Js("Aspiration. I'm going to prove that I'm worthy of a better life."), '+')
            var.put('bgText', Js('==EOF==<b>Bond:</b> '), '+')
            if (var.get('bond')==Js(1.0)):
                var.put('bgText', Js('My town or city is my home, and I’ll fight to defend it.'), '+')
            if (var.get('bond')==Js(2.0)):
                var.put('bgText', Js('I sponsor an orphanage to keep others from enduring what I was forced to endure.'), '+')
            if (var.get('bond')==Js(3.0)):
                var.put('bgText', Js('I owe my survival to another urchin who taught me to live on the streets.'), '+')
            if (var.get('bond')==Js(4.0)):
                var.put('bgText', Js('I owe a debt I can never repay to the person who took pity on me.'), '+')
            if (var.get('bond')==Js(5.0)):
                var.put('bgText', Js('I escaped my life of poverty by robbing an important person, and I’m wanted for it.'), '+')
            if (var.get('bond')==Js(6.0)):
                var.put('bgText', Js('No one else should have to endure the hardships I’ve been through.'), '+')
            var.put('bgText', Js('==EOF==<b>Flaw:</b> '), '+')
            if (var.get('flaw')==Js(1.0)):
                var.put('bgText', Js("If I'm outnumbered, I will run away from a fight."), '+')
            if (var.get('flaw')==Js(2.0)):
                var.put('bgText', Js('Gold seems like a lot of money to me, and I’ll do just about anything for more of it.'), '+')
            if (var.get('flaw')==Js(3.0)):
                var.put('bgText', Js('I will never fully trust anyone other than myself.'), '+')
            if (var.get('flaw')==Js(4.0)):
                var.put('bgText', Js('I’d rather kill someone in their sleep then fight fair.'), '+')
            if (var.get('flaw')==Js(5.0)):
                var.put('bgText', Js('It’s not stealing if I need it more than someone else.'), '+')
            if (var.get('flaw')==Js(6.0)):
                var.put('bgText', Js("People who can't take care of themselves get what they deserve."), '+')
            break
        SWITCHED = True
        break
    var.put('bgOutput', var.get('bgText'), '+')
    if (var.get('al')==Js(True)):
        var.put('eqOutput', Js(', Trinket'), '+')
    while 1:
        SWITCHED = False
        CONDITION = (var.get('cl'))
        if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
            SWITCHED = True
            #for JS loop
            var.put('x', Js(2.0))
            while (var.get('x')>Js(0.0)):
                try:
                    var.get('mySkills').callprop('push', var.get('pickSome')(Js([Js(1.0), Js(3.0), Js(7.0), Js(10.0), Js(11.0), Js(17.0)])))
                finally:
                        (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
            SWITCHED = True
            var.put('x', Js(3.0))
            if (var.get('classtxt').callprop('indexOf', Js('Lore'))>(-Js(1.0))):
                var.put('x', Js(6.0))
            #for JS loop
            
            while (var.get('x')>Js(0.0)):
                try:
                    if (var.get('Math').callprop('random')<Js(0.7)):
                        var.get('mySkills').callprop('push', var.get('pickSome')(Js([Js(0.0), Js(4.0), Js(7.0), Js(11.0), Js(9.0), Js(12.0), Js(13.0), Js(15.0), Js(16.0)])))
                    else:
                        var.get('mySkills').callprop('push', var.get('pickSome')(Js([Js(0.0), Js(1.0), Js(2.0), Js(3.0), Js(4.0), Js(5.0), Js(6.0), Js(7.0), Js(8.0), Js(9.0), Js(10.0), Js(11.0), Js(12.0), Js(13.0), Js(14.0), Js(15.0), Js(16.0), Js(17.0)])))
                finally:
                        (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
            if (var.get('level')>Js(2.0)):
                var.put('y', Js(2.0))
                if (var.get('level')>Js(9.0)):
                    var.put('y', Js(2.0), '+')
                    if (var.get('mySkills').get('length')<Js(4.0)):
                        var.put('y', Js(3.0))
                while (var.get('y')>Js(0.0)):
                    var.put('x', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('mySkills').get('length'))))
                    if (var.get('expertise').callprop('indexOf', var.get('mySkills').get(var.get('x')))==(-Js(1.0))):
                        var.get('expertise').callprop('push', var.get('mySkills').get(var.get('x')))
                        var.get('console').callprop('log', (Js('expertise:')+var.get('x')))
                        (var.put('y',Js(var.get('y').to_number())-Js(1))+Js(1))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(3.0)):
            SWITCHED = True
            #for JS loop
            var.put('x', Js(2.0))
            while (var.get('x')>Js(0.0)):
                try:
                    var.get('mySkills').callprop('push', var.get('pickSome')(Js([Js(5.0), Js(6.0), Js(9.0), Js(13.0), Js(14.0)])))
                finally:
                        (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(4.0)):
            SWITCHED = True
            #for JS loop
            var.put('x', Js(2.0))
            while (var.get('x')>Js(0.0)):
                try:
                    var.get('mySkills').callprop('push', var.get('pickSome')(Js([Js(1.0), Js(6.0), Js(9.0), Js(10.0), Js(11.0), Js(14.0), Js(17.0)])))
                finally:
                        (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(5.0)):
            SWITCHED = True
            #for JS loop
            var.put('x', Js(2.0))
            while (var.get('x')>Js(0.0)):
                try:
                    var.get('mySkills').callprop('push', var.get('pickSome')(Js([Js(0.0), Js(1.0), Js(3.0), Js(5.0), Js(6.0), Js(7.0), Js(11.0), Js(17.0)])))
                finally:
                        (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(6.0)):
            SWITCHED = True
            #for JS loop
            var.put('x', Js(2.0))
            while (var.get('x')>Js(0.0)):
                try:
                    var.get('mySkills').callprop('push', var.get('pickSome')(Js([Js(0.0), Js(1.0), Js(3.0), Js(5.0), Js(6.0), Js(7.0), Js(11.0), Js(17.0)])))
                finally:
                        (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(7.0)):
            SWITCHED = True
            #for JS loop
            var.put('x', Js(2.0))
            while (var.get('x')>Js(0.0)):
                try:
                    var.get('mySkills').callprop('push', var.get('pickSome')(Js([Js(0.0), Js(1.0), Js(3.0), Js(5.0), Js(6.0), Js(7.0), Js(11.0), Js(17.0)])))
                finally:
                        (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(8.0)):
            SWITCHED = True
            #for JS loop
            var.put('x', Js(2.0))
            while (var.get('x')>Js(0.0)):
                try:
                    var.get('mySkills').callprop('push', var.get('pickSome')(Js([Js(0.0), Js(3.0), Js(5.0), Js(6.0), Js(14.0), Js(16.0)])))
                finally:
                        (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(9.0)):
            SWITCHED = True
            #for JS loop
            var.put('x', Js(2.0))
            while (var.get('x')>Js(0.0)):
                try:
                    var.get('mySkills').callprop('push', var.get('pickSome')(Js([Js(0.0), Js(6.0), Js(7.0), Js(9.0), Js(13.0), Js(14.0)])))
                finally:
                        (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(10.0)):
            SWITCHED = True
            #for JS loop
            var.put('x', Js(3.0))
            while (var.get('x')>Js(0.0)):
                try:
                    var.get('mySkills').callprop('push', var.get('pickSome')(Js([Js(1.0), Js(3.0), Js(6.0), Js(8.0), Js(10.0), Js(11.0), Js(16.0), Js(17.0)])))
                finally:
                        (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(11.0)):
            SWITCHED = True
            #for JS loop
            var.put('x', Js(4.0))
            while (var.get('x')>Js(0.0)):
                try:
                    var.put('y', (var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(10.0)))+Js(1.0)))
                    if (var.get('y')<Js(9.0)):
                        var.put('tempAr', Js([Js(0.0), Js(11.0), Js(11.0), Js(15.0), Js(16.0), Js(16.0), Js(16.0), Js(16.0)]))
                        if (var.get('mod').get('3')>Js(0.0)):
                            var.get('tempAr').callprop('push', Js(8.0))
                        if (var.get('mod').get('5')>Js(0.0)):
                            var.get('tempAr').callprop('push', Js(4.0), Js(7.0), Js(12.0), Js(13.0))
                        var.get('mySkills').callprop('push', var.get('pickSome')(var.get('tempAr')))
                    else:
                        var.get('mySkills').callprop('push', var.get('pickSome')(Js([Js(0.0), Js(3.0), Js(4.0), Js(6.0), Js(7.0), Js(8.0), Js(11.0), Js(12.0), Js(13.0), Js(15.0), Js(16.0)])))
                finally:
                        (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
            var.put('z', Js(2.0))
            if (var.get('level')>Js(5.0)):
                var.put('z', Js(4.0))
            if (var.get('burglar')==Js(True)):
                (var.put('z',Js(var.get('z').to_number())-Js(1))+Js(1))
                var.get('console').callprop('log', Js('expertise: thieves tools'))
            while (var.get('z')>Js(0.0)):
                var.put('x', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('mySkills').get('length'))))
                if ((var.get('Math').callprop('random')<Js(0.5)) and (var.get('expertise').callprop('indexOf', Js(16.0))>(-Js(1.0)))):
                    var.put('x', var.get('mySkills').callprop('indexOf', Js(16.0)))
                while (var.get('expertise').callprop('indexOf', var.get('mySkills').get(var.get('x')))>(-Js(1.0))):
                    var.put('x', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('mySkills').get('length'))))
                var.get('expertise').callprop('push', var.get('mySkills').get(var.get('x')))
                (var.put('z',Js(var.get('z').to_number())-Js(1))+Js(1))
                var.get('console').callprop('log', (Js('expertise:  ')+var.get('expertise')))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(12.0)):
            SWITCHED = True
            #for JS loop
            var.put('x', Js(4.0))
            while (var.get('x')>Js(0.0)):
                try:
                    var.get('mySkills').callprop('push', var.get('pickSome')(Js([Js(0.0), Js(3.0), Js(4.0), Js(6.0), Js(7.0), Js(8.0), Js(11.0), Js(12.0), Js(13.0), Js(15.0), Js(16.0), Js(16.0), Js(16.0)])))
                finally:
                        (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
            var.put('z', Js(2.0))
            if (var.get('level')>Js(5.0)):
                var.put('z', Js(4.0))
            if (var.get('burglar')==Js(True)):
                (var.put('z',Js(var.get('z').to_number())-Js(1))+Js(1))
                var.get('console').callprop('log', Js('expertise: thieves tools'))
            while (var.get('z')>Js(0.0)):
                var.put('x', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('mySkills').get('length'))))
                if ((var.get('Math').callprop('random')<Js(0.5)) and (var.get('expertise').callprop('indexOf', Js(16.0))>(-Js(1.0)))):
                    var.put('x', var.get('mySkills').callprop('indexOf', Js(16.0)))
                while (var.get('expertise').callprop('indexOf', var.get('mySkills').get(var.get('x')))>(-Js(1.0))):
                    var.put('x', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('mySkills').get('length'))))
                var.get('expertise').callprop('push', var.get('mySkills').get(var.get('x')))
                (var.put('z',Js(var.get('z').to_number())-Js(1))+Js(1))
                var.get('console').callprop('log', (Js('expertise:  ')+var.get('expertise')))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(13.0)):
            SWITCHED = True
            #for JS loop
            var.put('x', Js(2.0))
            while (var.get('x')>Js(0.0)):
                try:
                    var.get('mySkills').callprop('push', var.get('pickSome')(Js([Js(2.0), Js(4.0), Js(6.0), Js(7.0), Js(13.0), Js(14.0)])))
                finally:
                        (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(14.0)):
            SWITCHED = True
            #for JS loop
            var.put('x', Js(2.0))
            while (var.get('x')>Js(0.0)):
                try:
                    var.get('mySkills').callprop('push', var.get('pickSome')(Js([Js(2.0), Js(4.0), Js(5.0), Js(7.0), Js(8.0), Js(10.0), Js(14.0)])))
                finally:
                        (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(15.0)):
            SWITCHED = True
            #for JS loop
            var.put('x', Js(2.0))
            while (var.get('x')>Js(0.0)):
                try:
                    var.get('mySkills').callprop('push', var.get('pickSome')(Js([Js(2.0), Js(5.0), Js(6.0), Js(8.0), Js(9.0), Js(14.0)])))
                finally:
                        (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
            break
        SWITCHED = True
        break
    if (var.get('racetxt')==Js('Half-Elf')):
        #for JS loop
        var.put('x', Js(2.0))
        while (var.get('x')>Js(0.0)):
            try:
                var.get('mySkills').callprop('push', var.get('pickSome')(Js([Js(0.0), Js(1.0), Js(2.0), Js(3.0), Js(4.0), Js(5.0), Js(6.0), Js(7.0), Js(8.0), Js(9.0), Js(10.0), Js(11.0), Js(12.0), Js(13.0), Js(14.0), Js(15.0), Js(16.0), Js(17.0)])))
            finally:
                    (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
    @Js
    def PyJs_anonymous_12_(a, b, this, arguments, var=var):
        var = Scope({'this':this, 'a':a, 'b':b, 'arguments':arguments}, var)
        var.registers(['a', 'b'])
        return (var.get('a')-var.get('b'))
    PyJs_anonymous_12_._set_name('anonymous')
    var.get('mySkills').callprop('sort', PyJs_anonymous_12_)
    var.put('first', Js(False))
    #for JS loop
    var.put('x', Js(0.0))
    while (var.get('x')<Js(18.0)):
        try:
            if (var.get('skLearn').get(var.get('x'))==Js(True)):
                if (var.get('first')==Js(False)):
                    pass
                else:
                    var.put('skOutput', Js(', '), '+')
                var.get('console').callprop('log', (((Js('skills:')+var.get('mySkills'))+Js(' /expertise:'))+var.get('expertise')))
                if (var.get('expertise').callprop('indexOf', var.get('x'))==(-Js(1.0))):
                    var.put('skOutput', ((var.get('skills').get(var.get('x'))+Js(' '))+var.get('showPlus')((var.get('mod').get(var.get('skAbil').get(var.get('x')))+var.get('prof')))), '+')
                else:
                    var.put('skOutput', ((((Js('')+var.get('skills').get(var.get('x')))+Js(' '))+var.get('showPlus')((var.get('mod').get(var.get('skAbil').get(var.get('x')))+(var.get('prof')*Js(2.0)))))+Js(' (Expertise)')), '+')
                var.put('first', Js(True))
        finally:
                (var.put('x',Js(var.get('x').to_number())+Js(1))-Js(1))
    if (var.get('burglar')==Js(True)):
        var.put('skOutput', Js(", Expert with Thieves' Tools"), '+')
    var.put('first', Js(False))
    var.put('skOutput', Js('==EOF==<b>Non-proficient skills:</b>==EOF=='), '+')
    #for JS loop
    var.put('x', Js(0.0))
    while (var.get('x')<Js(18.0)):
        try:
            if (var.get('skLearn').get(var.get('x'))==Js(False)):
                if (var.get('first')==Js(False)):
                    pass
                else:
                    var.put('skOutput', Js(',==EOF=='), '+')
                var.put('skOutput', ((var.get('skills').get(var.get('x'))+Js(' '))+var.get('showPlus')(var.get('mod').get(var.get('skAbil').get(var.get('x'))))), '+')
                var.put('first', Js(True))
        finally:
                (var.put('x',Js(var.get('x').to_number())+Js(1))-Js(1))
    var.put('i', Js(0.0))
    while (var.get('moreLang')>Js(0.0)):
        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
        var.put('newLang', Js(''))
        var.put('exotic', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(9.0))))
        if (var.get('exotic')==Js(0.0)):
            var.put('x', var.get('Math').callprop('floor', ((var.get('Math').callprop('random')*Js(8.0))+Js(1.0))))
            while 1:
                SWITCHED = False
                CONDITION = (var.get('x'))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
                    SWITCHED = True
                    var.put('newLang', Js('Abyssal'))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                    SWITCHED = True
                    var.put('newLang', Js('Celestial'))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js(3.0)):
                    SWITCHED = True
                    var.put('newLang', Js('Draconic'))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js(4.0)):
                    SWITCHED = True
                    var.put('newLang', Js('Deep Speech'))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js(5.0)):
                    SWITCHED = True
                    var.put('newLang', Js('Infernal'))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js(6.0)):
                    SWITCHED = True
                    var.put('newLang', Js('Primordial'))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js(7.0)):
                    SWITCHED = True
                    var.put('newLang', Js('Sylvan'))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js(8.0)):
                    SWITCHED = True
                    var.put('newLang', Js('Undercommon'))
                    break
                SWITCHED = True
                break
            if (var.get('languageOutput').callprop('indexOf', var.get('newLang'))==(-Js(1.0))):
                var.put('languageOutput', (Js(', ')+var.get('newLang')), '+')
                (var.put('moreLang',Js(var.get('moreLang').to_number())-Js(1))+Js(1))
        else:
            var.put('x', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(7.0))))
            while 1:
                SWITCHED = False
                CONDITION = (var.get('x'))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
                    SWITCHED = True
                    var.put('newLang', Js('Dwarvish'))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                    SWITCHED = True
                    var.put('newLang', Js('Elvish'))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js(3.0)):
                    SWITCHED = True
                    var.put('newLang', Js('Giant'))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js(4.0)):
                    SWITCHED = True
                    var.put('newLang', Js('Goblin'))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js(5.0)):
                    SWITCHED = True
                    var.put('newLang', Js('Gnomish'))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js(6.0)):
                    SWITCHED = True
                    var.put('newLang', Js('Halfling'))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js(7.0)):
                    SWITCHED = True
                    var.put('newLang', Js('Orc'))
                    break
                SWITCHED = True
                break
            if (var.get('languageOutput').callprop('indexOf', var.get('newLang'))==(-Js(1.0))):
                var.put('languageOutput', (Js(', ')+var.get('newLang')), '+')
                (var.put('moreLang',Js(var.get('moreLang').to_number())-Js(1))+Js(1))
    if (var.get('racetxt')==Js('High Elf')):
        var.put('x', Js(1.0))
        while (var.get('x')>Js(0.0)):
            if (var.get('Math').callprop('random')<Js(0.5)):
                var.put('tempAr', Js([Js('Acid Splash'), Js('Blade Ward'), Js('Chill Touch'), Js('Fire Bolt'), Js('Minor Illusion'), Js('Poison Spray'), Js('Ray of Frost'), Js('Shocking Grasp'), Js('True Strike')]))
            else:
                var.put('tempAr', var.get('wiCantrip'))
            var.put('temp', var.get('tempAr').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tempAr').get('length')))))
            if (var.get('mySpells').callprop('indexOf', var.get('temp'))==(-Js(1.0))):
                var.get('raceSpells').callprop('push', var.get('temp'))
                (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
    if (var.get('cl')==Js(2.0)):
        var.put('ss1', (var.get('level')+Js(1.0)))
        var.put('ss2', Js(0.0))
        if (var.get('level')>Js(2.0)):
            var.put('ss2', Js(2.0))
        if (var.get('level')>Js(3.0)):
            var.put('ss1', Js(4.0))
            var.put('ss2', Js(3.0))
        if (var.get('level')>Js(3.0)):
            var.put('ss1', Js(4.0))
            var.put('ss2', Js(3.0))
        if (var.get('level')==Js(5.0)):
            var.put('ss3', Js(2.0))
        if (var.get('level')>Js(5.0)):
            var.put('ss3', Js(3.0))
        if (var.get('level')>Js(6.0)):
            var.put('ss4', (var.get('level')-Js(6.0)))
        if (var.get('level')>Js(8.0)):
            var.put('ss4', Js(3.0))
            var.put('ss5', (var.get('level')-Js(8.0)))
        var.put('sp1', Js(4.0))
        var.put('sp2', Js(0.0))
        if (var.get('level')>Js(1.0)):
            var.put('sp1', Js(5.0))
        if (var.get('level')>Js(2.0)):
            var.put('sp2', (var.get('level')-Js(2.0)))
        if (var.get('level')>Js(4.0)):
            var.put('sp2', Js(2.0))
            var.put('sp3', (var.get('level')-Js(4.0)))
        if (var.get('level')>Js(6.0)):
            var.put('sp3', Js(2.0))
            var.put('sp4', (var.get('level')-Js(6.0)))
        if (var.get('level')>Js(8.0)):
            var.put('sp4', Js(2.0))
            var.put('sp5', Js(1.0))
        if (var.get('level')>Js(9.0)):
            var.put('sp5', Js(3.0))
        var.get('console').callprop('log', ((((((((((Js('spellsknown:  ')+var.get('sp1'))+Js('/'))+var.get('sp2'))+Js('/'))+var.get('sp3'))+Js('/'))+var.get('sp4'))+Js('/'))+var.get('sp5'))+Js('/')))
        var.put('sp', ((((var.get('sp1')+var.get('sp2'))+var.get('sp3'))+var.get('sp4'))+var.get('sp5')))
        var.put('x', Js(2.0))
        if (var.get('level')>Js(3.0)):
            var.put('x', Js(3.0))
        if (var.get('level')>Js(9.0)):
            var.put('x', Js(4.0))
        while (var.get('x')>Js(0.0)):
            var.put('tempAr', var.get('baCantrip'))
            if (var.get('Math').callprop('random')<Js(0.66)):
                var.put('tempAr', Js([Js('Blade Ward'), Js('Minor Illusion'), Js('True Strike'), Js('Vicious Mockery')]))
            var.put('temp', var.get('tempAr').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tempAr').get('length')))))
            if ((var.get('myCantrips').callprop('indexOf', var.get('temp'))==(-Js(1.0))) and (var.get('raceSpells').callprop('indexOf', var.get('temp'))==(-Js(1.0)))):
                var.get('myCantrips').callprop('push', var.get('temp'))
                (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
        var.get('myCantrips').callprop('sort')
        var.put('tempSpells', Js([]))
        var.put('x', var.get('sp1'))
        while (var.get('x')>Js(0.0)):
            var.put('tempAr', var.get('ba1'))
            if (var.get('Math').callprop('random')<Js(0.66)):
                var.put('tempAr', Js([Js('Charm Person'), Js('Cure Wounds'), Js('Cure Wounds'), Js('Dissonant Whispers'), Js('Dissonant Whispers'), Js('Healing Word'), Js('Healing Word'), Js('Silent Image'), Js('Sleep'), Js("Tasha's Hideous Laughter"), Js('Thunderwave'), Js('Thunderwave')]))
            var.put('temp', var.get('tempAr').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tempAr').get('length')))))
            if (var.get('tempSpells').callprop('indexOf', var.get('temp'))>(-Js(1.0))):
                pass
            else:
                var.get('tempSpells').callprop('push', var.get('temp'))
                (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
        var.get('tempSpells').callprop('sort')
        var.put('mySpells', var.get('mySpells').callprop('concat', var.get('tempSpells')))
        var.put('tempSpells', Js([]))
        var.put('x', var.get('sp2'))
        while (var.get('x')>Js(0.0)):
            var.put('tempAr', var.get('ba2'))
            if (var.get('Math').callprop('random')<Js(0.66)):
                var.put('tempAr', Js([Js('Blindness/Deafness'), Js('Cloud of Daggers'), Js('Crown of Madness'), Js('Enhance Ability'), Js('Heat Metal'), Js('Hold Person'), Js('Invisibility'), Js('Phantasmal Force'), Js('Shatter'), Js('Suggestion')]))
            var.put('temp', var.get('tempAr').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tempAr').get('length')))))
            if (var.get('tempSpells').callprop('indexOf', var.get('temp'))==(-Js(1.0))):
                var.get('tempSpells').callprop('push', var.get('temp'))
                (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
        var.get('tempSpells').callprop('sort')
        var.put('mySpells', var.get('mySpells').callprop('concat', var.get('tempSpells')))
        var.put('tempSpells', Js([]))
        var.put('x', var.get('sp3'))
        while (var.get('x')>Js(0.0)):
            var.put('tempAr', var.get('ba3'))
            if (var.get('Math').callprop('random')<Js(0.5)):
                var.put('tempAr', Js([Js('Bestow Curse'), Js('Clairvoyance'), Js('Dispel Magic'), Js('Fear'), Js('Glyph of Warding'), Js('Hypnotic Pattern'), Js('Leomund’s Tiny Hut'), Js('Major Image'), Js('Stinking Cloud')]))
            var.put('temp', var.get('tempAr').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tempAr').get('length')))))
            if (var.get('tempSpells').callprop('indexOf', var.get('temp'))==(-Js(1.0))):
                var.get('tempSpells').callprop('push', var.get('temp'))
                (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
        var.get('tempSpells').callprop('sort')
        var.put('mySpells', var.get('mySpells').callprop('concat', var.get('tempSpells')))
        var.put('tempSpells', Js([]))
        var.put('x', var.get('sp4'))
        while (var.get('x')>Js(0.0)):
            var.put('tempAr', var.get('ba4'))
            if (var.get('Math').callprop('random')<Js(0.5)):
                var.put('tempAr', Js([Js('Compulsion'), Js('Confusion'), Js('Dimension Door'), Js('Greater Invisibility'), Js('Polymorph')]))
            var.put('temp', var.get('tempAr').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tempAr').get('length')))))
            if (var.get('tempSpells').callprop('indexOf', var.get('temp'))==(-Js(1.0))):
                var.get('tempSpells').callprop('push', var.get('temp'))
                (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
        var.get('tempSpells').callprop('sort')
        var.put('mySpells', var.get('mySpells').callprop('concat', var.get('tempSpells')))
        var.put('tempSpells', Js([]))
        var.put('x', var.get('sp5'))
        while (var.get('x')>Js(0.0)):
            var.put('tempAr', var.get('ba5'))
            if (var.get('Math').callprop('random')<Js(0.5)):
                var.put('tempAr', Js([Js('Animate Objects'), Js('Dominate Person'), Js('Geas'), Js('Greater Restoration'), Js('Hold Monster'), Js('Legend Lore'), Js('Mass Cure Wounds'), Js('Mass Cure Wounds'), Js('Mislead'), Js('Modify Memory'), Js('Planar Binding'), Js('Raise Dead'), Js('Seeming'), Js('Teleportation Circle')]))
            var.put('temp', var.get('tempAr').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tempAr').get('length')))))
            if (var.get('tempSpells').callprop('indexOf', var.get('temp'))==(-Js(1.0))):
                var.get('tempSpells').callprop('push', var.get('temp'))
                (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
        var.get('tempSpells').callprop('sort')
        var.put('mySpells', var.get('mySpells').callprop('concat', var.get('tempSpells')))
        if (var.get('abOutput').callprop('indexOf', Js('Additional Magic'))>(-Js(1.0))):
            var.put('tempSpells', Js([]))
            var.put('x', Js(2.0))
            while (var.get('x')>Js(0.0)):
                var.put('tempAr', Js([Js('Fireball'), Js('Lightning Bolt'), Js('Fly'), Js('Gaseous Form'), Js('Mass Healing Word'), Js('Revivify'), Js('Call Lightning'), Js('Conjure Animals'), Js('Wind Wall'), Js('Blinding Smite'), Js('Lightning Arrow'), Js('Conjure Barrage'), Js('Aura of Vitality')]))
                var.put('temp', var.get('tempAr').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tempAr').get('length')))))
                if (var.get('tempSpells').callprop('indexOf', var.get('temp'))==(-Js(1.0))):
                    var.get('tempSpells').callprop('push', var.get('temp'))
                    (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
            var.get('tempSpells').callprop('sort')
            var.put('loSpells', var.get('loSpells').callprop('concat', var.get('tempSpells')))
        if (var.get('level')>Js(9.0)):
            var.put('tempSpells', Js([]))
            var.put('x', Js(2.0))
            while (var.get('x')>Js(0.0)):
                var.put('tempAr', Js([Js('Ice Storm'), Js('Bigby’s Hand'), Js('CloudkilI'), Js('Cone of Cold'), Js('Conjure Elemental'), Js('Passwall'), Js('Wall of Force'), Js('Wall of Stone'), Js('Antilife Shell'), Js('Contagion'), Js('Insect Plague'), Js('Flame Strike'), Js('Death Ward'), Js('Conjure Volley'), Js('Conjure Woodland Beings'), Js('Banishing Smite')]))
                var.put('temp', var.get('tempAr').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tempAr').get('length')))))
                if (var.get('tempSpells').callprop('indexOf', var.get('temp'))==(-Js(1.0))):
                    var.get('tempSpells').callprop('push', var.get('temp'))
                    (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
            var.get('tempSpells').callprop('sort')
            var.put('loSpells', var.get('loSpells').callprop('concat', var.get('tempSpells')))
    if (var.get('cl')==Js(3.0)):
        var.put('ss1', (var.get('level')+Js(1.0)))
        var.put('ss2', Js(0.0))
        if (var.get('level')>Js(2.0)):
            var.put('ss2', Js(2.0))
        if (var.get('level')>Js(3.0)):
            var.put('ss1', Js(4.0))
            var.put('ss2', Js(3.0))
        if (var.get('level')==Js(5.0)):
            var.put('ss3', Js(2.0))
        if (var.get('level')>Js(5.0)):
            var.put('ss3', Js(3.0))
        if (var.get('level')>Js(6.0)):
            var.put('ss4', (var.get('level')-Js(6.0)))
        if (var.get('level')>Js(8.0)):
            var.put('ss4', Js(3.0))
            var.put('ss5', (var.get('level')-Js(8.0)))
        var.put('sp', (var.get('level')+var.get('mod').get('4')))
        var.put('sp1', Js(0.0))
        var.put('sp2', Js(0.0))
        var.put('sp3', Js(0.0))
        var.put('sp4', Js(0.0))
        var.put('sp5', Js(0.0))
        if (var.get('level')<Js(3.0)):
            var.put('sp1', var.get('sp'))
            var.put('sp2', Js(0.0))
        else:
            if (var.get('level')<Js(5.0)):
                var.put('x', var.get('Math').callprop('floor', (var.get('sp')*Js(0.7))))
                var.put('sp1', var.get('x'))
                var.put('sp2', (var.get('sp')-var.get('x')))
            else:
                if (var.get('level')<Js(7.0)):
                    var.put('x', var.get('Math').callprop('ceil', (var.get('sp')*Js(0.35))))
                    var.put('y', var.get('Math').callprop('floor', (var.get('sp')*Js(0.35))))
                    var.put('sp1', var.get('x'))
                    var.put('z', ((var.get('sp')-var.get('x'))-var.get('y')))
                    var.put('sp2', var.get('y'))
                    var.put('sp3', var.get('z'))
                else:
                    if (var.get('level')<Js(9.0)):
                        var.put('x', var.get('Math').callprop('floor', (var.get('sp')*Js(0.28))))
                        var.put('y', var.get('Math').callprop('floor', (var.get('sp')*Js(0.28))))
                        var.put('z', var.get('Math').callprop('floor', (var.get('sp')*Js(0.28))))
                        var.put('sum', (((var.get('sp')-var.get('x'))-var.get('y'))-var.get('z')))
                        var.put('sp1', var.get('sum'))
                        var.put('sp2', var.get('y'))
                        var.put('sp3', var.get('z'))
                        var.put('sp4', var.get('x'))
                    else:
                        if (var.get('level')>Js(8.0)):
                            var.put('x', var.get('Math').callprop('floor', (var.get('sp')*Js(0.21))))
                            var.put('y', var.get('Math').callprop('ceil', (var.get('sp')*Js(0.18))))
                            var.put('z', var.get('Math').callprop('ceil', (var.get('sp')*Js(0.18))))
                            var.put('xx', var.get('Math').callprop('floor', (var.get('sp')*Js(0.21))))
                            var.put('sum', ((((var.get('sp')-var.get('x'))-var.get('y'))-var.get('z'))-var.get('xx')))
                            var.put('sp1', var.get('sum'))
                            var.put('sp2', var.get('y'))
                            var.put('sp3', var.get('z'))
                            var.put('sp4', var.get('xx'))
                            var.put('sp5', var.get('x'))
        var.get('console').callprop('log', (((((((((((Js('Spells known:  ')+var.get('sp1'))+Js('/ '))+var.get('sp2'))+Js('/ '))+var.get('sp3'))+Js('/ '))+var.get('sp4'))+Js('/ '))+var.get('sp5'))+Js(' / Total = '))+var.get('sp')))
        if (((((var.get('sp1')+var.get('sp2'))+var.get('sp3'))+var.get('sp4'))+var.get('sp5'))!=var.get('sp')):
            var.get('console').callprop('log', Js('not the right number of spells known'))
        var.put('x', Js(0.0))
        if (var.get('clDomain')==Js(3.0)):
            var.put('x', Js(1.0))
            while (var.get('x')>Js(0.0)):
                var.put('tempAr', var.get('drCantrip'))
                if (var.get('Math').callprop('random')<Js(0.66)):
                    var.put('tempAr', Js([Js('Druidcraft'), Js('Guidance'), Js('Poison Spray'), Js('Resistance'), Js('Shillelagh'), Js('Thorn Whip')]))
                var.put('temp', var.get('tempAr').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tempAr').get('length')))))
                if ((var.get('myCantrips').callprop('indexOf', var.get('temp'))==(-Js(1.0))) and (var.get('raceSpells').callprop('indexOf', var.get('temp'))==(-Js(1.0)))):
                    var.get('myCantrips').callprop('push', var.get('temp'))
                    (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
        if (var.get('clDomain')==Js(7.0)):
            var.put('x', Js(1.0))
            while (var.get('x')>Js(0.0)):
                var.put('tempAr', Js([Js('Chill Touch'), Js('Chill Touch'), Js('Spare the Dying')]))
                var.put('temp', var.get('tempAr').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tempAr').get('length')))))
                if ((var.get('myCantrips').callprop('indexOf', var.get('temp'))==(-Js(1.0))) and (var.get('raceSpells').callprop('indexOf', var.get('temp'))==(-Js(1.0)))):
                    var.get('myCantrips').callprop('push', var.get('temp'))
                    (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
        var.put('x', Js(3.0))
        if (var.get('level')>Js(3.0)):
            var.put('x', Js(4.0))
        if (var.get('level')>Js(9.0)):
            var.put('x', Js(5.0))
        while (var.get('x')>Js(0.0)):
            if (var.get('Math').callprop('random')<Js(0.66)):
                var.put('tempAr', Js([Js('Guidance'), Js('Sacred Flame'), Js('Spare the Dying')]))
            else:
                var.put('tempAr', var.get('clCantrip'))
            var.put('temp', var.get('tempAr').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tempAr').get('length')))))
            if ((var.get('myCantrips').callprop('indexOf', var.get('temp'))==(-Js(1.0))) and (var.get('raceSpells').callprop('indexOf', var.get('temp'))==(-Js(1.0)))):
                var.get('myCantrips').callprop('push', var.get('temp'))
                (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
        var.get('myCantrips').callprop('sort')
        var.put('tempSpells', Js([]))
        while 1:
            SWITCHED = False
            CONDITION = (var.get('clDomain'))
            if SWITCHED or PyJsStrictEq(CONDITION, Js(0.0)):
                SWITCHED = True
                var.get('doSpells').callprop('push', Js('Command'))
                var.get('doSpells').callprop('push', Js('Identify'))
                if (var.get('level')>Js(2.0)):
                    var.get('doSpells').callprop('push', Js('Augury'))
                    var.get('doSpells').callprop('push', Js('Suggestion'))
                if (var.get('level')>Js(4.0)):
                    var.get('doSpells').callprop('push', Js('Nondetection'))
                    var.get('doSpells').callprop('push', Js('Speak with Dead'))
                if (var.get('level')>Js(6.0)):
                    var.get('doSpells').callprop('push', Js('Arcane Eye'))
                    var.get('doSpells').callprop('push', Js('Confusion'))
                if (var.get('level')>Js(8.0)):
                    var.get('doSpells').callprop('push', Js('Legend Lore'))
                    var.get('doSpells').callprop('push', Js('Scrying'))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
                SWITCHED = True
                var.get('doSpells').callprop('push', Js('Bless'))
                var.get('doSpells').callprop('push', Js('Cure Wounds'))
                if (var.get('level')>Js(2.0)):
                    var.get('doSpells').callprop('push', Js('Lesser Restoration'))
                    var.get('doSpells').callprop('push', Js('Spiritual Weapon'))
                if (var.get('level')>Js(4.0)):
                    var.get('doSpells').callprop('push', Js('Beacon of Hope'))
                    var.get('doSpells').callprop('push', Js('Revivify'))
                if (var.get('level')>Js(6.0)):
                    var.get('doSpells').callprop('push', Js('Death Ward'))
                    var.get('doSpells').callprop('push', Js('Guardian of Faith'))
                if (var.get('level')>Js(8.0)):
                    var.get('doSpells').callprop('push', Js('Mass Cure Wounds'))
                    var.get('doSpells').callprop('push', Js('Raise Dead'))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                SWITCHED = True
                var.get('doSpells').callprop('push', Js('Burning Hands'))
                var.get('doSpells').callprop('push', Js('Faerie Fire'))
                if (var.get('level')>Js(2.0)):
                    var.get('doSpells').callprop('push', Js('Flaming Sphere'))
                    var.get('doSpells').callprop('push', Js('Scorching Ray'))
                if (var.get('level')>Js(4.0)):
                    var.get('doSpells').callprop('push', Js('Daylight'))
                    var.get('doSpells').callprop('push', Js('Fireball'))
                if (var.get('level')>Js(6.0)):
                    var.get('doSpells').callprop('push', Js('Guardian of Faith'))
                    var.get('doSpells').callprop('push', Js('Wall of Fire'))
                if (var.get('level')>Js(8.0)):
                    var.get('doSpells').callprop('push', Js('Flame Strike'))
                    var.get('doSpells').callprop('push', Js('Scrying'))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js(3.0)):
                SWITCHED = True
                var.get('doSpells').callprop('push', Js('Animal Friendship'))
                var.get('doSpells').callprop('push', Js('Speak with Animals'))
                if (var.get('level')>Js(2.0)):
                    var.get('doSpells').callprop('push', Js('Barkskin'))
                    var.get('doSpells').callprop('push', Js('Spike Growth'))
                if (var.get('level')>Js(4.0)):
                    var.get('doSpells').callprop('push', Js('Plant Growth'))
                    var.get('doSpells').callprop('push', Js('Wind Wall'))
                if (var.get('level')>Js(6.0)):
                    var.get('doSpells').callprop('push', Js('Dominate Beast'))
                    var.get('doSpells').callprop('push', Js('Grasping Vine'))
                if (var.get('level')>Js(8.0)):
                    var.get('doSpells').callprop('push', Js('Insect Plague'))
                    var.get('doSpells').callprop('push', Js('Tree Stride'))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js(4.0)):
                SWITCHED = True
                var.get('doSpells').callprop('push', Js('Fog Cloud'))
                var.get('doSpells').callprop('push', Js('Thunderwave'))
                if (var.get('level')>Js(2.0)):
                    var.get('doSpells').callprop('push', Js('Gust of Wind'))
                    var.get('doSpells').callprop('push', Js('Shatter'))
                if (var.get('level')>Js(4.0)):
                    var.get('doSpells').callprop('push', Js('Call Lightning'))
                    var.get('doSpells').callprop('push', Js('Sleet Storm'))
                if (var.get('level')>Js(6.0)):
                    var.get('doSpells').callprop('push', Js('Control Water'))
                    var.get('doSpells').callprop('push', Js('Ice Storm'))
                if (var.get('level')>Js(8.0)):
                    var.get('doSpells').callprop('push', Js('Destructive Wave'))
                    var.get('doSpells').callprop('push', Js('Insect Plague'))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js(5.0)):
                SWITCHED = True
                var.get('doSpells').callprop('push', Js('Charm Person'))
                var.get('doSpells').callprop('push', Js('Disguise Self'))
                if (var.get('level')>Js(2.0)):
                    var.get('doSpells').callprop('push', Js('Mirror Image'))
                    var.get('doSpells').callprop('push', Js('Pass without Trace'))
                if (var.get('level')>Js(4.0)):
                    var.get('doSpells').callprop('push', Js('Blink'))
                    var.get('doSpells').callprop('push', Js('Dispel Magic'))
                if (var.get('level')>Js(6.0)):
                    var.get('doSpells').callprop('push', Js('Dimension Door'))
                    var.get('doSpells').callprop('push', Js('Polymorph'))
                if (var.get('level')>Js(8.0)):
                    var.get('doSpells').callprop('push', Js('Dominate Person'))
                    var.get('doSpells').callprop('push', Js('Modify Memory'))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js(6.0)):
                SWITCHED = True
                var.get('doSpells').callprop('push', Js('Divine Favor'))
                var.get('doSpells').callprop('push', Js('Shield of Faith'))
                if (var.get('level')>Js(2.0)):
                    var.get('doSpells').callprop('push', Js('Magic Weapon'))
                    var.get('doSpells').callprop('push', Js('Spiritual Weapon'))
                if (var.get('level')>Js(4.0)):
                    var.get('doSpells').callprop('push', Js("Crusader's Mantle"))
                    var.get('doSpells').callprop('push', Js('Spirit Guardians'))
                if (var.get('level')>Js(6.0)):
                    var.get('doSpells').callprop('push', Js('Freedom of Movement'))
                    var.get('doSpells').callprop('push', Js('Stoneskin'))
                if (var.get('level')>Js(8.0)):
                    var.get('doSpells').callprop('push', Js('Flame Strike'))
                    var.get('doSpells').callprop('push', Js('Hold Monster'))
                break
            SWITCHED = True
            break
        var.put('x', var.get('sp1'))
        while (var.get('x')>Js(0.0)):
            var.put('tempAr', var.get('cl1'))
            if (var.get('Math').callprop('random')<Js(0.66)):
                var.put('tempAr', Js([Js('Bane'), Js('Bless'), Js('Command'), Js('Cure Wounds'), Js('Cure Wounds'), Js('Guiding Bolt'), Js('Guiding Bolt'), Js('Healing Word'), Js('Healing Word'), Js('Inflict Wounds'), Js('Shield of Faith')]))
            var.put('temp', var.get('tempAr').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tempAr').get('length')))))
            if ((var.get('tempSpells').callprop('indexOf', var.get('temp'))>(-Js(1.0))) or (var.get('doSpells').callprop('indexOf', var.get('temp'))>(-Js(1.0)))):
                pass
            else:
                var.get('tempSpells').callprop('push', var.get('temp'))
                (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
        var.get('tempSpells').callprop('sort')
        var.put('mySpells', var.get('mySpells').callprop('concat', var.get('tempSpells')))
        var.put('tempSpells', Js([]))
        var.put('x', var.get('sp2'))
        while (var.get('x')>Js(0.0)):
            var.put('tempAr', var.get('cl2'))
            if (var.get('Math').callprop('random')<Js(0.66)):
                var.put('tempAr', Js([Js('Aid'), Js('Blindness/Deafness'), Js('Enhance Ability'), Js('Hold Person'), Js('Lesser Restoration'), Js('Prayer of Healing'), Js('Silence'), Js('Spiritual Weapon'), Js('Warding Bond')]))
            var.put('temp', var.get('tempAr').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tempAr').get('length')))))
            if ((var.get('tempSpells').callprop('indexOf', var.get('temp'))>(-Js(1.0))) or (var.get('doSpells').callprop('indexOf', var.get('temp'))>(-Js(1.0)))):
                pass
            else:
                var.get('tempSpells').callprop('push', var.get('temp'))
                (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
        var.get('tempSpells').callprop('sort')
        var.put('mySpells', var.get('mySpells').callprop('concat', var.get('tempSpells')))
        var.put('tempSpells', Js([]))
        var.put('x', var.get('sp3'))
        while (var.get('x')>Js(0.0)):
            var.put('tempAr', var.get('cl3'))
            if (var.get('Math').callprop('random')<Js(0.66)):
                var.put('tempAr', Js([Js('Animate Dead'), Js('Beacon of Hope'), Js('Bestow Curse'), Js('Dispel Magic'), Js('Glyph of Warding'), Js('Magic Circle'), Js('Mass Healing Word'), Js('Mass Healing Word'), Js('Meld into Stone'), Js('Protection from Energy'), Js('Revivify'), Js('Spirit Guardians')]))
            var.put('temp', var.get('tempAr').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tempAr').get('length')))))
            if ((var.get('tempSpells').callprop('indexOf', var.get('temp'))==(-Js(1.0))) and (var.get('doSpells').callprop('indexOf', var.get('temp'))==(-Js(1.0)))):
                var.get('tempSpells').callprop('push', var.get('temp'))
                (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
        var.get('tempSpells').callprop('sort')
        var.put('mySpells', var.get('mySpells').callprop('concat', var.get('tempSpells')))
        var.put('tempSpells', Js([]))
        var.put('x', var.get('sp4'))
        while (var.get('x')>Js(0.0)):
            var.put('tempAr', var.get('cl4'))
            if (var.get('Math').callprop('random')<Js(0.5)):
                var.put('tempAr', Js([Js('Banishment'), Js('Control Water'), Js('Death Ward'), Js('Guardian of Faith'), Js('Stone Shape')]))
            var.put('temp', var.get('tempAr').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tempAr').get('length')))))
            if ((var.get('tempSpells').callprop('indexOf', var.get('temp'))==(-Js(1.0))) and (var.get('doSpells').callprop('indexOf', var.get('temp'))==(-Js(1.0)))):
                var.get('tempSpells').callprop('push', var.get('temp'))
                (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
        var.get('tempSpells').callprop('sort')
        var.put('mySpells', var.get('mySpells').callprop('concat', var.get('tempSpells')))
        var.put('tempSpells', Js([]))
        var.put('x', var.get('sp5'))
        while (var.get('x')>Js(0.0)):
            var.put('tempAr', var.get('cl5'))
            if (var.get('Math').callprop('random')<Js(0.5)):
                var.put('tempAr', Js([Js('Commune'), Js('Contagion'), Js('Dispel Evil and Good'), Js('Flame Strike'), Js('Geas'), Js('Greater Restoration'), Js('Hallow'), Js('Insect Plague'), Js('Legend Lore'), Js('Mass Cure Wounds'), Js('Mass Cure Wounds'), Js('Planar Binding'), Js('Raise Dead')]))
            var.put('temp', var.get('tempAr').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tempAr').get('length')))))
            if ((var.get('tempSpells').callprop('indexOf', var.get('temp'))==(-Js(1.0))) and (var.get('doSpells').callprop('indexOf', var.get('temp'))==(-Js(1.0)))):
                var.get('tempSpells').callprop('push', var.get('temp'))
                (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
        var.get('tempSpells').callprop('sort')
        var.put('mySpells', var.get('mySpells').callprop('concat', var.get('tempSpells')))
    if (var.get('cl')==Js(4.0)):
        var.put('ss1', (var.get('level')+Js(1.0)))
        var.put('ss2', Js(0.0))
        if (var.get('level')>Js(2.0)):
            var.put('ss2', Js(2.0))
        if (var.get('level')>Js(3.0)):
            var.put('ss1', Js(4.0))
            var.put('ss2', Js(3.0))
        if (var.get('level')==Js(5.0)):
            var.put('ss3', Js(2.0))
        if (var.get('level')>Js(5.0)):
            var.put('ss3', Js(3.0))
        if (var.get('level')>Js(6.0)):
            var.put('ss4', (var.get('level')-Js(6.0)))
        if (var.get('level')>Js(8.0)):
            var.put('ss4', Js(3.0))
            var.put('ss5', (var.get('level')-Js(8.0)))
        var.put('sp', (var.get('level')+var.get('mod').get('4')))
        var.put('sp3', Js(0.0))
        var.put('sp4', Js(0.0))
        var.put('sp5', Js(0.0))
        if (var.get('level')<Js(3.0)):
            var.put('sp1', var.get('sp'))
            var.put('sp2', Js(0.0))
        else:
            if (var.get('level')<Js(5.0)):
                var.put('x', var.get('Math').callprop('floor', (var.get('sp')*Js(0.7))))
                var.put('sp1', var.get('x'))
                var.put('sp2', (var.get('sp')-var.get('x')))
            else:
                if (var.get('level')<Js(7.0)):
                    var.put('x', var.get('Math').callprop('ceil', (var.get('sp')*Js(0.35))))
                    var.put('y', var.get('Math').callprop('floor', (var.get('sp')*Js(0.35))))
                    var.put('sp1', var.get('x'))
                    var.put('z', ((var.get('sp')-var.get('x'))-var.get('y')))
                    var.put('sp2', var.get('y'))
                    var.put('sp3', var.get('z'))
                else:
                    if (var.get('level')<Js(9.0)):
                        var.put('x', var.get('Math').callprop('floor', (var.get('sp')*Js(0.28))))
                        var.put('y', var.get('Math').callprop('floor', (var.get('sp')*Js(0.28))))
                        var.put('z', var.get('Math').callprop('floor', (var.get('sp')*Js(0.28))))
                        var.put('sum', (((var.get('sp')-var.get('x'))-var.get('y'))-var.get('z')))
                        var.put('sp1', var.get('sum'))
                        var.put('sp2', var.get('y'))
                        var.put('sp3', var.get('z'))
                        var.put('sp4', var.get('x'))
                    else:
                        if (var.get('level')>Js(8.0)):
                            var.put('x', var.get('Math').callprop('floor', (var.get('sp')*Js(0.21))))
                            var.put('y', var.get('Math').callprop('ceil', (var.get('sp')*Js(0.18))))
                            var.put('z', var.get('Math').callprop('ceil', (var.get('sp')*Js(0.18))))
                            var.put('xx', var.get('Math').callprop('floor', (var.get('sp')*Js(0.21))))
                            var.put('sum', ((((var.get('sp')-var.get('x'))-var.get('y'))-var.get('z'))-var.get('xx')))
                            var.put('sp1', var.get('sum'))
                            var.put('sp2', var.get('y'))
                            var.put('sp3', var.get('z'))
                            var.put('sp4', var.get('xx'))
                            var.put('sp5', var.get('x'))
        var.get('console').callprop('log', (((((((((((Js('Spells known:  ')+var.get('sp1'))+Js('/ '))+var.get('sp2'))+Js('/ '))+var.get('sp3'))+Js('/ '))+var.get('sp4'))+Js('/ '))+var.get('sp5'))+Js(' / Total = '))+var.get('sp')))
        var.put('x', Js(2.0))
        if (var.get('level')>Js(3.0)):
            var.put('x', Js(3.0))
        if (var.get('level')>Js(9.0)):
            var.put('x', Js(4.0))
        if (var.get('drCircle')==Js(0.0)):
            (var.put('x',Js(var.get('x').to_number())+Js(1))-Js(1))
        while (var.get('x')>Js(0.0)):
            var.put('tempAr', var.get('drCantrip'))
            if (var.get('Math').callprop('random')<Js(0.66)):
                var.put('tempAr', Js([Js('Guidance'), Js('Poison Spray'), Js('Resistance'), Js('Shillelagh'), Js('Thorn Whip')]))
            var.put('temp', var.get('tempAr').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tempAr').get('length')))))
            if ((var.get('myCantrips').callprop('indexOf', var.get('temp'))==(-Js(1.0))) and (var.get('raceSpells').callprop('indexOf', var.get('temp'))==(-Js(1.0)))):
                var.get('myCantrips').callprop('push', var.get('temp'))
                (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
        var.get('myCantrips').callprop('sort')
        var.put('tempSpells', Js([]))
        var.put('x', var.get('sp1'))
        while (var.get('x')>Js(0.0)):
            var.put('tempAr', var.get('dr1'))
            if (var.get('Math').callprop('random')<Js(0.66)):
                var.put('tempAr', Js([Js('Charm Person'), Js('Cure Wounds'), Js('Cure Wounds'), Js('Cure Wounds'), Js('Entangle'), Js('Fog Cloud'), Js('Healing Word'), Js('Healing Word'), Js('Thunderwave'), Js('Thunderwave')]))
            var.put('temp', var.get('tempAr').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tempAr').get('length')))))
            if ((var.get('tempSpells').callprop('indexOf', var.get('temp'))==(-Js(1.0))) and (var.get('ciSpells').callprop('indexOf', var.get('temp'))==(-Js(1.0)))):
                var.get('tempSpells').callprop('push', var.get('temp'))
                (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
        var.get('tempSpells').callprop('sort')
        var.put('mySpells', var.get('mySpells').callprop('concat', var.get('tempSpells')))
        var.put('tempSpells', Js([]))
        var.put('x', var.get('sp2'))
        while (var.get('x')>Js(0.0)):
            var.put('tempAr', var.get('dr2'))
            if (var.get('Math').callprop('random')<Js(0.66)):
                var.put('tempAr', Js([Js('Barkskin'), Js('Barkskin'), Js('Barkskin'), Js('Enhance Ability'), Js('Flame Blade'), Js('Flaming Sphere'), Js('Heat Metal'), Js('Heat Metal'), Js('Hold Person'), Js('Lesser Restoration'), Js('Moonbeam'), Js('Pass without Trace'), Js('Spike Growth')]))
            var.put('temp', var.get('tempAr').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tempAr').get('length')))))
            if ((var.get('tempSpells').callprop('indexOf', var.get('temp'))==(-Js(1.0))) and (var.get('ciSpells').callprop('indexOf', var.get('temp'))==(-Js(1.0)))):
                var.get('tempSpells').callprop('push', var.get('temp'))
                (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
        var.get('tempSpells').callprop('sort')
        var.put('mySpells', var.get('mySpells').callprop('concat', var.get('tempSpells')))
        var.put('tempSpells', Js([]))
        var.put('x', var.get('sp3'))
        while (var.get('x')>Js(0.0)):
            var.put('tempAr', var.get('dr3'))
            if (var.get('Math').callprop('random')<Js(0.66)):
                var.put('tempAr', Js([Js('Call Lightning'), Js('Conjure Animals'), Js('Dispel Magic'), Js('Meld into Stone'), Js('Protection from Energy'), Js('Sleet Storm'), Js('Speak with Plants'), Js('Wind Wall')]))
            var.put('temp', var.get('tempAr').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tempAr').get('length')))))
            if ((var.get('tempSpells').callprop('indexOf', var.get('temp'))==(-Js(1.0))) and (var.get('ciSpells').callprop('indexOf', var.get('temp'))==(-Js(1.0)))):
                var.get('tempSpells').callprop('push', var.get('temp'))
                (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
        var.get('tempSpells').callprop('sort')
        var.put('mySpells', var.get('mySpells').callprop('concat', var.get('tempSpells')))
        var.put('tempSpells', Js([]))
        var.put('x', var.get('sp4'))
        while (var.get('x')>Js(0.0)):
            var.put('tempAr', var.get('dr4'))
            if (var.get('Math').callprop('random')<Js(0.5)):
                var.put('tempAr', Js([Js('Blight'), Js('Confusion'), Js('Conjure Minor Elementals'), Js('Conjure Woodland Beings'), Js('Control Water'), Js('Dominate Beast'), Js('Giant Insect'), Js('Grasping Vine'), Js('Ice Storm'), Js('Locate Creature'), Js('Polymorph'), Js('Stone Shape'), Js('Stoneskin'), Js('Wall of Fire')]))
            var.put('temp', var.get('tempAr').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tempAr').get('length')))))
            if ((var.get('tempSpells').callprop('indexOf', var.get('temp'))==(-Js(1.0))) and (var.get('ciSpells').callprop('indexOf', var.get('temp'))==(-Js(1.0)))):
                var.get('tempSpells').callprop('push', var.get('temp'))
                (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
        var.get('tempSpells').callprop('sort')
        var.put('mySpells', var.get('mySpells').callprop('concat', var.get('tempSpells')))
        var.put('tempSpells', Js([]))
        var.put('x', var.get('sp5'))
        while (var.get('x')>Js(0.0)):
            var.put('tempAr', var.get('dr5'))
            if (var.get('Math').callprop('random')<Js(0.5)):
                var.put('tempAr', Js([Js('Antilife Shell'), Js('Commune with Nature'), Js('Conjure Elemental'), Js('Contagion'), Js('Geas'), Js('Greater Restoration'), Js('Insect Plague'), Js('Mass Cure Wounds'), Js('Mass Cure Wounds'), Js('Planar Binding'), Js('Reincarnate'), Js('Tree Stride'), Js('Wall of Stone')]))
            var.put('temp', var.get('tempAr').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tempAr').get('length')))))
            if ((var.get('tempSpells').callprop('indexOf', var.get('temp'))==(-Js(1.0))) and (var.get('ciSpells').callprop('indexOf', var.get('temp'))==(-Js(1.0)))):
                var.get('tempSpells').callprop('push', var.get('temp'))
                (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
        var.get('tempSpells').callprop('sort')
        var.put('mySpells', var.get('mySpells').callprop('concat', var.get('tempSpells')))
    if (var.get('cl')==Js(5.0)):
        var.put('ss1', Js(0.0))
        var.put('ss2', Js(0.0))
        if (var.get('level')==Js(3.0)):
            var.put('ss1', Js(2.0))
        if (var.get('level')>Js(3.0)):
            var.put('ss1', Js(3.0))
        if (var.get('level')>Js(6.0)):
            var.put('ss1', Js(4.0))
            var.put('ss2', Js(2.0))
        if (var.get('level')>Js(9.0)):
            var.put('ss2', Js(3.0))
        var.put('sp1', Js(0.0))
        var.put('sp2', Js(0.0))
        var.put('sp', Js(0.0))
        if (var.get('level')==Js(3.0)):
            var.put('sp', Js(3.0))
        if (var.get('level')>Js(3.0)):
            var.put('sp', Js(4.0))
        if (var.get('level')==Js(7.0)):
            var.put('sp', Js(5.0))
        if (var.get('level')>Js(7.0)):
            var.put('sp', Js(6.0))
        if (var.get('level')==Js(10.0)):
            var.put('sp', Js(7.0))
        if (var.get('level')==Js(7.0)):
            var.put('sp2', Js(1.0))
        if (var.get('level')>Js(7.0)):
            var.put('sp2', Js(2.0))
        if (var.get('level')>Js(9.0)):
            var.put('sp2', Js(3.0))
        var.put('sp1', (var.get('sp')-var.get('sp2')))
        var.get('console').callprop('log', ((((var.get('sp')+Js('/'))+var.get('sp1'))+Js('/'))+var.get('sp2')))
        var.put('x', Js(0.0))
        if (var.get('level')>Js(2.0)):
            var.put('x', Js(2.0))
        if (var.get('level')>Js(9.0)):
            var.put('x', Js(3.0))
        while (var.get('x')>Js(0.0)):
            if (var.get('Math').callprop('random')<Js(0.5)):
                var.put('tempAr', Js([Js('Acid Splash'), Js('Blade Ward'), Js('Chill Touch'), Js('Fire Bolt'), Js('Minor Illusion'), Js('Poison Spray'), Js('Ray of Frost'), Js('Shocking Grasp'), Js('True Strike')]))
            else:
                var.put('tempAr', var.get('wiCantrip'))
            var.put('temp', var.get('tempAr').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tempAr').get('length')))))
            if ((var.get('myCantrips').callprop('indexOf', var.get('temp'))==(-Js(1.0))) and (var.get('raceSpells').callprop('indexOf', var.get('temp'))==(-Js(1.0)))):
                var.get('myCantrips').callprop('push', var.get('temp'))
                (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
        var.get('myCantrips').callprop('sort')
        var.put('x', var.get('sp1'))
        if (var.get('x')>Js(0.0)):
            var.put('tempAr', var.get('wi1'))
            if (var.get('Math').callprop('random')<Js(0.66)):
                var.put('tempAr', Js([Js('Color Spray'), Js('False Life'), Js('Magic Missile'), Js('Ray of Sickness'), Js('Sleep'), Js("Tasha's Hideous Laughter"), Js('Thunderwave')]))
            else:
                var.put('tempAr', var.get('wi1'))
            var.put('temp', var.get('tempAr').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tempAr').get('length')))))
            var.get('tempSpells').callprop('push', var.get('temp'))
            (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
        var.put('tempAr', Js([Js(0.0), Js(1.0), Js(1.0), Js(3.0), Js(18.0), Js(19.0), Js(20.0), Js(22.0), Js(27.0), Js(27.0), Js(29.0)]))
        while (var.get('x')>Js(0.0)):
            var.put('i', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tempAr').get('length'))))
            var.put('temp', var.get('wi1').get(var.get('tempAr').get(var.get('i'))))
            if (var.get('tempSpells').callprop('indexOf', var.get('temp'))>(-Js(1.0))):
                pass
            else:
                var.get('tempSpells').callprop('push', var.get('temp'))
                (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
        var.get('tempSpells').callprop('sort')
        var.put('mySpells', var.get('mySpells').callprop('concat', var.get('tempSpells')))
        var.put('tempSpells', Js([]))
        var.put('x', var.get('sp2'))
        if (var.get('level')>Js(7.0)):
            if (var.get('x')>Js(0.0)):
                var.put('tempAr', var.get('wi1'))
                if (var.get('Math').callprop('random')<Js(0.66)):
                    var.put('tempAr', Js([Js('Blindness/Deafness'), Js('Blur'), Js('Cloud of Daggers'), Js('Crown of Madness'), Js('Flaming Sphere'), Js('Hold Person'), Js('Invisibility'), Js('Mirror Image'), Js('Phantasmal Force'), Js('Ray of Enfeeblement'), Js('Scorching Ray'), Js('Suggestion'), Js('Web')]))
                else:
                    var.put('tempAr', var.get('wi2'))
                var.put('temp', var.get('tempAr').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tempAr').get('length')))))
                var.get('tempSpells').callprop('push', var.get('temp'))
                (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
        var.put('tempAr', Js([Js(5.0), Js(7.0), Js(13.0), Js(21.0), Js(28.0), Js(30.0), Js(1.0)]))
        while (var.get('x')>Js(0.0)):
            var.put('i', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tempAr').get('length'))))
            var.put('temp', var.get('wi2').get(var.get('tempAr').get(var.get('i'))))
            if (var.get('tempSpells').callprop('indexOf', var.get('temp'))==(-Js(1.0))):
                var.get('tempSpells').callprop('push', var.get('temp'))
                (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
        var.get('tempSpells').callprop('sort')
        var.put('mySpells', var.get('mySpells').callprop('concat', var.get('tempSpells')))
    if (var.get('cl')==Js(9.0)):
        var.put('ss2', Js(0.0))
        var.put('ss3', Js(0.0))
        var.put('ss1', Js(0.0))
        if (var.get('level')==Js(2.0)):
            var.put('ss1', Js(2.0))
        if (var.get('level')>Js(2.0)):
            var.put('ss1', Js(3.0))
        if (var.get('level')>Js(4.0)):
            var.put('ss1', Js(4.0))
            var.put('ss2', Js(2.0))
        if (var.get('level')>Js(6.0)):
            var.put('ss2', Js(3.0))
        if (var.get('level')>Js(8.0)):
            var.put('ss3', Js(2.0))
        var.put('sp', (var.get('mod').get('5')+var.get('Math').callprop('floor', (var.get('level')/Js(2.0)))))
        if (var.get('sp')<Js(1.0)):
            var.put('sp', Js(1.0))
        if (var.get('level')<Js(5.0)):
            var.put('sp1', var.get('sp'))
            var.put('sp2', Js(0.0))
        else:
            if (var.get('level')<Js(9.0)):
                var.put('sp1', var.get('Math').callprop('ceil', (var.get('sp')/Js(2.0))))
                var.put('sp2', (var.get('sp')-var.get('sp1')))
            else:
                var.put('sp1', var.get('Math').callprop('ceil', (var.get('sp')*Js(0.35))))
                var.put('sp2', var.get('Math').callprop('floor', (var.get('sp')*Js(0.35))))
                var.put('sp3', ((var.get('sp')-var.get('sp1'))-var.get('sp2')))
        var.get('console').callprop('log', ((((((var.get('sp')+Js('/'))+var.get('sp1'))+Js('/'))+var.get('sp2'))+Js('/'))+var.get('sp3')))
        var.put('tempSpells', Js([]))
        var.put('x', var.get('sp1'))
        while (var.get('x')>Js(0.0)):
            var.put('tempAr', var.get('pa1'))
            if (var.get('Math').callprop('random')<Js(0.66)):
                var.put('tempAr', Js([Js('Command'), Js('Cure Wounds'), Js('Cure Wounds'), Js('Heroism'), Js('Searing Smite'), Js('Shield of Faith'), Js('Thunderous Smite'), Js('Thunderous Smite'), Js('Wrathful Smite')]))
            var.put('temp', var.get('tempAr').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tempAr').get('length')))))
            if ((var.get('tempSpells').callprop('indexOf', var.get('temp'))==(-Js(1.0))) and (var.get('oaSpells').callprop('indexOf', var.get('temp'))==(-Js(1.0)))):
                var.get('tempSpells').callprop('push', var.get('temp'))
                (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
        var.get('tempSpells').callprop('sort')
        var.put('mySpells', var.get('mySpells').callprop('concat', var.get('tempSpells')))
        var.put('tempSpells', Js([]))
        var.put('x', var.get('sp2'))
        while (var.get('x')>Js(0.0)):
            var.put('tempAr', var.get('pa2'))
            var.put('temp', var.get('tempAr').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tempAr').get('length')))))
            if ((var.get('tempSpells').callprop('indexOf', var.get('temp'))==(-Js(1.0))) and (var.get('oaSpells').callprop('indexOf', var.get('temp'))==(-Js(1.0)))):
                var.get('tempSpells').callprop('push', var.get('temp'))
                (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
        var.get('tempSpells').callprop('sort')
        var.put('mySpells', var.get('mySpells').callprop('concat', var.get('tempSpells')))
        var.put('tempSpells', Js([]))
        var.put('x', var.get('sp3'))
        while (var.get('x')>Js(0.0)):
            var.put('tempAr', var.get('pa3'))
            if (var.get('Math').callprop('random')<Js(0.66)):
                var.put('tempAr', Js([Js('Aura of Vitality'), Js('Aura of Vitality'), Js('Blinding Smite'), Js('Blinding Smite'), Js("Crusader's Mantle"), Js('Dispel Magic'), Js('Elemental Weapon')]))
            var.put('temp', var.get('tempAr').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tempAr').get('length')))))
            if ((var.get('tempSpells').callprop('indexOf', var.get('temp'))==(-Js(1.0))) and (var.get('oaSpells').callprop('indexOf', var.get('temp'))==(-Js(1.0)))):
                var.get('tempSpells').callprop('push', var.get('temp'))
                (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
        var.get('tempSpells').callprop('sort')
        var.put('mySpells', var.get('mySpells').callprop('concat', var.get('tempSpells')))
    if (var.get('cl')==Js(10.0)):
        if (var.get('level')==Js(2.0)):
            var.put('ss1', Js(2.0))
        if (var.get('level')>Js(2.0)):
            var.put('ss1', Js(3.0))
        if (var.get('level')>Js(4.0)):
            var.put('ss1', Js(4.0))
            var.put('ss2', Js(2.0))
        if (var.get('level')>Js(6.0)):
            var.put('ss2', Js(3.0))
        if (var.get('level')>Js(8.0)):
            var.put('ss3', Js(2.0))
        var.put('sp', (var.get('Math').callprop('ceil', (var.get('level')/Js(2.0)))+Js(1.0)))
        if (var.get('level')==Js(1.0)):
            var.put('sp', Js(0.0))
        if (var.get('level')<Js(5.0)):
            var.put('sp1', var.get('sp'))
            var.put('sp2', Js(0.0))
            var.put('sp3', Js(0.0))
        else:
            if (var.get('level')<Js(9.0)):
                var.put('sp1', var.get('Math').callprop('ceil', (var.get('sp')/Js(2.0))))
                var.put('sp2', (var.get('sp')-var.get('sp1')))
                var.put('sp3', Js(0.0))
            else:
                var.put('sp1', var.get('Math').callprop('ceil', (var.get('sp')*Js(0.35))))
                var.put('sp2', var.get('Math').callprop('floor', (var.get('sp')*Js(0.35))))
                var.put('sp3', ((var.get('sp')-var.get('sp1'))-var.get('sp2')))
        var.get('console').callprop('log', ((((((var.get('sp')+Js('/'))+var.get('sp1'))+Js('/'))+var.get('sp2'))+Js('/'))+var.get('sp3')))
        var.put('x', Js(0.0))
        var.put('x', var.get('sp1'))
        var.put('tempSpells', Js([]))
        while (var.get('x')>Js(0.0)):
            var.put('tempAr', var.get('ra1'))
            if (var.get('Math').callprop('random')<Js(0.66)):
                var.put('tempAr', Js([Js('Cure Wounds'), Js('Cure Wounds'), Js('Ensnaring Strike'), Js('Hail of Thorns'), Js("Hunter's Mark")]))
            var.put('temp', var.get('tempAr').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tempAr').get('length')))))
            if (var.get('tempSpells').callprop('indexOf', var.get('temp'))==(-Js(1.0))):
                var.get('tempSpells').callprop('push', var.get('temp'))
                (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
        var.get('tempSpells').callprop('sort')
        var.put('mySpells', var.get('mySpells').callprop('concat', var.get('tempSpells')))
        var.put('tempSpells', Js([]))
        var.put('x', Js(0.0))
        var.put('x', var.get('sp2'))
        while (var.get('x')>Js(0.0)):
            var.put('tempAr', var.get('ra2'))
            if (var.get('Math').callprop('random')<Js(0.66)):
                var.put('tempAr', Js([Js('Cordon of Arrows'), Js('Cordon of Arrows'), Js('Find Traps'), Js('Pass without Trace'), Js('Protection from Poison'), Js('Silence'), Js('Spike Growth')]))
            var.put('temp', var.get('tempAr').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tempAr').get('length')))))
            if ((var.get('tempSpells').callprop('indexOf', var.get('temp'))==(-Js(1.0))) and (var.get('oaSpells').callprop('indexOf', var.get('temp'))==(-Js(1.0)))):
                var.get('tempSpells').callprop('push', var.get('temp'))
                (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
        var.get('tempSpells').callprop('sort')
        var.put('mySpells', var.get('mySpells').callprop('concat', var.get('tempSpells')))
        var.put('tempSpells', Js([]))
        var.put('x', Js(0.0))
        var.put('x', var.get('sp3'))
        while (var.get('x')>Js(0.0)):
            var.put('tempAr', var.get('ra3'))
            if (var.get('Math').callprop('random')<Js(0.66)):
                var.put('tempAr', Js([Js('Conjure Animals'), Js('Conjure Barrage'), Js('Lightning Arrow'), Js('Protection from Energy'), Js('Wind Wall')]))
            var.put('temp', var.get('tempAr').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tempAr').get('length')))))
            if ((var.get('tempSpells').callprop('indexOf', var.get('temp'))==(-Js(1.0))) and (var.get('oaSpells').callprop('indexOf', var.get('temp'))==(-Js(1.0)))):
                var.get('tempSpells').callprop('push', var.get('temp'))
                (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
        var.get('tempSpells').callprop('sort')
        var.put('mySpells', var.get('mySpells').callprop('concat', var.get('tempSpells')))
    if (var.get('cl')==Js(12.0)):
        var.put('ss1', Js(0.0))
        var.put('ss2', Js(0.0))
        if (var.get('level')==Js(3.0)):
            var.put('ss1', Js(2.0))
        if (var.get('level')>Js(3.0)):
            var.put('ss1', Js(3.0))
        if (var.get('level')>Js(6.0)):
            var.put('ss1', Js(4.0))
            var.put('ss2', Js(2.0))
        if (var.get('level')>Js(9.0)):
            var.put('ss2', Js(3.0))
        var.put('sp1', Js(0.0))
        var.put('sp2', Js(0.0))
        var.put('sp', Js(0.0))
        if (var.get('level')==Js(3.0)):
            var.put('sp', Js(3.0))
        if (var.get('level')>Js(3.0)):
            var.put('sp', Js(4.0))
        if (var.get('level')==Js(7.0)):
            var.put('sp', Js(5.0))
        if (var.get('level')>Js(7.0)):
            var.put('sp', Js(6.0))
        if (var.get('level')==Js(10.0)):
            var.put('sp', Js(7.0))
        if (var.get('level')>Js(6.0)):
            var.put('sp2', Js(2.0))
        if (var.get('level')>Js(9.0)):
            var.put('sp2', Js(3.0))
        var.put('sp1', (var.get('sp')-var.get('sp2')))
        var.get('console').callprop('log', ((((var.get('sp')+Js('/'))+var.get('sp1'))+Js('/'))+var.get('sp2')))
        var.put('x', Js(0.0))
        if (var.get('level')>Js(2.0)):
            var.put('x', Js(2.0))
            var.get('myCantrips').callprop('push', var.get('wiCantrip').get('7'))
        if (var.get('level')>Js(9.0)):
            var.put('x', Js(3.0))
        while (var.get('x')>Js(0.0)):
            if (var.get('Math').callprop('random')<Js(0.5)):
                var.put('tempAr', Js([Js('Acid Splash'), Js('Blade Ward'), Js('Chill Touch'), Js('Fire Bolt'), Js('Minor Illusion'), Js('Poison Spray'), Js('Ray of Frost'), Js('Shocking Grasp'), Js('True Strike')]))
            else:
                var.put('tempAr', var.get('wiCantrip'))
            var.put('temp', var.get('tempAr').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tempAr').get('length')))))
            if ((var.get('myCantrips').callprop('indexOf', var.get('temp'))==(-Js(1.0))) and (var.get('raceSpells').callprop('indexOf', var.get('temp'))==(-Js(1.0)))):
                var.get('myCantrips').callprop('push', var.get('temp'))
                (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
        var.get('myCantrips').callprop('sort')
        var.put('x', var.get('sp1'))
        if (var.get('x')>Js(0.0)):
            var.put('tempAr', var.get('wi1'))
            if (var.get('Math').callprop('random')<Js(0.66)):
                var.put('tempAr', Js([Js('Burning Hands'), Js('Burning Hands'), Js('Chromatic Orb'), Js('False Life'), Js('Mage Armor'), Js('Magic Missile'), Js('Magic Missile'), Js('Ray of Sickness'), Js('Shield'), Js('Sleep'), Js("Tasha's Hideous Laughter"), Js("Tasha's Hideous Laughter"), Js('Thunderwave'), Js('Thunderwave'), Js('Thunderwave'), Js('Witch Bolt')]))
            var.put('temp', var.get('tempAr').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tempAr').get('length')))))
            var.get('tempSpells').callprop('push', var.get('temp'))
            (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
        var.put('tempAr', Js([Js(4.0), Js(7.0), Js(15.0), Js(23.0), Js(24.0), Js(25.0)]))
        while (var.get('x')>Js(0.0)):
            var.put('i', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tempAr').get('length'))))
            var.put('temp', var.get('wi1').get(var.get('tempAr').get(var.get('i'))))
            if (var.get('tempSpells').callprop('indexOf', var.get('temp'))>(-Js(1.0))):
                pass
            else:
                var.get('tempSpells').callprop('push', var.get('temp'))
                (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
        var.get('tempSpells').callprop('sort')
        var.put('mySpells', var.get('mySpells').callprop('concat', var.get('tempSpells')))
        var.put('tempSpells', Js([]))
        var.put('x', var.get('sp2'))
        if (var.get('level')>Js(7.0)):
            if (var.get('x')>Js(0.0)):
                var.put('tempAr', var.get('wi2'))
                if (var.get('Math').callprop('random')<Js(0.66)):
                    var.put('tempAr', Js([Js('Blindness/Deafness'), Js('Cloud of Daggers'), Js('Flaming Sphere'), Js('Invisibility'), Js("Melf's Acid Arrow"), Js('Ray of Enfeeblement'), Js('Scorching Ray'), Js('Shatter'), Js('Web')]))
                var.put('temp', var.get('tempAr').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tempAr').get('length')))))
                var.get('tempSpells').callprop('push', var.get('temp'))
                (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
        var.put('tempAr', Js([Js(3.0), Js(15.0), Js(15.0), Js(15.0), Js(22.0), Js(24.0), Js(25.0), Js(19.0), Js(6.0), Js(14.0), Js(32.0), Js(32.0)]))
        while (var.get('x')>Js(0.0)):
            var.put('i', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tempAr').get('length'))))
            var.put('temp', var.get('wi2').get(var.get('tempAr').get(var.get('i'))))
            if (var.get('tempSpells').callprop('indexOf', var.get('temp'))==(-Js(1.0))):
                var.get('tempSpells').callprop('push', var.get('temp'))
                (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
        var.get('tempSpells').callprop('sort')
        var.put('mySpells', var.get('mySpells').callprop('concat', var.get('tempSpells')))
    if (var.get('cl')==Js(13.0)):
        var.put('ss1', (var.get('level')+Js(1.0)))
        var.put('ss2', Js(0.0))
        if (var.get('level')>Js(2.0)):
            var.put('ss2', Js(2.0))
        if (var.get('level')>Js(3.0)):
            var.put('ss1', Js(4.0))
            var.put('ss2', Js(3.0))
        if (var.get('level')==Js(5.0)):
            var.put('ss3', Js(2.0))
        if (var.get('level')>Js(5.0)):
            var.put('ss3', Js(3.0))
        if (var.get('level')>Js(6.0)):
            var.put('ss4', (var.get('level')-Js(6.0)))
        if (var.get('level')>Js(8.0)):
            var.put('ss4', Js(3.0))
            var.put('ss5', (var.get('level')-Js(8.0)))
        var.put('sp', (var.get('level')+Js(1.0)))
        var.put('sp3', Js(0.0))
        var.put('sp4', Js(0.0))
        var.put('sp5', Js(0.0))
        if (var.get('level')<Js(3.0)):
            var.put('sp1', var.get('sp'))
            var.put('sp2', Js(0.0))
        else:
            if (var.get('level')<Js(5.0)):
                var.put('x', var.get('Math').callprop('floor', (var.get('sp')*Js(0.7))))
                var.put('sp1', var.get('x'))
                var.put('sp2', (var.get('sp')-var.get('x')))
            else:
                if (var.get('level')<Js(7.0)):
                    var.put('x', var.get('Math').callprop('ceil', (var.get('sp')*Js(0.35))))
                    var.put('y', var.get('Math').callprop('floor', (var.get('sp')*Js(0.35))))
                    var.put('sp1', var.get('x'))
                    var.put('z', ((var.get('sp')-var.get('x'))-var.get('y')))
                    var.put('sp2', var.get('y'))
                    var.put('sp3', var.get('z'))
                else:
                    if (var.get('level')<Js(9.0)):
                        var.put('x', var.get('Math').callprop('floor', (var.get('sp')*Js(0.28))))
                        var.put('y', var.get('Math').callprop('floor', (var.get('sp')*Js(0.28))))
                        var.put('z', var.get('Math').callprop('floor', (var.get('sp')*Js(0.28))))
                        var.put('sum', (((var.get('sp')-var.get('x'))-var.get('y'))-var.get('z')))
                        var.put('sp1', var.get('sum'))
                        var.put('sp2', var.get('y'))
                        var.put('sp3', var.get('z'))
                        var.put('sp4', var.get('x'))
                    else:
                        if (var.get('level')>Js(8.0)):
                            var.put('x', var.get('Math').callprop('floor', (var.get('sp')*Js(0.21))))
                            var.put('y', var.get('Math').callprop('ceil', (var.get('sp')*Js(0.18))))
                            var.put('z', var.get('Math').callprop('ceil', (var.get('sp')*Js(0.18))))
                            var.put('xx', var.get('Math').callprop('floor', (var.get('sp')*Js(0.21))))
                            var.put('sum', ((((var.get('sp')-var.get('x'))-var.get('y'))-var.get('z'))-var.get('xx')))
                            var.put('sp1', var.get('sum'))
                            var.put('sp2', var.get('y'))
                            var.put('sp3', var.get('z'))
                            var.put('sp4', var.get('xx'))
                            var.put('sp5', var.get('x'))
        var.get('console').callprop('log', (((((((((((Js('Spells known:  ')+var.get('sp1'))+Js('/ '))+var.get('sp2'))+Js('/ '))+var.get('sp3'))+Js('/ '))+var.get('sp4'))+Js('/ '))+var.get('sp5'))+Js(' / Total = '))+var.get('sp')))
        var.put('x', Js(4.0))
        if (var.get('level')>Js(3.0)):
            var.put('x', Js(5.0))
        if (var.get('level')>Js(9.0)):
            var.put('x', Js(6.0))
        while (var.get('x')>Js(0.0)):
            var.put('tempAr', var.get('soCantrip'))
            if (var.get('Math').callprop('random')<Js(0.66)):
                var.put('tempAr', Js([Js('Acid Splash'), Js('Blade Ward'), Js('Chill Touch'), Js('Fire Bolt'), Js('Minor Illusion'), Js('Poison Spray'), Js('Ray of Frost'), Js('Shocking Grasp'), Js('True Strike')]))
            var.put('temp', var.get('tempAr').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tempAr').get('length')))))
            if ((var.get('myCantrips').callprop('indexOf', var.get('temp'))==(-Js(1.0))) and (var.get('raceSpells').callprop('indexOf', var.get('temp'))==(-Js(1.0)))):
                var.get('myCantrips').callprop('push', var.get('temp'))
                (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
        var.get('myCantrips').callprop('sort')
        var.put('tempSpells', Js([]))
        var.put('x', var.get('sp1'))
        var.put('tempSpells', Js([]))
        while (var.get('x')>Js(0.0)):
            var.put('tempAr', var.get('so1'))
            if (var.get('Math').callprop('random')<Js(0.66)):
                var.put('tempAr', Js([Js('Burning Hands'), Js('Charm Person'), Js('Chromatic Orb'), Js('Color Spray'), Js('False Life'), Js('Mage Armor'), Js('Magic Missile'), Js('Ray of Sickness'), Js('Shield'), Js('Sleep'), Js('Thunderwave'), Js('Witch Bolt')]))
            var.put('temp', var.get('tempAr').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tempAr').get('length')))))
            if (var.get('tempSpells').callprop('indexOf', var.get('temp'))>(-Js(1.0))):
                pass
            else:
                var.get('tempSpells').callprop('push', var.get('temp'))
                (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
        var.get('tempSpells').callprop('sort')
        var.put('mySpells', var.get('mySpells').callprop('concat', var.get('tempSpells')))
        var.put('tempSpells', Js([]))
        var.put('x', var.get('sp2'))
        while (var.get('x')>Js(0.0)):
            var.put('tempAr', var.get('so2'))
            if (var.get('Math').callprop('random')<Js(0.66)):
                var.put('tempAr', Js([Js('Blindness/Deafness'), Js('Blur'), Js('Cloud of Daggers'), Js('Crown of Madness'), Js('Enhance Ability'), Js('Enlarge/Reduce'), Js('Hold Person'), Js('Invisibility'), Js('Mirror Image'), Js('Phantasmal Force'), Js('Scorching Ray'), Js('Shatter'), Js('Suggestion'), Js('Web')]))
            var.put('temp', var.get('tempAr').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tempAr').get('length')))))
            if (var.get('tempSpells').callprop('indexOf', var.get('temp'))>(-Js(1.0))):
                pass
            else:
                var.get('tempSpells').callprop('push', var.get('temp'))
                (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
        var.get('tempSpells').callprop('sort')
        var.put('mySpells', var.get('mySpells').callprop('concat', var.get('tempSpells')))
        var.put('tempSpells', Js([]))
        var.put('x', var.get('sp3'))
        while (var.get('x')>Js(0.0)):
            var.put('tempAr', var.get('so3'))
            if (var.get('Math').callprop('random')<Js(0.5)):
                var.put('tempAr', Js([Js('Blink'), Js('Counterspell'), Js('Dispel Magic'), Js('Fear'), Js('Fireball'), Js('Fireball'), Js('Fly'), Js('Gaseous Form'), Js('Haste'), Js('Hypnotic Pattern'), Js('Lightning Bolt'), Js('Lightning Bolt'), Js('Lightning Bolt'), Js('Major Image'), Js('Protection from Energy'), Js('Slow'), Js('Stinking Cloud')]))
            var.put('temp', var.get('tempAr').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tempAr').get('length')))))
            if (var.get('tempSpells').callprop('indexOf', var.get('temp'))==(-Js(1.0))):
                var.get('tempSpells').callprop('push', var.get('temp'))
                (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
        var.get('tempSpells').callprop('sort')
        var.put('mySpells', var.get('mySpells').callprop('concat', var.get('tempSpells')))
        var.put('tempSpells', Js([]))
        var.put('x', var.get('sp4'))
        while (var.get('x')>Js(0.0)):
            var.put('tempAr', var.get('so4'))
            var.put('temp', var.get('tempAr').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tempAr').get('length')))))
            if (var.get('tempSpells').callprop('indexOf', var.get('temp'))==(-Js(1.0))):
                var.get('tempSpells').callprop('push', var.get('temp'))
                (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
        var.get('tempSpells').callprop('sort')
        var.put('mySpells', var.get('mySpells').callprop('concat', var.get('tempSpells')))
        var.put('tempSpells', Js([]))
        var.put('x', var.get('sp5'))
        while (var.get('x')>Js(0.0)):
            var.put('tempAr', var.get('so5'))
            var.put('temp', var.get('tempAr').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tempAr').get('length')))))
            if (var.get('tempSpells').callprop('indexOf', var.get('temp'))==(-Js(1.0))):
                var.get('tempSpells').callprop('push', var.get('temp'))
                (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
        var.get('tempSpells').callprop('sort')
        var.put('mySpells', var.get('mySpells').callprop('concat', var.get('tempSpells')))
    if (var.get('cl')==Js(14.0)):
        var.put('ss1', Js(1.0))
        if (var.get('level')>Js(1.0)):
            var.put('ss1', Js(2.0))
        var.put('sp', (var.get('level')+Js(1.0)))
        if (var.get('level')>Js(8.0)):
            var.put('sp', Js(10.0))
        var.put('sp1', Js(2.0))
        var.put('sp2', Js(0.0))
        var.put('sp3', Js(0.0))
        var.put('sp4', Js(0.0))
        var.put('sp5', Js(0.0))
        if (var.get('level')<Js(3.0)):
            var.put('sp1', var.get('sp'))
            var.put('sp2', Js(0.0))
        else:
            if (var.get('level')<Js(5.0)):
                var.put('x', var.get('Math').callprop('floor', (var.get('sp')*Js(0.7))))
                var.put('sp1', var.get('x'))
                var.put('sp2', (var.get('sp')-var.get('x')))
            else:
                if (var.get('level')<Js(7.0)):
                    var.put('x', var.get('Math').callprop('ceil', (var.get('sp')*Js(0.35))))
                    var.put('y', var.get('Math').callprop('floor', (var.get('sp')*Js(0.35))))
                    var.put('sp1', var.get('x'))
                    var.put('sp2', var.get('y'))
                    var.put('sp3', ((var.get('sp')-var.get('x'))-var.get('y')))
                else:
                    if (var.get('level')<Js(9.0)):
                        var.put('x', var.get('Math').callprop('floor', (var.get('sp')*Js(0.28))))
                        var.put('y', var.get('Math').callprop('floor', (var.get('sp')*Js(0.28))))
                        var.put('z', var.get('Math').callprop('floor', (var.get('sp')*Js(0.28))))
                        var.put('sum', (((var.get('sp')-var.get('x'))-var.get('y'))-var.get('z')))
                        var.put('sp1', var.get('sum'))
                        var.put('sp2', var.get('y'))
                        var.put('sp3', var.get('z'))
                        var.put('sp4', var.get('x'))
                    else:
                        var.put('x', var.get('Math').callprop('floor', (var.get('sp')*Js(0.21))))
                        var.put('y', var.get('Math').callprop('ceil', (var.get('sp')*Js(0.18))))
                        var.put('z', var.get('Math').callprop('ceil', (var.get('sp')*Js(0.18))))
                        var.put('xx', var.get('Math').callprop('floor', (var.get('sp')*Js(0.21))))
                        var.put('sum', ((((var.get('sp')-var.get('x'))-var.get('y'))-var.get('z'))-var.get('xx')))
                        var.put('sp1', var.get('sum'))
                        var.put('sp2', var.get('y'))
                        var.put('sp3', var.get('z'))
                        var.put('sp4', var.get('xx'))
                        var.put('sp5', var.get('x'))
        var.get('console').callprop('log', (((((((((((Js('Spells known:  ')+var.get('sp1'))+Js('/ '))+var.get('sp2'))+Js('/ '))+var.get('sp3'))+Js('/ '))+var.get('sp4'))+Js('/ '))+var.get('sp5'))+Js(' / Total = '))+var.get('sp')))
        var.put('x', Js(2.0))
        if (var.get('level')>Js(3.0)):
            var.put('x', Js(3.0))
        if (var.get('level')>Js(9.0)):
            var.put('x', Js(4.0))
        if (var.get('eblast')==Js(True)):
            var.get('myCantrips').callprop('push', Js('Eldritch Blast'))
            (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
        while (var.get('x')>Js(0.0)):
            var.put('tempAr', var.get('waCantrip'))
            if (var.get('Math').callprop('random')<Js(0.66)):
                var.put('tempAr', Js([Js('Blade Ward'), Js('Chill Touch'), Js('Eldritch Blast'), Js('Eldritch Blast'), Js('Minor Illusion'), Js('Poison Spray'), Js('True Strike')]))
            var.put('temp', var.get('tempAr').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tempAr').get('length')))))
            if ((var.get('myCantrips').callprop('indexOf', var.get('temp'))==(-Js(1.0))) and (var.get('raceSpells').callprop('indexOf', var.get('temp'))==(-Js(1.0)))):
                var.get('myCantrips').callprop('push', var.get('temp'))
                (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
        var.get('myCantrips').callprop('sort')
        if (var.get('tome')==Js(True)):
            var.put('z', Js(3.0))
            while (var.get('z')>Js(0.0)):
                var.put('y', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(5.0))))
                if (var.get('y')==Js(0.0)):
                    var.put('temp', var.get('baCantrip').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('baCantrip').get('length')))))
                    if (((var.get('myCantrips').callprop('indexOf', var.get('temp'))==(-Js(1.0))) and (var.get('waTome').callprop('indexOf', var.get('temp'))==(-Js(1.0)))) and (var.get('raceSpells').callprop('indexOf', var.get('temp'))==(-Js(1.0)))):
                        var.get('waTome').callprop('push', var.get('temp'))
                        (var.put('z',Js(var.get('z').to_number())-Js(1))+Js(1))
                if (var.get('y')==Js(1.0)):
                    var.put('temp', var.get('clCantrip').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('clCantrip').get('length')))))
                    if (((var.get('myCantrips').callprop('indexOf', var.get('temp'))==(-Js(1.0))) and (var.get('waTome').callprop('indexOf', var.get('temp'))==(-Js(1.0)))) and (var.get('raceSpells').callprop('indexOf', var.get('temp'))==(-Js(1.0)))):
                        var.get('waTome').callprop('push', var.get('temp'))
                        (var.put('z',Js(var.get('z').to_number())-Js(1))+Js(1))
                if (var.get('y')==Js(2.0)):
                    var.put('temp', var.get('drCantrip').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('drCantrip').get('length')))))
                    if (((var.get('myCantrips').callprop('indexOf', var.get('temp'))==(-Js(1.0))) and (var.get('waTome').callprop('indexOf', var.get('temp'))==(-Js(1.0)))) and (var.get('raceSpells').callprop('indexOf', var.get('temp'))==(-Js(1.0)))):
                        var.get('waTome').callprop('push', var.get('temp'))
                        (var.put('z',Js(var.get('z').to_number())-Js(1))+Js(1))
                if (var.get('y')==Js(3.0)):
                    var.put('temp', var.get('soCantrip').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('soCantrip').get('length')))))
                    if (((var.get('myCantrips').callprop('indexOf', var.get('temp'))==(-Js(1.0))) and (var.get('waTome').callprop('indexOf', var.get('temp'))==(-Js(1.0)))) and (var.get('raceSpells').callprop('indexOf', var.get('temp'))==(-Js(1.0)))):
                        var.get('waTome').callprop('push', var.get('temp'))
                        (var.put('z',Js(var.get('z').to_number())-Js(1))+Js(1))
                if (var.get('y')==Js(4.0)):
                    var.put('temp', var.get('wiCantrip').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('wiCantrip').get('length')))))
                    if (((var.get('myCantrips').callprop('indexOf', var.get('temp'))==(-Js(1.0))) and (var.get('waTome').callprop('indexOf', var.get('temp'))==(-Js(1.0)))) and (var.get('raceSpells').callprop('indexOf', var.get('temp'))==(-Js(1.0)))):
                        var.get('waTome').callprop('push', var.get('temp'))
                        (var.put('z',Js(var.get('z').to_number())-Js(1))+Js(1))
            var.get('waTome').callprop('sort')
            if (var.get('abOutput').callprop('indexOf', Js('Ancient Secrets'))>(-Js(1.0))):
                var.put('xx', Js(2.0))
                while (var.get('xx')>Js(0.0)):
                    var.put('temp', var.get('tomeRituals').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tomeRituals').get('length')))))
                    if ((var.get('mySpells').callprop('indexOf', var.get('temp'))==(-Js(1.0))) and (var.get('waTomeRituals').callprop('indexOf', var.get('temp'))==(-Js(1.0)))):
                        var.get('waTomeRituals').callprop('push', var.get('temp'))
                        (var.put('xx',Js(var.get('xx').to_number())-Js(1))+Js(1))
                var.put('xx', Js(0.0))
                if (var.get('upgradeUncommon')()==Js(True)):
                    var.put('xx', var.get('Math').callprop('floor', ((var.get('Math').callprop('random')*Js(2.0))+Js(1.0))), '+')
                if (var.get('upgradeRare')()==Js(True)):
                    var.put('xx', var.get('Math').callprop('floor', ((var.get('Math').callprop('random')*Js(2.0))+Js(1.0))), '+')
                var.get('console').callprop('log', ((Js('Tome has ')+(Js(2.0)+var.get('xx')))+Js(' rituals')))
                if (var.get('level')>Js(3.0)):
                    var.get('tomeRituals').callprop('push', Js('Magic Mouth'))
                    var.get('tomeRituals').callprop('push', Js('Magic Mouth'))
                    var.get('tomeRituals').callprop('push', Js('Silence'))
                    var.get('tomeRituals').callprop('push', Js('Augury'))
                    var.get('tomeRituals').callprop('push', Js('Beast Sense'))
                    var.get('tomeRituals').callprop('push', Js('Gentle Repose'))
                    var.get('tomeRituals').callprop('push', Js('Locate Animals or Plants'))
                    var.get('tomeRituals').callprop('push', Js('Animal Messenger'))
                    var.get('tomeRituals').callprop('push', Js('Animal Messenger'))
                if (var.get('level')>Js(5.0)):
                    var.get('tomeRituals').callprop('push', Js('Meld into Stone'))
                    var.get('tomeRituals').callprop('push', Js('Feign Death'))
                    var.get('tomeRituals').callprop('push', Js('Meld into Stone'))
                    var.get('tomeRituals').callprop('push', Js('Leomund’s Tiny Hut'))
                    var.get('tomeRituals').callprop('push', Js('Leomund’s Tiny Hut'))
                    var.get('tomeRituals').callprop('push', Js('Water Breathing'))
                    var.get('tomeRituals').callprop('push', Js('Phantom Steed'))
                    var.get('tomeRituals').callprop('push', Js('Water Walk'))
                    var.get('tomeRituals').callprop('push', Js('Water Breathing'))
                    var.get('tomeRituals').callprop('push', Js('Phantom Steed'))
                    var.get('tomeRituals').callprop('push', Js('Water Walk'))
                if (var.get('level')>Js(7.0)):
                    var.get('tomeRituals').callprop('push', Js('Divination'))
                if (var.get('level')>Js(9.0)):
                    var.get('tomeRituals').callprop('push', Js('Contact Other Plane'))
                    var.get('tomeRituals').callprop('push', Js('Commune'))
                    var.get('tomeRituals').callprop('push', Js('Contact Other Plane'))
                    var.get('tomeRituals').callprop('push', Js('Commune with Nature'))
                    var.get('tomeRituals').callprop('push', Js("Rary's Telepathic Bond"))
                while (var.get('xx')>Js(0.0)):
                    var.put('temp', var.get('tomeRituals').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tomeRituals').get('length')))))
                    if ((var.get('mySpells').callprop('indexOf', var.get('temp'))==(-Js(1.0))) and (var.get('waTomeRituals').callprop('indexOf', var.get('temp'))==(-Js(1.0)))):
                        var.get('waTomeRituals').callprop('push', var.get('temp'))
                        (var.put('xx',Js(var.get('xx').to_number())-Js(1))+Js(1))
            var.get('waTomeRituals').callprop('sort')
        var.put('tempSpells', Js([]))
        var.put('x', var.get('sp1'))
        while (var.get('x')>Js(0.0)):
            var.put('tempAr', var.get('wa1'))
            if (var.get('Math').callprop('random')<Js(0.66)):
                var.put('tempAr', Js([Js('Armor of Agathys'), Js('Arms of Hadar'), Js('Charm Person'), Js('Hellish Rebuke'), Js('Hex'), Js('Witch Bolt')]))
            var.put('tempAr', var.get('tempAr').callprop('concat', var.get('patronSpells1')))
            var.put('temp', var.get('tempAr').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tempAr').get('length')))))
            if (var.get('tempSpells').callprop('indexOf', var.get('temp'))==(-Js(1.0))):
                var.get('tempSpells').callprop('push', var.get('temp'))
                (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
        var.get('tempSpells').callprop('sort')
        var.put('mySpells', var.get('mySpells').callprop('concat', var.get('tempSpells')))
        var.put('tempSpells', Js([]))
        var.put('x', var.get('sp2'))
        while (var.get('x')>Js(0.0)):
            var.put('tempAr', var.get('wa2'))
            if (var.get('Math').callprop('random')<Js(0.66)):
                var.put('tempAr', Js([Js('Cloud of Daggers'), Js('Crown of Madness'), Js('Hold Person'), Js('Invisibility'), Js('Mirror Image'), Js('Misty Step'), Js('Ray of Enfeeblement'), Js('Shatter'), Js('Suggestion')]))
            var.put('tempAr', var.get('tempAr').callprop('concat', var.get('patronSpells2')))
            var.put('temp', var.get('tempAr').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tempAr').get('length')))))
            if (var.get('tempSpells').callprop('indexOf', var.get('temp'))==(-Js(1.0))):
                var.get('tempSpells').callprop('push', var.get('temp'))
                (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
        var.get('tempSpells').callprop('sort')
        var.put('mySpells', var.get('mySpells').callprop('concat', var.get('tempSpells')))
        var.put('tempSpells', Js([]))
        var.put('x', var.get('sp3'))
        while (var.get('x')>Js(0.0)):
            var.put('tempAr', var.get('wa3'))
            if (var.get('Math').callprop('random')<Js(0.66)):
                var.put('tempAr', Js([Js('Counterspell'), Js('Dispel Magic'), Js('Fear'), Js('Fear'), Js('Fly'), Js('Gaseous Form'), Js('Hunger of Hadar'), Js('Hunger of Hadar'), Js('Hypnotic Pattern'), Js('Magic Circle'), Js('Major Image'), Js('Vampiric Touch'), Js('Vampiric Touch')]))
            var.put('tempAr', var.get('tempAr').callprop('concat', var.get('patronSpells3')))
            var.put('temp', var.get('tempAr').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tempAr').get('length')))))
            if (var.get('tempSpells').callprop('indexOf', var.get('temp'))==(-Js(1.0))):
                var.get('tempSpells').callprop('push', var.get('temp'))
                (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
        var.get('tempSpells').callprop('sort')
        var.put('mySpells', var.get('mySpells').callprop('concat', var.get('tempSpells')))
        var.put('tempSpells', Js([]))
        var.put('x', var.get('sp4'))
        while (var.get('x')>Js(0.0)):
            var.put('tempAr', var.get('wa4'))
            if (var.get('Math').callprop('random')<Js(0.5)):
                var.put('tempAr', Js([Js('Banishment'), Js('Blight'), Js('Dimension Door')]))
            var.put('tempAr', var.get('tempAr').callprop('concat', var.get('patronSpells4')))
            var.put('temp', var.get('tempAr').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tempAr').get('length')))))
            if (var.get('tempSpells').callprop('indexOf', var.get('temp'))==(-Js(1.0))):
                var.get('tempSpells').callprop('push', var.get('temp'))
                (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
        var.get('tempSpells').callprop('sort')
        var.put('mySpells', var.get('mySpells').callprop('concat', var.get('tempSpells')))
        var.put('tempSpells', Js([]))
        var.put('x', var.get('sp5'))
        while (var.get('x')>Js(0.0)):
            var.put('tempAr', var.get('wa5'))
            var.put('tempAr', var.get('tempAr').callprop('concat', var.get('patronSpells5')))
            var.put('temp', var.get('tempAr').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tempAr').get('length')))))
            if (var.get('tempSpells').callprop('indexOf', var.get('temp'))==(-Js(1.0))):
                var.get('tempSpells').callprop('push', var.get('temp'))
                (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
        var.get('tempSpells').callprop('sort')
        var.put('mySpells', var.get('mySpells').callprop('concat', var.get('tempSpells')))
    if (var.get('cl')==Js(15.0)):
        var.put('ss1', (var.get('level')+Js(1.0)))
        var.put('ss2', Js(0.0))
        if (var.get('level')>Js(2.0)):
            var.put('ss2', Js(2.0))
        if (var.get('level')>Js(3.0)):
            var.put('ss1', Js(4.0))
            var.put('ss2', Js(3.0))
        if (var.get('level')==Js(5.0)):
            var.put('ss3', Js(2.0))
        if (var.get('level')>Js(5.0)):
            var.put('ss3', Js(3.0))
        if (var.get('level')>Js(6.0)):
            var.put('ss4', (var.get('level')-Js(6.0)))
        if (var.get('level')>Js(8.0)):
            var.put('ss4', Js(3.0))
            var.put('ss5', (var.get('level')-Js(8.0)))
        var.put('sp1', Js(6.0))
        var.put('sp2', Js(0.0))
        var.put('sp', (var.get('mod').get('3')+var.get('level')))
        if (var.get('level')>Js(1.0)):
            var.put('sp1', Js(2.0), '+')
        if (var.get('level')>Js(2.0)):
            var.put('sp2', ((var.get('level')-Js(2.0))*Js(2.0)), '+')
        if (var.get('level')>Js(4.0)):
            var.put('sp2', Js(4.0))
            var.put('sp3', ((var.get('level')-Js(4.0))*Js(2.0)))
        if (var.get('level')>Js(6.0)):
            var.put('sp3', Js(4.0))
            var.put('sp4', ((var.get('level')-Js(6.0))*Js(2.0)))
        if (var.get('level')>Js(8.0)):
            var.put('sp4', Js(4.0))
            var.put('sp5', ((var.get('level')-Js(8.0))*Js(2.0)))
        var.get('console').callprop('log', (((((((((((Js('Spellbook:   ')+var.get('sp1'))+Js('/ '))+var.get('sp2'))+Js('/ '))+var.get('sp3'))+Js('/ '))+var.get('sp4'))+Js('/ '))+var.get('sp5'))+Js(' / Total = '))+var.get('sp')))
        var.put('wiz3', Js(0.0))
        var.put('wiz2', Js(0.0))
        if (var.get('level')>Js(8.0)):
            var.put('x', var.get('Math').callprop('floor', (var.get('sp')*Js(0.21))))
            var.put('y', var.get('Math').callprop('ceil', (var.get('sp')*Js(0.18))))
            var.put('z', var.get('Math').callprop('ceil', (var.get('sp')*Js(0.18))))
            var.put('xx', var.get('Math').callprop('floor', (var.get('sp')*Js(0.21))))
            var.put('sum', ((((var.get('sp')-var.get('x'))-var.get('y'))-var.get('z'))-var.get('xx')))
            var.put('wiz1', var.get('sum'))
            var.put('wiz2', var.get('y'))
            var.put('wiz3', var.get('z'))
            var.put('wiz4', var.get('xx'))
            var.put('wiz5', var.get('x'))
        else:
            if (var.get('level')>Js(6.0)):
                var.put('x', var.get('Math').callprop('floor', (var.get('sp')*Js(0.28))))
                var.put('y', var.get('Math').callprop('floor', (var.get('sp')*Js(0.28))))
                var.put('z', var.get('Math').callprop('floor', (var.get('sp')*Js(0.28))))
                var.put('sum', (((var.get('sp')-var.get('x'))-var.get('y'))-var.get('z')))
                var.put('wiz1', var.get('sum'))
                var.put('wiz2', var.get('y'))
                var.put('wiz3', var.get('z'))
                var.put('wiz4', var.get('x'))
            else:
                if (var.get('level')>Js(4.0)):
                    var.put('wiz1', var.get('Math').callprop('ceil', (var.get('sp')*Js(0.35))))
                    var.put('wiz2', var.get('Math').callprop('floor', (var.get('sp')*Js(0.35))))
                    var.put('wiz3', ((var.get('sp')-var.get('wiz1'))-var.get('wiz2')))
                else:
                    if (var.get('level')>Js(2.0)):
                        var.put('wiz1', var.get('Math').callprop('floor', (var.get('sp')*Js(0.7))))
                        var.put('wiz2', (var.get('sp')-var.get('wiz1')))
                    else:
                        var.put('wiz1', var.get('sp'))
                        var.put('wiz2', Js(0.0))
        while (var.get('wiz5')>var.get('sp5')):
            (var.put('wiz5',Js(var.get('wiz5').to_number())-Js(1))+Js(1))
            (var.put('wiz4',Js(var.get('wiz4').to_number())+Js(1))-Js(1))
        while (var.get('wiz4')>var.get('sp4')):
            (var.put('wiz4',Js(var.get('wiz4').to_number())-Js(1))+Js(1))
            (var.put('wiz3',Js(var.get('wiz3').to_number())+Js(1))-Js(1))
        while (var.get('wiz3')>var.get('sp3')):
            (var.put('wiz3',Js(var.get('wiz3').to_number())-Js(1))+Js(1))
            (var.put('wiz2',Js(var.get('wiz2').to_number())+Js(1))-Js(1))
        while (var.get('wiz2')>var.get('sp2')):
            (var.put('wiz2',Js(var.get('wiz2').to_number())-Js(1))+Js(1))
            (var.put('wiz1',Js(var.get('wiz1').to_number())+Js(1))-Js(1))
        var.get('console').callprop('log', ((((((((((((Js('memorized:   (')+var.get('wiz1'))+Js('/ '))+var.get('wiz2'))+Js('/ '))+var.get('wiz3'))+Js('/ '))+var.get('wiz4'))+Js('/ '))+var.get('wiz5'))+Js(' --- total ='))+var.get('sp'))+Js(')')))
        var.put('x', Js(3.0))
        if (var.get('level')>Js(3.0)):
            var.put('x', Js(4.0))
        if (var.get('level')>Js(9.0)):
            var.put('x', Js(5.0))
        if (var.get('wiSchool')==Js(5.0)):
            var.put('temp', Js('Minor Illusion'))
            if ((var.get('myCantrips').callprop('indexOf', var.get('temp'))==(-Js(1.0))) and (var.get('raceSpells').callprop('indexOf', var.get('temp'))==(-Js(1.0)))):
                var.get('myCantrips').callprop('push', var.get('temp'))
        while (var.get('x')>Js(0.0)):
            if (var.get('Math').callprop('random')<Js(0.5)):
                var.put('tempAr', Js([Js('Acid Splash'), Js('Blade Ward'), Js('Chill Touch'), Js('Fire Bolt'), Js('Minor Illusion'), Js('Poison Spray'), Js('Ray of Frost'), Js('Shocking Grasp'), Js('True Strike')]))
            else:
                var.put('tempAr', var.get('wiCantrip'))
            var.put('temp', var.get('tempAr').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tempAr').get('length')))))
            if ((var.get('myCantrips').callprop('indexOf', var.get('temp'))==(-Js(1.0))) and (var.get('raceSpells').callprop('indexOf', var.get('temp'))==(-Js(1.0)))):
                var.get('myCantrips').callprop('push', var.get('temp'))
                (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
        var.get('myCantrips').callprop('sort')
        var.put('x', var.get('sp1'))
        while (var.get('x')>Js(0.0)):
            var.put('tempAr', var.get('wi1'))
            if (var.get('Math').callprop('random')<Js(0.66)):
                var.put('tempAr', Js([Js('Burning Hands'), Js('Chromatic Orb'), Js('Color Spray'), Js('False Life'), Js('Mage Armor'), Js('Magic Missile'), Js('Ray of Sickness'), Js('Shield'), Js('Sleep'), Js("Tasha's Hideous Laughter"), Js('Thunderwave'), Js('Witch Bolt')]))
            if (var.get('Math').callprop('random')<Js(0.4)):
                var.get('tempAr').callprop('push', Js('Find Familiar'))
            var.put('temp', var.get('tempAr').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tempAr').get('length')))))
            if (var.get('tempSpells').callprop('indexOf', var.get('temp'))>(-Js(1.0))):
                pass
            else:
                var.get('tempSpells').callprop('push', var.get('temp'))
                (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
        #for JS loop
        var.put('x', Js(0.0))
        while (var.get('x')<var.get('wiz1')):
            var.put('temp', var.get('tempSpells').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tempSpells').get('length')))))
            if ((var.get('wiz1Prepared').callprop('indexOf', var.get('temp'))==(-Js(1.0))) and (var.get('temp')!=Js('Find Familiar'))):
                var.get('wiz1Prepared').callprop('push', var.get('temp'))
                (var.put('x',Js(var.get('x').to_number())+Js(1))-Js(1))
        
        var.get('wiz1Prepared').callprop('sort')
        var.get('tempSpells').callprop('sort')
        var.put('mySpells', var.get('mySpells').callprop('concat', var.get('tempSpells')))
        var.put('x', var.get('sp2'))
        var.put('tempSpells', Js([]))
        while (var.get('x')>Js(0.0)):
            var.put('tempAr', var.get('wi2'))
            if (var.get('Math').callprop('random')<Js(0.66)):
                var.put('tempAr', Js([Js('Blindness/Deafness'), Js('Blur'), Js('Cloud of Daggers'), Js('Crown of Madness'), Js('Flaming Sphere'), Js('Hold Person'), Js('Invisibility'), Js("Melf's Acid Arrow"), Js('Mirror Image'), Js('Phantasmal Force'), Js('Ray of Enfeeblement'), Js('Scorching Ray'), Js('Shatter'), Js('Suggestion'), Js('Web')]))
            var.put('temp', var.get('tempAr').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tempAr').get('length')))))
            if (var.get('tempSpells').callprop('indexOf', var.get('temp'))>(-Js(1.0))):
                pass
            else:
                var.get('tempSpells').callprop('push', var.get('temp'))
                (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
        #for JS loop
        var.put('x', Js(0.0))
        while (var.get('x')<var.get('wiz2')):
            var.put('temp', var.get('tempSpells').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tempSpells').get('length')))))
            if (var.get('wiz2Prepared').callprop('indexOf', var.get('temp'))==(-Js(1.0))):
                var.get('wiz2Prepared').callprop('push', var.get('temp'))
                (var.put('x',Js(var.get('x').to_number())+Js(1))-Js(1))
        
        var.get('wiz2Prepared').callprop('sort')
        var.get('tempSpells').callprop('sort')
        var.put('mySpells', var.get('mySpells').callprop('concat', var.get('tempSpells')))
        var.put('tempSpells', Js([]))
        if (var.get('abOutput').callprop('indexOf', Js('Undead Thralls'))>(-Js(1.0))):
            var.get('tempSpells').callprop('push', Js('Animate Dead'))
        var.put('x', var.get('sp3'))
        while (var.get('x')>Js(0.0)):
            var.put('tempAr', var.get('wi3'))
            if (var.get('Math').callprop('random')<Js(0.66)):
                def PyJs_LONG_13_(var=var):
                    return var.put('tempAr', Js([Js('Animate Dead'), Js('Bestow Curse'), Js('Blink'), Js('Counterspell'), Js('Dispel Magic'), Js('Fear'), Js('Fireball'), Js('Fireball'), Js('Fly'), Js('Gaseous Form'), Js('Glyph of Warding'), Js('Haste'), Js('Hypnotic Pattern'), Js('Leomund’s Tiny Hut'), Js('Lightning Bolt'), Js('Lightning Bolt'), Js('Lightning Bolt'), Js('Magic Circle'), Js('Major Image'), Js('Protection from Energy'), Js('Slow'), Js('Stinking Cloud'), Js('Vampiric Touch')]))
                PyJs_LONG_13_()
            var.put('temp', var.get('tempAr').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tempAr').get('length')))))
            if (var.get('tempSpells').callprop('indexOf', var.get('temp'))==(-Js(1.0))):
                var.get('tempSpells').callprop('push', var.get('temp'))
                (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
        #for JS loop
        var.put('x', Js(0.0))
        while (var.get('x')<var.get('wiz3')):
            var.put('temp', var.get('tempSpells').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tempSpells').get('length')))))
            if ((var.get('abOutput').callprop('indexOf', Js('Undead Thralls'))>(-Js(1.0))) and (var.get('Math').callprop('random')>Js(0.66))):
                var.put('temp', Js('Animate Dead'))
            if (var.get('wiz3Prepared').callprop('indexOf', var.get('temp'))==(-Js(1.0))):
                var.get('wiz3Prepared').callprop('push', var.get('temp'))
                (var.put('x',Js(var.get('x').to_number())+Js(1))-Js(1))
        
        var.get('wiz3Prepared').callprop('sort')
        var.get('tempSpells').callprop('sort')
        var.put('mySpells', var.get('mySpells').callprop('concat', var.get('tempSpells')))
        var.put('tempSpells', Js([]))
        if (var.get('abOutput').callprop('indexOf', Js('Shapechanger'))>(-Js(1.0))):
            var.get('tempSpells').callprop('push', Js('Polymorph'))
        var.put('x', var.get('sp4'))
        while (var.get('x')>Js(0.0)):
            var.put('tempAr', var.get('wi4'))
            if (var.get('Math').callprop('random')<Js(0.5)):
                var.put('tempAr', Js([Js('Banishment'), Js('Blight'), Js('Confusion'), Js('Conjure Minor Elementals'), Js('Dimension Door'), Js("Evard's Black Tentacles"), Js('Fire Shield'), Js('Greater Invisibility'), Js('Ice Storm'), Js('Mordenkainen’s Faithful Hound'), Js('Otiluke’s Resilient Sphere'), Js('Phantasmal Killer'), Js('Polymorph'), Js('Stoneskin'), Js('Wall of Fire')]))
            var.put('temp', var.get('tempAr').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tempAr').get('length')))))
            if (var.get('tempSpells').callprop('indexOf', var.get('temp'))==(-Js(1.0))):
                var.get('tempSpells').callprop('push', var.get('temp'))
                (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
        #for JS loop
        var.put('x', Js(0.0))
        while (var.get('x')<var.get('wiz4')):
            var.put('temp', var.get('tempSpells').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tempSpells').get('length')))))
            if ((var.get('abOutput').callprop('indexOf', Js('Shapechanger'))>(-Js(1.0))) and (var.get('Math').callprop('random')>Js(0.66))):
                var.put('temp', Js('Polymorph'))
            if (var.get('wiz4Prepared').callprop('indexOf', var.get('temp'))==(-Js(1.0))):
                var.get('wiz4Prepared').callprop('push', var.get('temp'))
                (var.put('x',Js(var.get('x').to_number())+Js(1))-Js(1))
        
        var.get('wiz4Prepared').callprop('sort')
        var.get('tempSpells').callprop('sort')
        var.put('mySpells', var.get('mySpells').callprop('concat', var.get('tempSpells')))
        var.put('tempSpells', Js([]))
        var.put('x', var.get('sp5'))
        while (var.get('x')>Js(0.0)):
            var.put('tempAr', var.get('wi5'))
            if (var.get('Math').callprop('random')<Js(0.5)):
                var.put('tempAr', Js([Js('Animate Objects'), Js('Bigby’s Hand'), Js('CloudkilI'), Js('Cone of Cold'), Js('Conjure Elemental'), Js('Dominate Person'), Js('Geas'), Js('Hold Monster'), Js('Legend Lore'), Js('Mislead'), Js('Passwall'), Js('Planar Binding'), Js('Seeming'), Js('Telekinesis'), Js('Teleportation Circle'), Js('Wall of Force'), Js('Wall of Stone')]))
            var.put('temp', var.get('tempAr').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tempAr').get('length')))))
            if (var.get('tempSpells').callprop('indexOf', var.get('temp'))==(-Js(1.0))):
                var.get('tempSpells').callprop('push', var.get('temp'))
                (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
        #for JS loop
        var.put('x', Js(0.0))
        while (var.get('x')<var.get('wiz5')):
            var.put('temp', var.get('tempSpells').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('tempSpells').get('length')))))
            if (var.get('wiz5Prepared').callprop('indexOf', var.get('temp'))==(-Js(1.0))):
                var.get('wiz5Prepared').callprop('push', var.get('temp'))
                (var.put('x',Js(var.get('x').to_number())+Js(1))-Js(1))
        
        var.get('wiz5Prepared').callprop('sort')
        var.get('tempSpells').callprop('sort')
        var.put('mySpells', var.get('mySpells').callprop('concat', var.get('tempSpells')))
    if (var.get('myCantrips').get('length')>Js(0.0)):
        if (var.get('mySpells').get('length')>Js(0.0)):
            var.put('cOutput', Js('==EOF==<b>Cantrip'))
        else:
            var.put('cOutput', Js('==EOF==<b>Cantrip'))
        if (var.get('myCantrips').get('length')>Js(1.0)):
            var.put('cOutput', Js('s'), '+')
        var.put('cOutput', Js(':</b> '), '+')
        #for JS loop
        var.put('x', Js(0.0))
        while (var.get('x')<var.get('myCantrips').get('length')):
            try:
                if (var.get('x')==Js(0.0)):
                    var.put('cOutput', var.get('myCantrips').get(var.get('x')), '+')
                else:
                    var.put('cOutput', (Js(', ')+var.get('myCantrips').get(var.get('x'))), '+')
            finally:
                    (var.put('x',Js(var.get('x').to_number())+Js(1))-Js(1))
        if (var.get('mySpells').get('length')==Js(0.0)):
            var.put('cOutput', ((Js('     (<b>Spell save DC:</b>  ')+((Js(8.0)+var.get('prof'))+var.get('mod').get(var.get('spellAbility'))))+Js(') ')), '+')
    if (var.get('cl')==Js(15.0)):
        var.put('spOutput', Js('==EOF==<b>Spellbook:</b>  '), '+')
    if ((var.get('cl')==Js(4.0)) or (var.get('cl')==Js(3.0))):
        var.put('spOutput', Js('==EOF==<b>Current spells:</b> '), '+')
    if ((var.get('cl')==Js(9.0)) and (var.get('mySpells').get('length')>Js(0.0))):
        var.put('spOutput', Js('==EOF==<b>Current spells:</b>  '), '+')
    if (((((var.get('mySpells').get('length')>Js(0.0)) and (var.get('cl')!=Js(15.0))) and (var.get('cl')!=Js(4.0))) and (var.get('cl')!=Js(3.0))) and (var.get('cl')!=Js(9.0))):
        var.put('spOutput', Js('==EOF==<b>Spells known:</b>  '), '+')
    #for JS loop
    var.put('x', Js(0.0))
    while (var.get('x')<var.get('mySpells').get('length')):
        try:
            if (var.get('x')==Js(0.0)):
                var.put('spOutput', var.get('mySpells').get(var.get('x')), '+')
            else:
                var.put('spOutput', (Js(', ')+var.get('mySpells').get(var.get('x'))), '+')
        finally:
                (var.put('x',Js(var.get('x').to_number())+Js(1))-Js(1))
    if (var.get('cl')==Js(15.0)):
        var.put('spOutput', Js('==EOF==<b>Current spells:</b>  '), '+')
        #for JS loop
        var.put('x', Js(0.0))
        while (var.get('x')<var.get('wiz1Prepared').get('length')):
            try:
                if (var.get('x')==Js(0.0)):
                    var.put('spOutput', var.get('wiz1Prepared').get(var.get('x')), '+')
                else:
                    var.put('spOutput', (Js(', ')+var.get('wiz1Prepared').get(var.get('x'))), '+')
            finally:
                    (var.put('x',Js(var.get('x').to_number())+Js(1))-Js(1))
        #for JS loop
        var.put('x', Js(0.0))
        while (var.get('x')<var.get('wiz2Prepared').get('length')):
            try:
                var.put('spOutput', (Js(', ')+var.get('wiz2Prepared').get(var.get('x'))), '+')
            finally:
                    (var.put('x',Js(var.get('x').to_number())+Js(1))-Js(1))
        #for JS loop
        var.put('x', Js(0.0))
        while (var.get('x')<var.get('wiz3Prepared').get('length')):
            try:
                var.put('spOutput', (Js(', ')+var.get('wiz3Prepared').get(var.get('x'))), '+')
            finally:
                    (var.put('x',Js(var.get('x').to_number())+Js(1))-Js(1))
        #for JS loop
        var.put('x', Js(0.0))
        while (var.get('x')<var.get('wiz4Prepared').get('length')):
            try:
                var.put('spOutput', (Js(', ')+var.get('wiz4Prepared').get(var.get('x'))), '+')
            finally:
                    (var.put('x',Js(var.get('x').to_number())+Js(1))-Js(1))
        #for JS loop
        var.put('x', Js(0.0))
        while (var.get('x')<var.get('wiz5Prepared').get('length')):
            try:
                var.put('spOutput', (Js(', ')+var.get('wiz5Prepared').get(var.get('x'))), '+')
            finally:
                    (var.put('x',Js(var.get('x').to_number())+Js(1))-Js(1))
    var.put('spOutput', var.get('cOutput'), '+')
    if (var.get('ciSpells').get('length')>Js(0.0)):
        var.put('spOutput', Js('==EOF==Druid Circle Spells: '), '+')
        #for JS loop
        var.put('x', Js(0.0))
        while (var.get('x')<var.get('ciSpells').get('length')):
            try:
                if (var.get('x')==Js(0.0)):
                    var.put('spOutput', var.get('ciSpells').get(var.get('x')), '+')
                else:
                    var.put('spOutput', (Js(', ')+var.get('ciSpells').get(var.get('x'))), '+')
            finally:
                    (var.put('x',Js(var.get('x').to_number())+Js(1))-Js(1))
    if (var.get('oaSpells').get('length')>Js(0.0)):
        var.put('spOutput', Js('==EOF==Paladin Oath Spells: '), '+')
        #for JS loop
        var.put('x', Js(0.0))
        while (var.get('x')<var.get('oaSpells').get('length')):
            try:
                if (var.get('x')==Js(0.0)):
                    var.put('spOutput', var.get('oaSpells').get(var.get('x')), '+')
                else:
                    var.put('spOutput', (Js(', ')+var.get('oaSpells').get(var.get('x'))), '+')
            finally:
                    (var.put('x',Js(var.get('x').to_number())+Js(1))-Js(1))
    if (var.get('loSpells').get('length')>Js(0.0)):
        var.put('spOutput', Js('==EOF==Bard Magical Secret Spells: '), '+')
        #for JS loop
        var.put('x', Js(0.0))
        while (var.get('x')<var.get('loSpells').get('length')):
            try:
                if (var.get('x')==Js(0.0)):
                    var.put('spOutput', var.get('loSpells').get(var.get('x')), '+')
                else:
                    var.put('spOutput', (Js(', ')+var.get('loSpells').get(var.get('x'))), '+')
            finally:
                    (var.put('x',Js(var.get('x').to_number())+Js(1))-Js(1))
    if (var.get('doSpells').get('length')>Js(0.0)):
        var.put('spOutput', Js('==EOF==Cleric Domain Spells: '), '+')
        #for JS loop
        var.put('x', Js(0.0))
        while (var.get('x')<var.get('doSpells').get('length')):
            try:
                if (var.get('x')==Js(0.0)):
                    var.put('spOutput', var.get('doSpells').get(var.get('x')), '+')
                else:
                    var.put('spOutput', (Js(', ')+var.get('doSpells').get(var.get('x'))), '+')
            finally:
                    (var.put('x',Js(var.get('x').to_number())+Js(1))-Js(1))
    if (var.get('waTome').get('length')>Js(0.0)):
        var.put('spOutput', Js('==EOF==<b>Warlock Tome Cantrips:</b> '), '+')
        #for JS loop
        var.put('x', Js(0.0))
        while (var.get('x')<var.get('waTome').get('length')):
            try:
                if (var.get('x')==Js(0.0)):
                    var.put('spOutput', var.get('waTome').get(var.get('x')), '+')
                else:
                    var.put('spOutput', (Js(', ')+var.get('waTome').get(var.get('x'))), '+')
            finally:
                    (var.put('x',Js(var.get('x').to_number())+Js(1))-Js(1))
        if (var.get('waTomeRituals').get('length')>Js(0.0)):
            var.put('spOutput', Js('   Tome Rituals: '), '+')
            #for JS loop
            var.put('x', Js(0.0))
            while (var.get('x')<var.get('waTomeRituals').get('length')):
                try:
                    if (var.get('x')==Js(0.0)):
                        var.put('spOutput', var.get('waTomeRituals').get(var.get('x')), '+')
                    else:
                        var.put('spOutput', (Js(', ')+var.get('waTomeRituals').get(var.get('x'))), '+')
                finally:
                        (var.put('x',Js(var.get('x').to_number())+Js(1))-Js(1))
    if (var.get('waSpells').get('length')>Js(0.0)):
        var.put('spOutput', Js('==EOF==Spells Given by Invocations: '), '+')
        #for JS loop
        var.put('x', Js(0.0))
        while (var.get('x')<var.get('waSpells').get('length')):
            try:
                if (var.get('x')==Js(0.0)):
                    var.put('spOutput', var.get('waSpells').get(var.get('x')), '+')
                else:
                    var.put('spOutput', (Js(', ')+var.get('waSpells').get(var.get('x'))), '+')
            finally:
                    (var.put('x',Js(var.get('x').to_number())+Js(1))-Js(1))
    if (var.get('ss1')>Js(0.0)):
        var.put('spOutput', (Js('==EOF==<b>Spell slots:</b>==EOF== ')+var.get('ss1')), '+')
        if (var.get('cl')!=Js(14.0)):
            var.put('spOutput', Js(' first level'), '+')
            if (var.get('ss2')>Js(0.0)):
                var.put('spOutput', ((Js(',==EOF== ')+var.get('ss2'))+Js(' second level')), '+')
            if (var.get('ss3')>Js(0.0)):
                var.put('spOutput', ((Js(',==EOF== ')+var.get('ss3'))+Js(' third level')), '+')
            if (var.get('ss4')>Js(0.0)):
                var.put('spOutput', ((Js(',==EOF== ')+var.get('ss4'))+Js(' fourth level')), '+')
            if (var.get('ss5')>Js(0.0)):
                var.put('spOutput', ((Js(',==EOF== ')+var.get('ss5'))+Js(' fifth level')), '+')
        if (var.get('cl')==Js(14.0)):
            if (var.get('level')<Js(3.0)):
                var.put('spOutput', Js(' first level'), '+')
            if ((var.get('level')>Js(2.0)) and (var.get('level')<Js(5.0))):
                var.put('spOutput', Js(' second level'), '+')
            if (var.get('level')>Js(8.0)):
                var.put('spOutput', Js(' fifth level'), '+')
            else:
                if (var.get('level')>Js(6.0)):
                    var.put('spOutput', Js(' fourth level'), '+')
                else:
                    if (var.get('level')>Js(4.0)):
                        var.put('spOutput', Js(' third level'), '+')
        var.put('spOutput', (((Js('==EOF==<b>Spell save DC:</b>  ')+((Js(8.0)+var.get('prof'))+var.get('mod').get(var.get('spellAbility'))))+Js('      <b>Spell Attack Modifier:</b>  '))+var.get('showPlus')((var.get('prof')+var.get('mod').get(var.get('spellAbility'))))), '+')
        if ((((var.get('cl')==Js(3.0)) or (var.get('cl')==Js(4.0))) or (var.get('cl')==Js(15.0))) or (var.get('cl')==Js(9.0))):
            var.put('spOutput', ((Js('      ==EOF==Can prepare ')+var.get('sp'))+Js(' spells')), '+')
        if ((((((var.get('cl')==Js(2.0)) or (var.get('cl')==Js(5.0))) or (var.get('cl')==Js(10.0))) or (var.get('cl')==Js(12.0))) or (var.get('cl')==Js(13.0))) or (var.get('cl')==Js(14.0))):
            var.put('spOutput', ((Js('      ==EOF==Knows ')+var.get('sp'))+Js(' spells')), '+')
    if (var.get('raceSpells').get('length')>Js(0.0)):
        if (var.get('spOutput').get('length')>Js(0.0)):
            var.put('spOutput', Js('==EOF=='), '+')
        var.put('spOutput', Js('<b>Race magic'), '+')
        var.put('spOutput', Js(':</b> '), '+')
        #for JS loop
        var.put('x', Js(0.0))
        while (var.get('x')<var.get('raceSpells').get('length')):
            try:
                if (var.get('x')==Js(0.0)):
                    var.put('spOutput', var.get('raceSpells').get(var.get('x')), '+')
                else:
                    var.put('spOutput', (Js(', ')+var.get('raceSpells').get(var.get('x'))), '+')
            finally:
                    (var.put('x',Js(var.get('x').to_number())+Js(1))-Js(1))
        var.put('spOutput', (((Js('     Spell save DC:  ')+((Js(8.0)+var.get('prof'))+var.get('mod').get(var.get('raceSpellAbility'))))+Js('      Spell Attack Modifier:  '))+var.get('showPlus')((var.get('prof')+var.get('mod').get(var.get('raceSpellAbility'))))), '+')
    while 1:
        SWITCHED = False
        CONDITION = (var.get('cl'))
        if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
            SWITCHED = True
            if (var.get('size')==Js('Small')):
                var.put('i', var.get('pickWeap')(Js([Js(11.0), Js(14.0), Js(19.0)])))
                var.get('myWp').callprop('push', var.get('weapons').get(var.get('i')))
            else:
                if (var.get('Math').callprop('random')>Js(0.5)):
                    var.put('i', Js(20.0))
                    var.get('myWp').callprop('push', var.get('weapons').get('20'))
                else:
                    var.put('i', var.get('pickWeap')(Js([Js(11.0), Js(12.0), Js(19.0)])))
                    var.get('myWp').callprop('push', var.get('weapons').get(var.get('i')))
            var.put('bool', Js(False))
            if ((var.get('i')!=Js(12.0)) and (var.get('i')!=Js(20.0))):
                var.put('bool', Js(True))
            if ((var.get('Math').callprop('random')>Js(0.75)) and (var.get('level')>Js(1.0))):
                var.get('myWp').callprop('push', var.get('weapons').get('3'))
                var.get('wpNum').put('3', (var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(3.0)))+Js(2.0)))
            else:
                if (var.get('level')>Js(1.0)):
                    var.put('y', var.get('pickWeap')(Js([Js(11.0), Js(14.0), Js(15.0), Js(19.0)])))
                    while (var.get('i')==var.get('y')):
                        var.put('y', var.get('pickWeap')(Js([Js(11.0), Js(14.0), Js(15.0), Js(19.0)])))
                    var.get('myWp').callprop('push', var.get('weapons').get(var.get('y')))
            if ((var.get('mod').get('1')>(-Js(1.0))) and (var.get('level')>Js(1.0))):
                if (var.get('size')==Js('Small')):
                    var.get('myWp').callprop('push', var.get('weapons').get('8'))
                else:
                    var.get('myWp').callprop('push', var.get('weapons').get('9'))
            else:
                var.get('myWp').callprop('push', var.get('weapons').get('4'))
                var.get('wpNum').put('4', Js(3.0))
                if (var.get('level')>Js(1.0)):
                    var.get('wpNum').put('4', (var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(5.0)))+Js(3.0)))
            if ((var.get('upgradeRare')()==Js(True)) and (var.get('mod').get('2')<Js(5.0))):
                var.get('myAr').callprop('push', var.get('armors').get('8'))
            else:
                if ((var.get('upgradeUncommon')()==Js(True)) and (var.get('mod').get('2')<Js(4.0))):
                    var.get('myAr').callprop('push', var.get('armors').get('7'))
                else:
                    if ((var.get('upgrade')()==Js(True)) and (var.get('mod').get('2')<Js(3.0))):
                        var.get('myAr').callprop('push', var.get('armors').get('5'))
            if ((var.get('bool')==Js(True)) and (var.get('upgrade')()==Js(True))):
                var.get('myAr').callprop('push', var.get('armors').get('0'))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
            SWITCHED = True
            if (var.get('mod').get('1')>var.get('mod').get('0')):
                var.get('myWp').callprop('push', var.get('weapons').get('16'))
            else:
                var.get('myWp').callprop('push', var.get('weapons').get('14'))
            if (var.get('elfBow')()==Js(False)):
                if (var.get('level')>Js(1.0)):
                    if ((var.get('classtxt').callprop('indexOf', Js('Valor'))>(-Js(1.0))) and (var.get('size')!=Js('Small'))):
                        if (var.get('Math').callprop('random')>Js(0.5)):
                            var.get('myWp').callprop('push', var.get('weapons').get('6'))
                        else:
                            var.get('myWp').callprop('push', var.get('weapons').get('9'))
                    else:
                        var.put('x', var.get('Math').callprop('random'))
                        if (var.get('x')>Js(0.5)):
                            var.get('myWp').callprop('push', var.get('weapons').get('5'))
                        else:
                            var.get('myWp').callprop('push', var.get('weapons').get('8'))
            var.get('myWp').callprop('push', var.get('weapons').get('0'))
            if (var.get('upgrade')()==Js(True)):
                var.get('wpNum').put('0', (var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(3.0)))+Js(3.0)))
            if (var.get('upgradeUncommon')()==Js(True)):
                var.get('myWp').callprop('push', var.get('weapons').get('7'))
            if (var.get('classtxt').callprop('indexOf', Js('Valor'))>(-Js(1.0))):
                var.get('myAr').callprop('push', var.get('armors').get('0'))
                if (var.get('upgradeUncommon')()==Js(True)):
                    var.get('myAr').callprop('push', var.get('armors').get('7'))
                else:
                    var.get('myAr').callprop('push', var.get('armors').get('5'))
            else:
                if ((var.get('racetxt')==Js('Mountain Dwarf')) and (var.get('level')>Js(1.0))):
                    if (var.get('upgradeUncommon')()==Js(True)):
                        var.get('myAr').callprop('push', var.get('armors').get('7'))
                    else:
                        var.get('myAr').callprop('push', var.get('armors').get('5'))
                else:
                    if ((var.get('upgrade')()==Js(True)) and (var.get('level')>Js(1.0))):
                        var.get('myAr').callprop('push', var.get('armors').get('3'))
                    else:
                        var.get('myAr').callprop('push', var.get('armors').get('2'))
            if (var.get('Math').callprop('random')<Js(0.5)):
                var.put('eqOutput', Js(", Diplomat's pack"), '+')
            else:
                var.put('eqOutput', Js(", Entertainer's pack"), '+')
            var.put('eqOutput', (Js(', ')+var.get('myInstrument')), '+')
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(3.0)):
            SWITCHED = True
            if (((((var.get('clDomain')==Js(1.0)) or (var.get('clDomain')==Js(3.0))) or (var.get('clDomain')==Js(4.0))) or (var.get('clDomain')==Js(6.0))) and (var.get('abil').get('0')>Js(12.0))):
                if (((var.get('upgradeUncommon')()==Js(True)) and (var.get('abil').get('0')>Js(14.0))) and (var.get('level')>Js(1.0))):
                    if (var.get('upgradeUncommon')()==Js(True)):
                        var.get('myAr').callprop('push', var.get('armors').get('12'))
                    else:
                        var.get('myAr').callprop('push', var.get('armors').get('11'))
                else:
                    var.get('myAr').callprop('push', var.get('armors').get('10'))
            else:
                if (var.get('racetxt')==Js('Mountain Dwarf')):
                    if ((var.get('upgradeUncommon')()==Js(True)) and (var.get('level')>Js(1.0))):
                        var.get('myAr').callprop('push', var.get('armors').get('7'))
                    else:
                        var.get('myAr').callprop('push', var.get('armors').get('6'))
                else:
                    if (var.get('upgrade')()==Js(True)):
                        var.get('myAr').callprop('push', var.get('armors').get('3'))
                    else:
                        var.get('myAr').callprop('push', var.get('armors').get('2'))
            if (((var.get('elfWeapon')()==Js(False)) and (var.get('dwarfWeapon')()==Js(False))) and (var.get('level')>Js(1.0))):
                if ((var.get('clDomain')==Js(4.0)) or (var.get('clDomain')==Js(6.0))):
                    if (var.get('abil').get('0')>var.get('abil').get('1')):
                        var.put('x', var.get('pickWeap')(Js([Js(11.0), Js(14.0), Js(15.0), Js(19.0)])))
                        var.get('myWp').callprop('push', var.get('weapons').get(var.get('x')))
                    else:
                        var.put('x', var.get('pickWeap')(Js([Js(17.0), Js(18.0)])))
                        var.get('myWp').callprop('push', var.get('weapons').get(var.get('x')))
                else:
                    var.get('myWp').callprop('push', var.get('weapons').get('1'))
                    var.put('x', var.get('pickWeap')(Js([Js(2.0), Js(3.0), Js(22.0)])))
                    var.get('myWp').callprop('push', var.get('weapons').get(var.get('x')))
            else:
                var.get('myWp').callprop('push', var.get('weapons').get('1'))
            if (var.get('level')==Js(1.0)):
                if (var.get('Math').callprop('random')>Js(0.5)):
                    var.put('x', var.get('pickWeap')(Js([Js(2.0), Js(3.0), Js(22.0)])))
                    var.get('myWp').callprop('push', var.get('weapons').get(var.get('x')))
                else:
                    var.get('myWp').callprop('push', var.get('weapons').get('5'))
            if (var.get('elfBow')()==Js(False)):
                if (var.get('level')>Js(1.0)):
                    if (((var.get('clDomain')==Js(4.0)) or (var.get('clDomain')==Js(6.0))) and (var.get('size')!=Js('Small'))):
                        if (var.get('Math').callprop('random')>Js(0.5)):
                            var.get('myWp').callprop('push', var.get('weapons').get('6'))
                        else:
                            var.get('myWp').callprop('push', var.get('weapons').get('9'))
                    else:
                        var.get('myWp').callprop('push', var.get('weapons').get('5'))
            var.get('myAr').callprop('push', var.get('armors').get('0'))
            if (var.get('eqOutput').callprop('indexOf', Js('Holy symbol'))==(-Js(1.0))):
                var.put('eqOutput', Js(', Holy symbol'), '+')
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(4.0)):
            SWITCHED = True
            if ((var.get('elfWeapon')()==Js(False)) and (var.get('dwarfWeapon')()==Js(False))):
                if (var.get('mod').get('0')<var.get('mod').get('1')):
                    var.get('myWp').callprop('push', var.get('weapons').get('17'))
                else:
                    var.put('x', var.get('pickWeap')(Js([Js(1.0), Js(2.0), Js(3.0), Js(22.0)])))
                    var.get('myWp').callprop('push', var.get('weapons').get(var.get('x')))
            if (((var.get('Math').callprop('random')>Js(0.5)) and (var.get('myCantrips').callprop('indexOf', Js('Shillelagh'))>(-Js(1.0)))) and (var.get('x')!=Js(22.0))):
                var.get('myWp').callprop('push', var.get('weapons').get('22'))
            if (var.get('elfBow')()==Js(False)):
                if (var.get('level')>Js(1.0)):
                    if (var.get('mod').get('1')>var.get('mod').get('0')):
                        if (var.get('Math').callprop('random')>Js(0.3)):
                            var.get('myWp').callprop('push', var.get('weapons').get('24'))
                        else:
                            var.get('myWp').callprop('push', var.get('weapons').get('21'))
                            var.get('wpNum').put('21', (var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(4.0)))+Js(8.0)))
                            if (var.get('upgrade')()==Js(True)):
                                var.get('myWp').callprop('push', var.get('weapons').get('24'))
                    else:
                        var.get('myWp').callprop('push', var.get('weapons').get('4'))
                        var.get('wpNum').put('4', (var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(3.0)))+Js(3.0)))
                else:
                    if (var.get('Math').callprop('random')>Js(0.3)):
                        var.get('myWp').callprop('push', var.get('weapons').get('24'))
                    else:
                        var.get('myWp').callprop('push', var.get('weapons').get('21'))
                        var.get('wpNum').put('21', Js(10.0))
            if (var.get('upgrade')()==Js(True)):
                var.get('myAr').callprop('push', var.get('armors').get('0'))
            if ((var.get('upgrade')()==Js(True)) and (var.get('mod').get('1')<Js(3.0))):
                var.get('myAr').callprop('push', var.get('armors').get('4'))
            else:
                var.get('myAr').callprop('push', var.get('armors').get('2'))
            var.put('eqOutput', Js(", Explorer's pack, Druidic focus"), '+')
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(5.0)):
            SWITCHED = True
            var.get('warriorArmor')()
            var.put('z', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(2.0))))
            if (var.get('fiStyle')==Js(3.0)):
                var.put('z', Js(0.0))
            if ((var.get('fiStyle')==Js(2.0)) or (var.get('fiStyle')==Js(4.0))):
                var.put('z', Js(1.0))
            if (var.get('fiStyle')==Js(5.0)):
                var.put('z', Js(2.0))
            var.get('console').callprop('log', (((Js('weapon choice:  ')+var.get('z'))+Js(' / fighting style: '))+var.get('fiStyle')))
            if ((var.get('z')==Js(0.0)) and (var.get('size')!=Js('Small'))):
                var.put('x', var.get('pickWeap')(Js([Js(13.0), Js(20.0), Js(12.0)])))
                var.get('myWp').callprop('push', var.get('weapons').get(var.get('x')))
            if ((var.get('z')==Js(0.0)) and (var.get('size')==Js('Small'))):
                var.put('x', var.get('pickWeap')(Js([Js(11.0), Js(14.0), Js(19.0)])))
                var.get('myWp').callprop('push', var.get('weapons').get(var.get('x')))
            if (var.get('z')==Js(1.0)):
                var.get('myAr').callprop('push', var.get('armors').get('0'))
                if (var.get('mod').get('1')<var.get('mod').get('0')):
                    var.put('x', var.get('pickWeap')(Js([Js(11.0), Js(14.0), Js(15.0), Js(19.0)])))
                    var.get('myWp').callprop('push', var.get('weapons').get(var.get('x')))
                else:
                    var.get('myWp').callprop('push', var.get('weapons').get('16'))
            if (var.get('z')==Js(2.0)):
                var.put('x', var.get('pickWeap')(Js([Js(17.0), Js(18.0)])))
                var.get('myWp').callprop('push', var.get('weapons').get(var.get('x')))
                var.get('wpNum').put(var.get('x'), Js(2.0))
            if (var.get('level')>Js(1.0)):
                var.put('x', var.get('pickWeap')(Js([Js(14.0), Js(2.0), Js(11.0)])))
                while (var.get('myWp').callprop('indexOf', var.get('weapons').get(var.get('x')))!=(-Js(1.0))):
                    var.put('x', var.get('pickWeap')(Js([Js(14.0), Js(2.0), Js(11.0)])))
                var.get('myWp').callprop('push', var.get('weapons').get(var.get('x')))
            var.put('x', var.get('Math').callprop('random'))
            if (var.get('x')<Js(0.6)):
                if (var.get('x')>Js(0.3)):
                    var.get('myWp').callprop('push', var.get('weapons').get('3'))
                    var.get('wpNum').put('3', Js(3.0))
                else:
                    var.get('myWp').callprop('push', var.get('weapons').get('4'))
                    var.get('wpNum').put('4', Js(3.0))
                    if (var.get('level')>Js(1.0)):
                        var.get('wpNum').put('4', (var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(3.0)))+Js(3.0)))
            if (var.get('size')==Js('Small')):
                if (var.get('Math').callprop('random')>Js(0.33)):
                    var.get('myWp').callprop('push', var.get('weapons').get('8'))
                else:
                    var.get('myWp').callprop('push', var.get('weapons').get('5'))
            else:
                if (var.get('Math').callprop('random')>Js(0.33)):
                    var.get('myWp').callprop('push', var.get('weapons').get('9'))
                else:
                    var.get('myWp').callprop('push', var.get('weapons').get('6'))
            if (var.get('Math').callprop('random')>Js(0.5)):
                var.put('eqOutput', Js(", Dungeoneer's pack"), '+')
            else:
                var.put('eqOutput', Js(", Explorer's pack"), '+')
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(6.0)):
            SWITCHED = True
            var.get('warriorArmor')()
            var.put('z', Js(1.0))
            if (var.get('fiStyle')==Js(5.0)):
                var.put('z', Js(2.0))
            if (var.get('z')==Js(1.0)):
                var.get('myAr').callprop('push', var.get('armors').get('0'))
                if (var.get('mod').get('1')<var.get('mod').get('0')):
                    var.put('x', var.get('pickWeap')(Js([Js(11.0), Js(14.0), Js(15.0), Js(19.0)])))
                    var.get('myWp').callprop('push', var.get('weapons').get(var.get('x')))
                else:
                    var.get('myWp').callprop('push', var.get('weapons').get('16'))
            if (var.get('z')==Js(2.0)):
                var.put('x', var.get('pickWeap')(Js([Js(17.0), Js(18.0)])))
                var.get('myWp').callprop('push', var.get('weapons').get(var.get('x')))
                var.get('wpNum').put(var.get('x'), Js(2.0))
            if (var.get('fiStyle2')==Js(5.0)):
                var.put('x', var.get('pickWeap')(Js([Js(17.0), Js(18.0)])))
                var.get('myWp').callprop('push', var.get('weapons').get(var.get('x')))
                var.get('wpNum').put(var.get('x'), Js(2.0))
            else:
                if (var.get('fiStyle2')==Js(3.0)):
                    if (var.get('size')!=Js('Small')):
                        var.put('x', var.get('pickWeap')(Js([Js(13.0), Js(20.0), Js(12.0)])))
                        var.get('myWp').callprop('push', var.get('weapons').get(var.get('x')))
                    else:
                        var.put('x', var.get('pickWeap')(Js([Js(11.0), Js(14.0), Js(19.0)])))
                        var.get('myWp').callprop('push', var.get('weapons').get(var.get('x')))
                else:
                    if (var.get('level')>Js(1.0)):
                        var.put('x', var.get('pickWeap')(Js([Js(14.0), Js(2.0), Js(11.0)])))
                        while (var.get('myWp').callprop('indexOf', var.get('weapons').get(var.get('x')))!=(-Js(1.0))):
                            var.put('x', var.get('pickWeap')(Js([Js(14.0), Js(2.0), Js(11.0)])))
                        var.get('myWp').callprop('push', var.get('weapons').get(var.get('x')))
            var.put('x', var.get('Math').callprop('random'))
            if (var.get('x')<Js(0.6)):
                if (var.get('x')>Js(0.3)):
                    var.get('myWp').callprop('push', var.get('weapons').get('3'))
                    var.get('wpNum').put('3', Js(3.0))
                else:
                    var.get('myWp').callprop('push', var.get('weapons').get('4'))
                    var.get('wpNum').put('4', Js(3.0))
                    if (var.get('level')>Js(1.0)):
                        var.get('wpNum').put('4', (var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(3.0)))+Js(3.0)))
            if (var.get('size')==Js('Small')):
                if (var.get('Math').callprop('random')>Js(0.33)):
                    var.get('myWp').callprop('push', var.get('weapons').get('8'))
                else:
                    var.get('myWp').callprop('push', var.get('weapons').get('5'))
            else:
                if (var.get('Math').callprop('random')>Js(0.33)):
                    var.get('myWp').callprop('push', var.get('weapons').get('9'))
                else:
                    var.get('myWp').callprop('push', var.get('weapons').get('6'))
            if (var.get('Math').callprop('random')>Js(0.5)):
                var.put('eqOutput', Js(", Dungeoneer's pack"), '+')
            else:
                var.put('eqOutput', Js(", Explorer's pack"), '+')
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(7.0)):
            SWITCHED = True
            var.get('warriorArmor')()
            var.put('z', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(2.0))))
            if (var.get('fiStyle')==Js(3.0)):
                var.put('z', Js(0.0))
            if ((var.get('fiStyle')==Js(2.0)) or (var.get('fiStyle')==Js(4.0))):
                var.put('z', Js(1.0))
            if (var.get('fiStyle')==Js(5.0)):
                var.put('z', Js(2.0))
            var.get('console').callprop('log', (((Js('weapon choice:  ')+var.get('z'))+Js(' / fighting style: '))+var.get('fiStyle')))
            if ((var.get('z')==Js(0.0)) and (var.get('size')!=Js('Small'))):
                var.put('x', var.get('pickWeap')(Js([Js(13.0), Js(20.0), Js(12.0)])))
                var.get('myWp').callprop('push', var.get('weapons').get(var.get('x')))
            if ((var.get('z')==Js(0.0)) and (var.get('size')==Js('Small'))):
                var.put('x', var.get('pickWeap')(Js([Js(11.0), Js(14.0), Js(19.0)])))
                var.get('myWp').callprop('push', var.get('weapons').get(var.get('x')))
            if (var.get('z')==Js(1.0)):
                var.get('myAr').callprop('push', var.get('armors').get('0'))
                if (var.get('mod').get('1')<var.get('mod').get('0')):
                    var.put('x', var.get('pickWeap')(Js([Js(11.0), Js(14.0), Js(15.0), Js(19.0)])))
                    var.get('myWp').callprop('push', var.get('weapons').get(var.get('x')))
                else:
                    var.get('myWp').callprop('push', var.get('weapons').get('16'))
            else:
                if ((var.get('fiStyle2')==Js(2.0)) or (var.get('fiStyle2')==Js(4.0))):
                    pass
            if (var.get('z')==Js(2.0)):
                var.put('x', var.get('pickWeap')(Js([Js(17.0), Js(18.0)])))
                var.get('myWp').callprop('push', var.get('weapons').get(var.get('x')))
                var.get('wpNum').put(var.get('x'), Js(2.0))
            if (var.get('fiStyle2')==Js(5.0)):
                var.put('x', var.get('pickWeap')(Js([Js(17.0), Js(18.0)])))
                var.get('myWp').callprop('push', var.get('weapons').get(var.get('x')))
                var.get('wpNum').put(var.get('x'), Js(2.0))
            else:
                if (var.get('fiStyle2')==Js(3.0)):
                    if (var.get('size')!=Js('Small')):
                        var.put('x', var.get('pickWeap')(Js([Js(13.0), Js(20.0), Js(12.0)])))
                        var.get('myWp').callprop('push', var.get('weapons').get(var.get('x')))
                    else:
                        var.put('x', var.get('pickWeap')(Js([Js(11.0), Js(14.0), Js(19.0)])))
                        var.get('myWp').callprop('push', var.get('weapons').get(var.get('x')))
                else:
                    if (var.get('level')>Js(1.0)):
                        var.put('x', var.get('pickWeap')(Js([Js(14.0), Js(2.0), Js(11.0)])))
                        while (var.get('myWp').callprop('indexOf', var.get('weapons').get(var.get('x')))!=(-Js(1.0))):
                            var.put('x', var.get('pickWeap')(Js([Js(14.0), Js(2.0), Js(11.0)])))
                        var.get('myWp').callprop('push', var.get('weapons').get(var.get('x')))
            var.put('x', var.get('Math').callprop('random'))
            if (var.get('x')<Js(0.6)):
                if (var.get('x')>Js(0.3)):
                    var.get('myWp').callprop('push', var.get('weapons').get('3'))
                    var.get('wpNum').put('3', Js(3.0))
                else:
                    var.get('myWp').callprop('push', var.get('weapons').get('4'))
                    var.get('wpNum').put('4', Js(3.0))
                    if (var.get('level')>Js(1.0)):
                        var.get('wpNum').put('4', (var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(3.0)))+Js(3.0)))
            if (var.get('size')==Js('Small')):
                if (var.get('Math').callprop('random')>Js(0.33)):
                    var.get('myWp').callprop('push', var.get('weapons').get('8'))
                else:
                    var.get('myWp').callprop('push', var.get('weapons').get('5'))
            else:
                if (var.get('Math').callprop('random')>Js(0.33)):
                    var.get('myWp').callprop('push', var.get('weapons').get('9'))
                else:
                    var.get('myWp').callprop('push', var.get('weapons').get('6'))
            if (var.get('Math').callprop('random')>Js(0.5)):
                var.put('eqOutput', Js(", Dungeoneer's pack"), '+')
            else:
                var.put('eqOutput', Js(", Explorer's pack"), '+')
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(8.0)):
            SWITCHED = True
            var.get('myWp').callprop('push', var.get('weapons').get('23'))
            if (var.get('Math').callprop('random')>Js(0.5)):
                var.get('myWp').callprop('push', var.get('weapons').get('18'))
            else:
                var.put('x', var.get('pickWeap')(Js([Js(2.0), Js(22.0), Js(3.0)])))
                var.get('myWp').callprop('push', var.get('weapons').get(var.get('x')))
            if (var.get('Math').callprop('random')>Js(0.5)):
                var.put('eqOutput', Js(", Dungeoneer's pack"), '+')
            else:
                var.put('eqOutput', Js(", Explorer's pack"), '+')
            if (var.get('elfBow')()==Js(False)):
                var.put('x', var.get('Math').callprop('random'))
                if ((var.get('x')>Js(0.8)) or (var.get('level')==Js(1.0))):
                    var.get('myWp').callprop('push', var.get('weapons').get('21'))
                    var.get('wpNum').put('21', Js(10.0))
                else:
                    var.put('x', var.get('pickWeap')(Js([Js(5.0), Js(8.0)])))
                    var.get('myWp').callprop('push', var.get('weapons').get(var.get('x')))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(9.0)):
            SWITCHED = True
            if ((var.get('abil').get('0')>Js(14.0)) and (var.get('level')>Js(1.0))):
                if (var.get('upgradeRare')()==Js(True)):
                    var.get('myAr').callprop('push', var.get('armors').get('12'))
                else:
                    if (var.get('upgradeUncommon')()==Js(True)):
                        var.get('myAr').callprop('push', var.get('armors').get('11'))
            if ((var.get('abil').get('0')>Js(12.0)) and (var.get('myAr').get('length')==Js(0.0))):
                var.get('myAr').callprop('push', var.get('armors').get('10'))
            else:
                if (var.get('myAr').get('length')==Js(0.0)):
                    var.get('myAr').callprop('push', var.get('armors').get('9'))
            var.put('z', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(3.0))))
            if (var.get('fiStyle')==Js(3.0)):
                var.put('z', Js(0.0))
            if ((var.get('fiStyle')==Js(2.0)) or (var.get('fiStyle')==Js(4.0))):
                var.put('z', Js(1.0))
            if (var.get('fiStyle')==Js(5.0)):
                var.put('z', Js(2.0))
            if ((var.get('z')==Js(0.0)) and (var.get('size')!=Js('Small'))):
                var.put('x', var.get('pickWeap')(Js([Js(13.0), Js(20.0), Js(12.0)])))
                var.get('myWp').callprop('push', var.get('weapons').get(var.get('x')))
            if ((var.get('z')==Js(0.0)) and (var.get('size')==Js('Small'))):
                var.put('x', var.get('pickWeap')(Js([Js(11.0), Js(14.0), Js(19.0)])))
                var.get('myWp').callprop('push', var.get('weapons').get(var.get('x')))
            if (var.get('z')==Js(1.0)):
                var.get('myAr').callprop('push', var.get('armors').get('0'))
                if (var.get('mod').get('1')<var.get('mod').get('0')):
                    var.put('x', var.get('pickWeap')(Js([Js(11.0), Js(14.0), Js(15.0), Js(19.0)])))
                    var.get('myWp').callprop('push', var.get('weapons').get(var.get('x')))
                else:
                    var.get('myWp').callprop('push', var.get('weapons').get('16'))
            if (var.get('z')==Js(2.0)):
                var.put('x', var.get('pickWeap')(Js([Js(17.0), Js(18.0)])))
                var.get('myWp').callprop('push', var.get('weapons').get(var.get('x')))
                var.get('wpNum').put(var.get('x'), Js(2.0))
            if ((var.get('mod').get('1')<var.get('mod').get('0')) and (var.get('Math').callprop('random')<Js(0.66))):
                var.put('x', (var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(4.0)))+Js(3.0)))
                if (var.get('Math').callprop('random')>Js(0.5)):
                    var.get('myWp').callprop('push', var.get('weapons').get('4'))
                    var.get('wpNum').put('4', var.get('x'))
                else:
                    var.get('myWp').callprop('push', var.get('weapons').get('3'))
                    var.get('wpNum').put('3', var.get('x'))
            else:
                if (var.get('size')==Js('Small')):
                    if (var.get('Math').callprop('random')>Js(0.33)):
                        var.get('myWp').callprop('push', var.get('weapons').get('8'))
                    else:
                        var.get('myWp').callprop('push', var.get('weapons').get('5'))
                else:
                    if (var.get('Math').callprop('random')>Js(0.33)):
                        var.get('myWp').callprop('push', var.get('weapons').get('9'))
                    else:
                        var.get('myWp').callprop('push', var.get('weapons').get('6'))
            if (var.get('level')>Js(1.0)):
                var.put('x', var.get('pickWeap')(Js([Js(14.0), Js(2.0), Js(11.0), Js(15.0)])))
                while (var.get('myWp').callprop('indexOf', var.get('weapons').get(var.get('x')))!=(-Js(1.0))):
                    var.put('x', var.get('pickWeap')(Js([Js(14.0), Js(2.0), Js(11.0), Js(15.0)])))
                var.get('myWp').callprop('push', var.get('weapons').get(var.get('x')))
            if (var.get('Math').callprop('random')>Js(0.5)):
                var.put('eqOutput', Js(", Priest's pack"), '+')
            else:
                var.put('eqOutput', Js(", Explorer's pack"), '+')
            var.put('eqOutput', Js(', Holy symbol'), '+')
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(10.0)):
            SWITCHED = True
            if (var.get('size')==Js('Small')):
                var.get('myWp').callprop('push', var.get('weapons').get('8'))
            else:
                var.get('myWp').callprop('push', var.get('weapons').get('9'))
            if (((var.get('mod').get('1')<Js(3.0)) and (var.get('mod').get('1')>Js(0.0))) and (var.get('level')>Js(1.0))):
                if (var.get('upgrade')()==Js(True)):
                    if (var.get('upgrade')()==Js(True)):
                        if (var.get('skLearn').get('16')==Js(True)):
                            var.get('myAr').callprop('push', var.get('armors').get('7'))
                        else:
                            var.get('myAr').callprop('push', var.get('armors').get('8'))
                    else:
                        var.get('myAr').callprop('push', var.get('armors').get('7'))
                else:
                    if (var.get('skLearn').get('16')==Js(True)):
                        var.get('myAr').callprop('push', var.get('armors').get('5'))
                    else:
                        var.get('myAr').callprop('push', var.get('armors').get('6'))
            else:
                if (var.get('upgrade')()==Js(True)):
                    var.get('myAr').callprop('push', var.get('armors').get('3'))
                else:
                    var.get('myAr').callprop('push', var.get('armors').get('2'))
            if (var.get('Math').callprop('random')>Js(0.5)):
                var.put('eqOutput', Js(", Dungeoneer's pack"), '+')
            else:
                var.put('eqOutput', Js(", Explorer's pack"), '+')
            var.put('z', var.get('Math').callprop('floor', ((var.get('Math').callprop('random')*Js(2.0))+Js(1.0))))
            if ((var.get('fiStyle')==Js(2.0)) or (var.get('fiStyle')==Js(4.0))):
                var.put('z', Js(1.0))
            if (var.get('fiStyle')==Js(5.0)):
                var.put('z', Js(2.0))
            if (var.get('level')>Js(1.0)):
                if (var.get('z')==Js(1.0)):
                    if (var.get('mod').get('1')<var.get('mod').get('0')):
                        var.put('x', var.get('pickWeap')(Js([Js(11.0), Js(14.0), Js(15.0), Js(19.0)])))
                        var.get('myWp').callprop('push', var.get('weapons').get(var.get('x')))
                    else:
                        var.put('x', var.get('pickWeap')(Js([Js(16.0), Js(16.0), Js(17.0), Js(18.0)])))
                        var.get('myWp').callprop('push', var.get('weapons').get(var.get('x')))
                    var.put('x', var.get('pickWeap')(Js([Js(14.0), Js(2.0), Js(11.0)])))
                    while (var.get('myWp').callprop('indexOf', var.get('weapons').get(var.get('x')))!=(-Js(1.0))):
                        var.put('x', var.get('pickWeap')(Js([Js(14.0), Js(2.0), Js(11.0)])))
                    var.get('myWp').callprop('push', var.get('weapons').get(var.get('x')))
            else:
                if (var.get('mod').get('1')<var.get('mod').get('0')):
                    var.put('x', var.get('pickWeap')(Js([Js(16.0), Js(16.0), Js(17.0), Js(18.0)])))
                    var.get('myWp').callprop('push', var.get('weapons').get(var.get('x')))
                else:
                    if (var.get('z')!=Js(2.0)):
                        var.put('x', var.get('pickWeap')(Js([Js(16.0), Js(17.0), Js(18.0)])))
                        var.get('myWp').callprop('push', var.get('weapons').get(var.get('x')))
            if (var.get('z')==Js(2.0)):
                var.put('x', var.get('pickWeap')(Js([Js(17.0), Js(18.0)])))
                var.get('myWp').callprop('push', var.get('weapons').get(var.get('x')))
                var.get('wpNum').put(var.get('x'), Js(2.0))
            if ((var.get('z')!=Js(2.0)) and (var.get('level')>Js(1.0))):
                var.get('myAr').callprop('push', var.get('armors').get('0'))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(11.0)):
            SWITCHED = True
            if (var.get('Math').callprop('random')>Js(0.5)):
                var.get('myWp').callprop('push', var.get('weapons').get('16'))
            else:
                var.get('myWp').callprop('push', var.get('weapons').get('18'))
            if (var.get('upgrade')()==Js(True)):
                var.get('myAr').callprop('push', var.get('armors').get('3'))
            else:
                var.get('myAr').callprop('push', var.get('armors').get('2'))
            if (var.get('elfBow')()==Js(False)):
                var.get('myWp').callprop('push', var.get('weapons').get('8'))
            if (var.get('upgradeUncommon')()==Js(True)):
                var.get('myWp').callprop('push', var.get('weapons').get('7'))
            var.get('myWp').callprop('push', var.get('weapons').get('0'))
            var.get('wpNum').put('0', Js(2.0))
            if (var.get('upgrade')()==Js(True)):
                var.get('wpNum').put('0', (var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(2.0)))+Js(3.0)))
            var.put('x', var.get('Math').callprop('random'))
            if (var.get('x')>Js(0.66)):
                var.put('eqOutput', Js(", Dungeoneer's pack"), '+')
            else:
                if (var.get('x')>Js(0.33)):
                    var.put('eqOutput', Js(", Explorer's pack"), '+')
                else:
                    var.put('eqOutput', Js(", Burglar's pack"), '+')
            var.put('eqOutput', Js(", Thieves' tools"), '+')
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(12.0)):
            SWITCHED = True
            if (var.get('Math').callprop('random')>Js(0.5)):
                var.get('myWp').callprop('push', var.get('weapons').get('16'))
            else:
                var.get('myWp').callprop('push', var.get('weapons').get('18'))
            if (var.get('elfBow')()==Js(False)):
                var.get('myWp').callprop('push', var.get('weapons').get('8'))
            if (var.get('upgradeUncommon')()==Js(True)):
                var.get('myWp').callprop('push', var.get('weapons').get('7'))
            if (var.get('upgrade')()==Js(True)):
                var.get('myAr').callprop('push', var.get('armors').get('3'))
            else:
                var.get('myAr').callprop('push', var.get('armors').get('2'))
            var.get('myWp').callprop('push', var.get('weapons').get('0'))
            var.get('wpNum').put('0', Js(2.0))
            if (var.get('upgrade')()==Js(True)):
                var.get('wpNum').put('0', (var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(2.0)))+Js(3.0)))
            var.put('x', var.get('Math').callprop('random'))
            if (var.get('x')>Js(0.66)):
                var.put('eqOutput', Js(", Dungeoneer's pack"), '+')
            else:
                if (var.get('x')>Js(0.33)):
                    var.put('eqOutput', Js(", Explorer's pack"), '+')
                else:
                    var.put('eqOutput', Js(", Burglar's pack"), '+')
            var.put('eqOutput', Js(", Thieves' tools"), '+')
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(13.0)):
            SWITCHED = True
            if ((var.get('elfWeapon')()==Js(False)) and (var.get('dwarfWeapon')()==Js(False))):
                if (var.get('mod').get('1')>var.get('mod').get('0')):
                    var.put('x', var.get('pickWeap')(Js([Js(22.0)])))
                    var.get('myWp').callprop('push', var.get('weapons').get(var.get('x')))
            var.get('myWp').callprop('push', var.get('weapons').get('0'))
            var.get('wpNum').put('0', Js(2.0))
            if (var.get('upgrade')()==Js(True)):
                var.get('wpNum').put('0', (var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(2.0)))+Js(3.0)))
            if (var.get('elfBow')()==Js(False)):
                var.put('x', var.get('Math').callprop('random'))
                if (var.get('x')>Js(0.75)):
                    var.get('wpNum').put('0', (var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(3.0)))+Js(4.0)))
                else:
                    if (var.get('x')>Js(0.25)):
                        var.get('myWp').callprop('push', var.get('weapons').get('5'))
                    else:
                        var.get('myWp').callprop('push', var.get('weapons').get('21'))
                        var.get('wpNum').put('21', (var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(3.0)))+Js(9.0)))
            var.get('dwarfMagicArmor')()
            if (var.get('Math').callprop('random')>Js(0.5)):
                var.put('eqOutput', Js(", Dungeoneer's pack"), '+')
            else:
                var.put('eqOutput', Js(", Explorer's pack"), '+')
            if (var.get('Math').callprop('random')>Js(0.5)):
                var.put('eqOutput', Js(', Component pouch'), '+')
                if (var.get('upgrade')()==Js(True)):
                    var.put('eqOutput', Js(', Arcane focus'), '+')
            else:
                var.put('eqOutput', Js(', Arcane focus'), '+')
                if (var.get('upgrade')()==Js(True)):
                    var.put('eqOutput', Js(', Component pouch'), '+')
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(14.0)):
            SWITCHED = True
            if ((var.get('elfWeapon')()==Js(False)) and (var.get('dwarfWeapon')()==Js(False))):
                var.put('x', var.get('pickWeap')(Js([Js(1.0), Js(2.0), Js(2.0), Js(3.0), Js(22.0)])))
                var.get('myWp').callprop('push', var.get('weapons').get(var.get('x')))
            if (var.get('elfBow')()==Js(False)):
                var.put('z', var.get('Math').callprop('random'))
                if (var.get('z')>Js(0.5)):
                    var.get('myWp').callprop('push', var.get('weapons').get('5'))
                else:
                    var.get('myWp').callprop('push', var.get('weapons').get('8'))
            var.get('myWp').callprop('push', var.get('weapons').get('0'))
            var.get('wpNum').put('0', Js(2.0))
            if (var.get('upgrade')()==Js(True)):
                var.get('wpNum').put('0', (var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(3.0)))+Js(3.0)))
            if (var.get('dwarfMagicArmor')()==Js(False)):
                if ((var.get('upgrade')()==Js(True)) and (var.get('level')>Js(1.0))):
                    var.get('myAr').callprop('push', var.get('armors').get('3'))
                else:
                    var.get('myAr').callprop('push', var.get('armors').get('2'))
            if (var.get('Math').callprop('random')>Js(0.5)):
                var.put('eqOutput', Js(", Dungeoneer's pack"), '+')
            else:
                var.put('eqOutput', Js(", Scholar's pack"), '+')
            if (var.get('Math').callprop('random')>Js(0.5)):
                var.put('eqOutput', Js(', Component pouch'), '+')
                if (var.get('upgrade')()==Js(True)):
                    var.put('eqOutput', Js(', Arcane focus'), '+')
            else:
                var.put('eqOutput', Js(', Arcane focus'), '+')
                if (var.get('upgrade')()==Js(True)):
                    var.put('eqOutput', Js(', Component pouch'), '+')
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(15.0)):
            SWITCHED = True
            if ((var.get('elfWeapon')()==Js(False)) and (var.get('dwarfWeapon')()==Js(False))):
                if (var.get('mod').get('1')>var.get('mod').get('0')):
                    var.get('myWp').callprop('push', var.get('weapons').get('0'))
                    if (var.get('level')>Js(1.0)):
                        var.get('wpNum').put('0', Js(2.0))
                else:
                    var.get('myWp').callprop('push', var.get('weapons').get('22'))
            if (var.get('elfBow')()==Js(False)):
                var.put('x', var.get('Math').callprop('random'))
                if (var.get('x')>Js(0.75)):
                    if (var.get('myWp').callprop('indexOf', Js('Dagger'))==(-Js(1.0))):
                        var.get('myWp').callprop('push', var.get('weapons').get('0'))
                    var.get('wpNum').put('0', (var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(3.0)))+Js(4.0)))
                else:
                    if (var.get('x')>Js(0.25)):
                        var.get('myWp').callprop('push', var.get('weapons').get('5'))
                    else:
                        var.get('myWp').callprop('push', var.get('weapons').get('21'))
                        var.get('wpNum').put('21', (var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(3.0)))+Js(9.0)))
            var.get('dwarfMagicArmor')()
            if (var.get('Math').callprop('random')>Js(0.5)):
                var.put('eqOutput', Js(", Explorer's pack"), '+')
            else:
                var.put('eqOutput', Js(", Scholar's pack"), '+')
            if (var.get('Math').callprop('random')>Js(0.5)):
                var.put('eqOutput', Js(', Component pouch'), '+')
                if (var.get('upgrade')()==Js(True)):
                    var.put('eqOutput', Js(', Arcane focus'), '+')
            else:
                var.put('eqOutput', Js(', Arcane focus'), '+')
                if (var.get('upgrade')()==Js(True)):
                    var.put('eqOutput', Js(', Component pouch'), '+')
            var.put('eqOutput', Js(', Spellbook'), '+')
            break
        SWITCHED = True
        break
    if (var.get('racetxt')==Js('Drow Elf')):
        if ((var.get('upgradeUncommon')()==Js(True)) and (var.get('myWp').callprop('indexOf', Js('Hand crossbow'))==(-Js(1.0)))):
            var.get('myWp').callprop('push', var.get('weapons').get('7'))
    var.put('x', Js(5.0))
    if ((var.get('cl')==Js(1.0)) or (var.get('cl')==Js(4.0))):
        var.put('x', Js(2.0))
    if (var.get('cl')>Js(10.0)):
        var.put('x', Js(4.0))
    if (var.get('cl')==Js(13.0)):
        var.put('x', Js(3.0))
    var.put('sum', Js(0.0))
    #for JS loop
    var.put('i', Js(1.0))
    while (var.get('i')<=var.get('x')):
        try:
            var.put('sum', var.get('Math').callprop('floor', ((var.get('Math').callprop('random')*Js(4.0))+Js(1.0))), '+')
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    if (var.get('cl')!=Js(8.0)):
        var.put('sum', (var.get('sum')*Js(10.0)))
    var.put('gold', var.get('sum'), '+')
    if (var.get('al')==Js(True)):
        var.put('gold', (var.get('x')*Js(40.0)))
        if (var.get('cl')==Js(8.0)):
            var.put('gold', Js(20.0))
    var.put('golddebug', Js([]))
    var.get('golddebug').callprop('unshift', var.get('gold'))
    var.put('x', (var.get('level')-Js(1.0)))
    while (var.get('x')>Js(0.0)):
        var.put('i', var.get('Math').callprop('random'))
        if (var.get('i')<Js(0.2)):
            var.put('gold', (var.get('gold')*((var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(3.0)))+Js(7.0))*Js(0.1))))
        else:
            var.put('gold', (var.get('gold')*((var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(6.0)))+Js(12.0))*Js(0.1))))
        var.put('gold', var.get('Math').callprop('floor', var.get('gold')))
        var.get('golddebug').callprop('push', var.get('gold'))
        (var.put('x',Js(var.get('x').to_number())-Js(1))+Js(1))
    if ((var.get('upgrade')()==Js(True)) and (var.get('gold')>Js(250.0))):
        var.put('x', ((var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(3.0)))+Js(7.0))*Js(0.1)))
        var.put('platinum', var.get('Math').callprop('floor', ((var.get('gold')*var.get('x'))/Js(10.0))))
        var.put('gold', var.get('Math').callprop('floor', (var.get('gold')*(Js(1.0)-var.get('x')))))
    var.put('weOutput', ((Js('==EOF==<b>Wealth:</b> ')+var.get('gold'))+Js(' gp')), '+')
    if (var.get('platinum')>Js(0.0)):
        var.put('weOutput', ((Js(', ')+var.get('platinum'))+Js(' pp')), '+')
    var.get('console').callprop('log', ((((Js('Gold at 1st level = ')+var.get('sum'))+Js(')(history = '))+var.get('golddebug'))+Js(')')))
    var.get('console').callprop('log', (((Js('final gold=')+var.get('gold'))+Js(' final platinum ='))+var.get('platinum')))
    if (var.get('cl')!=Js(8.0)):
        if (var.get('upgrade')()==Js(True)):
            var.put('x', ((var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(20.0)))+Js(1.0))+(var.get('level')*Js(2.0))))
            var.put('z', Js(0.0))
            if (var.get('x')>Js(37.0)):
                var.put('z', Js(4.0))
            else:
                if (var.get('x')>Js(29.0)):
                    var.put('z', Js(3.0))
                else:
                    if (var.get('x')>Js(23.0)):
                        var.put('z', Js(2.0))
                    else:
                        var.put('z', Js(1.0))
            var.get('console').callprop('log', ((((Js('extra wealth rolls:  x=')+var.get('x'))+Js(' / z='))+var.get('z'))+Js(' items')))
            var.put('bool', Js(False))
            while (var.get('z')>Js(0.0)):
                var.put('i', Js(0.0))
                var.put('y', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(4.0))))
                if (var.get('x')>Js(29.0)):
                    (var.put('y',Js(var.get('y').to_number())-Js(1))+Js(1))
                if (var.get('x')>Js(36.0)):
                    (var.put('y',Js(var.get('y').to_number())-Js(1))+Js(1))
                var.put('x', Js(0.0))
                if (var.get('level')>Js(7.0)):
                    (var.put('y',Js(var.get('y').to_number())-Js(1))+Js(1))
                if (var.get('y')<Js(0.0)):
                    var.put('y', Js(0.0))
                if (var.get('y')==Js(0.0)):
                    if (var.get('upgradeRare')()==Js(True)):
                        if (var.get('upgradeRare')()==Js(True)):
                            var.put('i', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(7.0))))
                            var.put('i', ((var.get('i')*Js(100.0))+Js(400.0)))
                            var.put('tempTxt', ((var.get('jewelryAdjectivesRare').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('jewelryAdjectivesRare').get('length'))))+Js(' '))+var.get('jewelryRare').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('jewelryRare').get('length'))))))
                            var.put('weOutput', ((((Js(', ')+var.get('tempTxt'))+Js(' worth '))+var.get('i'))+Js(' gold')), '+')
                            (var.put('z',Js(var.get('z').to_number())-Js(1))+Js(1))
                        else:
                            var.put('x', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(7.0))))
                            var.put('i', ((var.get('i')*Js(50.0))+Js(300.0)))
                            var.put('tempTxt', ((var.get('jewelryAdjectives').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('jewelryAdjectives').get('length'))))+Js(' '))+var.get('jewelry').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('jewelry').get('length'))))))
                            var.put('weOutput', ((((Js(', ')+var.get('tempTxt'))+Js(' worth '))+var.get('i'))+Js(' gold')), '+')
                            (var.put('z',Js(var.get('z').to_number())-Js(1))+Js(1))
                if (var.get('y')==Js(1.0)):
                    if (var.get('upgradeRare')()==Js(True)):
                        var.put('i', (var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(8.0)))+Js(4.0)))
                        var.put('i', ((var.get('i')*Js(50.0))+Js(50.0)))
                        var.put('weOutput', ((Js(', Gem worth ')+var.get('i'))+Js(' gold')), '+')
                        (var.put('z',Js(var.get('z').to_number())-Js(1))+Js(1))
                if (var.get('y')==Js(2.0)):
                    if (var.get('upgradeUncommon')()==Js(True)):
                        if ((var.get('Math').callprop('random')>Js(0.5)) and (var.get('bool')==Js(False))):
                            var.put('q', (var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(3.0)))+Js(2.0)))
                            var.put('i', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(7.0))))
                            var.put('i', ((var.get('i')*Js(20.0))+Js(120.0)))
                            var.put('weOutput', ((((Js(', ')+var.get('q'))+Js(' small gemstones  worth '))+var.get('i'))+Js(' gold')), '+')
                            (var.put('z',Js(var.get('z').to_number())-Js(1))+Js(1))
                            var.put('bool', Js(True))
                        else:
                            var.put('x', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(4.0))))
                            var.put('i', ((var.get('i')*Js(50.0))+Js(150.0)))
                            var.put('tempTxt', ((var.get('jewelryAdjectives').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('jewelryAdjectives').get('length'))))+Js(' '))+var.get('jewelry').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('jewelry').get('length'))))))
                            var.put('weOutput', ((((Js(', ')+var.get('tempTxt'))+Js(' worth '))+var.get('i'))+Js(' gold')), '+')
                            (var.put('z',Js(var.get('z').to_number())-Js(1))+Js(1))
                if (var.get('y')==Js(3.0)):
                    if (var.get('upgrade')()==Js(True)):
                        var.put('i', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(7.0))))
                        var.put('i', ((var.get('i')*Js(10.0))+Js(50.0)))
                        var.put('tempTxt', var.get('valuables').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('valuables').get('length')))))
                        var.put('weOutput', ((((Js(', ')+var.get('tempTxt'))+Js(' worth '))+var.get('i'))+Js(' gold')), '+')
                        (var.put('z',Js(var.get('z').to_number())-Js(1))+Js(1))
    if ((var.get('level')>Js(1.0)) and ((var.get('cl')==Js(9.0)) or (var.get('cl')==Js(3.0)))):
        if (var.get('upgrade')()==Js(True)):
            if (var.get('upgradeUncommon')()==Js(True)):
                var.put('x', (var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(2.0)))+Js(2.0)))
                var.put('eqOutput', ((Js(', ')+var.get('x'))+Js(' Flasks of Holy Water')), '+')
            else:
                var.put('eqOutput', Js(', Flask of Holy Water'), '+')
        if (var.get('upgradeUncommon')()==Js(True)):
            var.put('eqOutput', Js(', Vial of Antitoxin'), '+')
    else:
        if (var.get('level')>Js(1.0)):
            if (var.get('upgradeUncommon')()==Js(True)):
                var.put('eqOutput', Js(', Flask of Holy Water'), '+')
            if (var.get('upgradeRare')()==Js(True)):
                var.put('eqOutput', Js(', Vial of Antitoxin'), '+')
    if (var.get('upgradeUncommon')()==Js(True)):
        var.put('eqOutput', Js(", Healer's kit"), '+')
    if (var.get('level')>Js(1.0)):
        if (var.get('upgradeRare')()==Js(True)):
            var.put('eqOutput', Js(", Flask of Alchemist's Fire"), '+')
        if (var.get('upgradeUncommon')()==Js(True)):
            var.put('eqOutput', Js(', Vial of Acid'), '+')
        if (var.get('classtxt').callprop('indexOf', Js('Rogue'))>(-Js(1.0))):
            if (var.get('upgrade')()==Js(True)):
                var.put('eqOutput', Js(', Caltrops'), '+')
            if (var.get('upgradeUncommon')()==Js(True)):
                var.put('eqOutput', Js(', Magnifying Glass'), '+')
            if ((var.get('upgradeUncommon')()==Js(True)) and (var.get('classtxt').callprop('indexOf', Js('ssassin'))==(-Js(1.0)))):
                var.put('y', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(20.0))))
                if ((var.get('y')==Js(0.0)) and (var.get('upgradeVeryRare')()==Js(True))):
                    var.put('z', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('poisonVeryRare').get('length'))))
                    var.put('eqOutput', (Js(', Poison: ')+var.get('poisonVeryRare').get(var.get('z'))), '+')
                else:
                    if ((var.get('y')<Js(5.0)) and (var.get('upgradeRare')()==Js(True))):
                        var.put('z', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('poisonRare').get('length'))))
                        var.put('eqOutput', (Js(', Poison: ')+var.get('poisonRare').get(var.get('z'))), '+')
                    else:
                        if (var.get('upgradeUncommon')()==Js(True)):
                            var.put('z', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('poisonUncommon').get('length'))))
                            var.put('eqOutput', (Js(', Poison: ')+var.get('poisonUncommon').get(var.get('z'))), '+')
                        else:
                            var.put('eqOutput', Js(', Vial of Basic Poison'), '+')
        else:
            if (var.get('upgradeRare')()==Js(True)):
                var.put('eqOutput', Js(', Magnifying Glass'), '+')
            if (var.get('upgradeRare')()==Js(True)):
                var.put('eqOutput', Js(', Vial of Basic Poison'), '+')
        if (var.get('classtxt').callprop('indexOf', Js('ssassin'))>(-Js(1.0))):
            if (var.get('upgrade')()==Js(True)):
                var.put('eqOutput', Js(", Poisoner's Kit"), '+')
            if ((var.get('upgrade')()==Js(True)) and (var.get('eqOutput').callprop('indexOf', Js('Disguise'))==(-Js(1.0)))):
                var.put('eqOutput', Js(', Disguise Kit'), '+')
            var.put('bool', Js(False))
            if (var.get('upgrade')()==Js(True)):
                var.put('bool', Js(True))
            if (var.get('upgradeUncommon')()==Js(True)):
                var.put('xx', Js(0.0))
                var.put('xx', (var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(3.0)))+Js(1.0)))
                var.put('poOutput', Js('==EOF==Poison'), '+')
                if ((var.get('xx')>Js(1.0)) or var.put('bool', Js(True))):
                    var.put('poOutput', Js('s'), '+')
                var.put('poOutput', Js(': '), '+')
                if (var.get('bool')==Js(True)):
                    var.put('poOutput', Js('Basic poison, \t'), '+')
                var.put('first', Js(True))
                while (var.get('xx')>Js(0.0)):
                    var.put('y', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(20.0))))
                    if ((var.get('y')==Js(0.0)) and (var.get('upgradeVeryRare')()==Js(True))):
                        var.put('z', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('poisonVeryRare').get('length'))))
                        if (var.get('first')==Js(False)):
                            var.put('poOutput', Js(', '), '+')
                        var.put('poOutput', var.get('poisonVeryRare').get(var.get('z')), '+')
                        (var.put('xx',Js(var.get('xx').to_number())-Js(1))+Js(1))
                        var.put('first', Js(False))
                    else:
                        if ((var.get('y')<Js(5.0)) and (var.get('upgradeRare')()==Js(True))):
                            var.put('z', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('poisonRare').get('length'))))
                            if (var.get('first')==Js(False)):
                                var.put('poOutput', Js(', '), '+')
                            var.put('poOutput', var.get('poisonRare').get(var.get('z')), '+')
                            (var.put('xx',Js(var.get('xx').to_number())-Js(1))+Js(1))
                            var.put('first', Js(False))
                        else:
                            if (var.get('upgradeUncommon')()==Js(True)):
                                var.put('z', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('poisonUncommon').get('length'))))
                                if (var.get('first')==Js(False)):
                                    var.put('poOutput', Js(', '), '+')
                                var.put('poOutput', var.get('poisonUncommon').get(var.get('z')), '+')
                                (var.put('xx',Js(var.get('xx').to_number())-Js(1))+Js(1))
                                var.put('first', Js(False))
        var.put('bool', Js(False))
        if (var.get('upgrade')()==Js(True)):
            if (var.get('upgrade')()==Js(True)):
                var.put('x', (var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(3.0)))+Js(2.0)))
                if (var.get('level')>Js(6.0)):
                    (var.put('x',Js(var.get('x').to_number())+Js(1))-Js(1))
                if (var.get('level')<Js(5.0)):
                    var.put('x', (var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(2.0)))+Js(2.0)))
                var.put('maOutput', ((Js(', ')+var.get('x'))+Js(' Potions of Healing')), '+')
            else:
                var.put('maOutput', Js(', Potion of Healing'), '+')
            var.put('bool', Js(True))
        if ((var.get('bool')==Js(False)) and (var.get('cl')==Js(4.0))):
            if (var.get('upgrade')()==Js(True)):
                var.put('maOutput', Js(', Potion of Healing'), '+')
        var.put('eqOutput', (var.get('eqOutput')+var.get('poOutput')))
        if (var.get('upgrade')()==Js(True)):
            var.put('z', Js(0.0))
            var.put('xx', ((var.get('level')*Js(20.0))/Js(100.0)))
            if (var.get('level')<Js(7.0)):
                var.put('xx', Js(96.0))
            if (var.get('level')>Js(6.0)):
                var.put('xx', Js(99.0))
            var.get('console').callprop('log', ((((Js('* / * / * / * / Level ')+var.get('level'))+Js(' guy has a '))+var.get('xx'))+Js(' chance of getting the first  magic item')))
            if (var.get('Math').callprop('random')<var.get('xx')):
                (var.put('z',Js(var.get('z').to_number())+Js(1))-Js(1))
            if (var.get('level')<Js(5.0)):
                var.put('xx', Js(0.0))
            if (var.get('level')==Js(5.0)):
                var.put('xx', Js(5.0))
            if (var.get('level')>Js(5.0)):
                var.put('xx', (((var.get('level')-Js(5.0))*Js(20.0))/Js(100.0)))
            if (var.get('level')>Js(7.0)):
                var.put('xx', ((((var.get('level')-Js(8.0))*Js(13.0))+Js(70.0))/Js(100.0)))
            var.get('console').callprop('log', ((((Js('* / * / * / * / Level ')+var.get('level'))+Js(' guy has a '))+var.get('xx'))+Js(' chance of getting the second magic item')))
            if (var.get('Math').callprop('random')<var.get('xx')):
                (var.put('z',Js(var.get('z').to_number())+Js(1))-Js(1))
            if ((var.get('upgradeVeryRare')()==Js(True)) and (var.get('level')>Js(6.0))):
                (var.put('z',Js(var.get('z').to_number())+Js(1))-Js(1))
            var.get('console').callprop('log', ((Js('* / * / * / * / Your character has ')+var.get('z'))+Js(' magic item(s)')))
            while (var.get('z')>Js(0.0)):
                var.put('x', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(20.0))))
                if (var.get('x')==Js(0.0)):
                    var.put('y', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('magicVeryRare').get('length'))))
                    var.put('maOutput', (Js(', ')+var.get('magicVeryRare').get(var.get('y'))), '+')
                    var.put('z', (var.get('z')-Js(0.6)))
                else:
                    if (var.get('x')<Js(5.0)):
                        if (((var.get('Math').callprop('random')<Js(0.25)) and (var.get('magicArmor')==Js(0.0))) and (var.get('myAr').get('length')>Js(0.0))):
                            var.put('q', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('myAr').get('length'))))
                            if (var.get('upgradeVeryRare')()==Js(True)):
                                var.put('magicArmor', Js(2.0))
                            else:
                                var.put('magicArmor', Js(1.0))
                            var.put('maOutput', (((Js(', +')+var.get('magicArmor'))+Js(' '))+var.get('myAr').get(var.get('q'))), '+')
                            if (var.get('upgradeVeryRare')()==Js(True)):
                                var.put('i', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(10.0))))
                                var.put('maOutput', ((Js(' (Resistant to ')+var.get('ringResistance').get(var.get('i')))+Js(' damage)')), '+')
                            var.put('whichMagicArmor', var.get('q'))
                            (var.put('z',Js(var.get('z').to_number())-Js(1))+Js(1))
                        else:
                            var.put('y', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('magicRare').get('length'))))
                            if ((var.get('magicRare').get(var.get('y'))==Js('Ring of Resistance')) and (var.get('maOutput').callprop('indexOf', Js('Ring of Resistance'))==(-Js(1.0)))):
                                var.put('i', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(10.0))))
                                var.put('maOutput', ((((Js(', ')+var.get('ringStone').get(var.get('i')))+Js(' Ring of Resistance ('))+var.get('ringResistance').get(var.get('i')))+Js(' damage)')), '+')
                                (var.put('z',Js(var.get('z').to_number())-Js(1))+Js(1))
                            else:
                                if ((var.get('magicRare').get(var.get('y'))==Js('Ring of Protection')) and (var.get('maOutput').callprop('indexOf', Js('Ring of Protection'))==(-Js(1.0)))):
                                    var.put('ringProtection', Js(1.0))
                                    if (var.get('upgradeVeryRare')()==Js(True)):
                                        var.put('ringProtection', Js(2.0))
                                    var.put('maOutput', ((Js(', +')+var.get('ringProtection'))+Js(' Ring of Protection')), '+')
                                    (var.put('z',Js(var.get('z').to_number())-Js(1))+Js(1))
                                else:
                                    if ((var.get('magicRare').get(var.get('y'))==Js('Ring of Evasion (3 charges)')) and (var.get('maOutput').callprop('indexOf', Js('Ring of Evasion'))==(-Js(1.0)))):
                                        var.put('maOutput', (Js(', ')+var.get('magicRare').get(var.get('y'))), '+')
                                        (var.put('z',Js(var.get('z').to_number())-Js(1))+Js(1))
                    else:
                        if ((var.get('Math').callprop('random')<Js(0.2)) and (var.get('magicWeapon')==Js(0.0))):
                            var.put('bool', Js(False))
                            var.put('count', Js(0.0))
                            while (var.get('bool')==Js(False)):
                                (var.put('count',Js(var.get('count').to_number())+Js(1))-Js(1))
                                if (var.get('count')>Js(500.0)):
                                    var.put('bool', Js(True))
                                var.put('q', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('myWp').get('length'))))
                                var.put('i', var.get('weapons').callprop('indexOf', var.get('myWp').get(var.get('q'))))
                                var.put('y', (var.get('wpNum').get(var.get('i'))*Js(1.0)))
                                if ((var.get('y')==Js(0.0)) and (var.get('i')!=Js(23.0))):
                                    if (var.get('upgradeVeryRare')()==Js(True)):
                                        var.put('magicWeapon', Js(2.0))
                                        var.put('bool', Js(True))
                                        var.put('maOutput', (((Js(', +')+var.get('magicWeapon'))+Js(' '))+var.get('myWp').get(var.get('q'))), '+')
                                        var.put('whichMagic', var.get('q'))
                                        (var.put('z',Js(var.get('z').to_number())-Js(1))+Js(1))
                                    else:
                                        var.put('magicWeapon', Js(1.0))
                                        var.put('bool', Js(True))
                                        var.put('maOutput', (((Js(', +')+var.get('magicWeapon'))+Js(' '))+var.get('myWp').get(var.get('q'))), '+')
                                        var.put('whichMagic', var.get('q'))
                                        (var.put('z',Js(var.get('z').to_number())-Js(1))+Js(1))
                        else:
                            if (var.get('Math').callprop('random')<Js(0.2)):
                                var.put('xx', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(20.0))))
                                var.put('y', Js(0.0))
                                if (var.get('xx')==Js(0.0)):
                                    var.put('y', Js(2.0))
                                else:
                                    if (var.get('xx')<Js(4.0)):
                                        var.put('y', Js(1.0))
                                if (var.get('cl')==Js(2.0)):
                                    if (var.get('y')==Js(0.0)):
                                        var.put('maOutput', (Js(', Scroll of ')+var.get('scrollBardUnc').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('scrollBardUnc').get('length'))))), '+')
                                    else:
                                        if (var.get('y')==Js(1.0)):
                                            var.put('maOutput', (Js(', Scroll of ')+var.get('scrollBardRare').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('scrollBardRare').get('length'))))), '+')
                                        else:
                                            if (var.get('y')==Js(2.0)):
                                                var.put('maOutput', (Js(', Scroll of ')+var.get('scrollBardVery').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('scrollBardVery').get('length'))))), '+')
                                    var.put('z', (var.get('z')-Js(0.6)))
                                else:
                                    if (var.get('cl')==Js(3.0)):
                                        if (var.get('y')==Js(0.0)):
                                            var.put('maOutput', (Js(', Scroll of ')+var.get('scrollClerUnc').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('scrollClerUnc').get('length'))))), '+')
                                        else:
                                            if (var.get('y')==Js(1.0)):
                                                var.put('maOutput', (Js(', Scroll of ')+var.get('scrollClerRare').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('scrollClerRare').get('length'))))), '+')
                                            else:
                                                if (var.get('y')==Js(2.0)):
                                                    var.put('maOutput', (Js(', Scroll of ')+var.get('scrollClerVery').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('scrollClerVery').get('length'))))), '+')
                                        var.put('z', (var.get('z')-Js(0.6)))
                                    else:
                                        if (var.get('cl')==Js(4.0)):
                                            if (var.get('y')==Js(0.0)):
                                                var.put('maOutput', (Js(', Scroll of ')+var.get('scrollDruiUnc').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('scrollDruiUnc').get('length'))))), '+')
                                            else:
                                                if (var.get('y')==Js(1.0)):
                                                    var.put('maOutput', (Js(', Scroll of ')+var.get('scrollDruiRare').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('scrollDruiRare').get('length'))))), '+')
                                                else:
                                                    if (var.get('y')==Js(2.0)):
                                                        var.put('maOutput', (Js(', Scroll of ')+var.get('scrollDruiVery').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('scrollDruiVery').get('length'))))), '+')
                                            var.put('z', (var.get('z')-Js(0.6)))
                                        else:
                                            if (var.get('cl')==Js(9.0)):
                                                if (var.get('y')==Js(0.0)):
                                                    var.put('maOutput', (Js(', Scroll of ')+var.get('scrollPalaUnc').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('scrollPalaUnc').get('length'))))), '+')
                                                else:
                                                    if (var.get('y')==Js(1.0)):
                                                        var.put('maOutput', (Js(', Scroll of ')+var.get('scrollPalaRare').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('scrollPalaRare').get('length'))))), '+')
                                                    else:
                                                        if (var.get('y')==Js(2.0)):
                                                            var.put('maOutput', (Js(', Scroll of ')+var.get('scrollPalaVery').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('scrollPalaVery').get('length'))))), '+')
                                                var.put('z', (var.get('z')-Js(0.6)))
                                            else:
                                                if (var.get('cl')==Js(10.0)):
                                                    if (var.get('y')==Js(0.0)):
                                                        var.put('maOutput', (Js(', Scroll of ')+var.get('scrollRangUnc').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('scrollRangUnc').get('length'))))), '+')
                                                    else:
                                                        if (var.get('y')==Js(1.0)):
                                                            var.put('maOutput', (Js(', Scroll of ')+var.get('scrollRangRare').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('scrollRangRare').get('length'))))), '+')
                                                        else:
                                                            if (var.get('y')==Js(2.0)):
                                                                var.put('maOutput', (Js(', Scroll of ')+var.get('scrollRangVery').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('scrollRangVery').get('length'))))), '+')
                                                    var.put('z', (var.get('z')-Js(0.6)))
                                                else:
                                                    if (var.get('cl')==Js(14.0)):
                                                        if (var.get('y')==Js(0.0)):
                                                            var.put('maOutput', (Js(', Scroll of ')+var.get('scrollWarlUnc').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('scrollWarlUnc').get('length'))))), '+')
                                                        else:
                                                            if (var.get('y')==Js(1.0)):
                                                                var.put('maOutput', (Js(', Scroll of ')+var.get('scrollWarlRare').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('scrollWarlRare').get('length'))))), '+')
                                                            else:
                                                                if (var.get('y')==Js(2.0)):
                                                                    var.put('maOutput', (Js(', Scroll of ')+var.get('scrollWarlVery').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('scrollWarlVery').get('length'))))), '+')
                                                        var.put('z', (var.get('z')-Js(0.6)))
                                                    else:
                                                        if ((((var.get('cl')==Js(5.0)) or (var.get('cl')==Js(12.0))) or (var.get('cl')==Js(13.0))) or (var.get('cl')==Js(15.0))):
                                                            if (((var.get('y')==Js(0.0)) or (var.get('cl')==Js(5.0))) or (var.get('cl')==Js(12.0))):
                                                                var.put('maOutput', (Js(', Scroll of ')+var.get('scrollWizaUnc').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('scrollWizaUnc').get('length'))))), '+')
                                                            else:
                                                                if (var.get('y')==Js(1.0)):
                                                                    var.put('maOutput', (Js(', Scroll of ')+var.get('scrollWizaRare').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('scrollWizaRare').get('length'))))), '+')
                                                                else:
                                                                    if (var.get('y')==Js(2.0)):
                                                                        var.put('maOutput', (Js(', Scroll of ')+var.get('scrollWizaVery').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('scrollWizaVery').get('length'))))), '+')
                                                            var.put('z', (var.get('z')-Js(0.6)))
                            else:
                                if ((var.get('Math').callprop('random')<Js(0.2)) and (var.get('magicArrows')<Js(1.0))):
                                    var.put('bool', Js(False))
                                    #for JS loop
                                    var.put('x', Js(0.0))
                                    while (var.get('x')<var.get('myWp').get('length')):
                                        try:
                                            var.put('i', var.get('weapons').callprop('indexOf', var.get('myWp').get(var.get('x'))))
                                            if (((var.get('i')==Js(5.0)) or (var.get('i')==Js(6.0))) or (var.get('i')==Js(7.0))):
                                                var.put('bool', Js(True))
                                                var.get('rangedWeapons').callprop('push', var.get('i'))
                                            else:
                                                if ((var.get('i')==Js(8.0)) or (var.get('i')==Js(9.0))):
                                                    var.put('bool', Js(True))
                                                    var.get('rangedWeapons').callprop('push', var.get('i'))
                                                else:
                                                    if (var.get('i')==Js(24.0)):
                                                        var.put('bool', Js(True))
                                                        var.get('rangedWeapons').callprop('push', var.get('i'))
                                        finally:
                                                (var.put('x',Js(var.get('x').to_number())+Js(1))-Js(1))
                                    if (var.get('bool')==Js(True)):
                                        var.put('i', var.get('rangedWeapons').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('rangedWeapons').get('length')))))
                                        if (((var.get('i')==Js(5.0)) or (var.get('i')==Js(6.0))) or (var.get('i')==Js(7.0))):
                                            var.put('magicArrowType', Js('Crossbow bolts'))
                                        else:
                                            if ((var.get('i')==Js(8.0)) or (var.get('i')==Js(9.0))):
                                                var.put('magicArrowType', Js('Arrows'))
                                            else:
                                                if (var.get('i')==Js(24.0)):
                                                    var.put('magicArrowType', Js('Sling bullets'))
                                        if (var.get('upgradeRare')()==Js(True)):
                                            var.put('magicArrowPlus', Js(3.0))
                                            var.put('magicArrows', (var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(8.0)))+Js(3.0)))
                                        else:
                                            if (var.get('upgradeUncommon')()==Js(True)):
                                                var.put('magicArrowPlus', Js(2.0))
                                                var.put('magicArrows', ((var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(6.0)))+Js(2.0))+(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(6.0)))+Js(2.0))))
                                            else:
                                                var.put('magicArrowPlus', Js(1.0))
                                                var.put('magicArrows', ((((var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(6.0)))+Js(1.0))+(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(6.0)))+Js(1.0)))+(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(6.0)))+Js(1.0)))+Js(3.0)))
                                        (var.put('z',Js(var.get('z').to_number())-Js(1))+Js(1))
                                        var.put('maOutput', ((((((Js(', +')+var.get('magicArrowPlus'))+Js(' '))+var.get('magicArrowType'))+Js(' ('))+var.get('magicArrows'))+Js(')')), '+')
                                else:
                                    var.put('y', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('magicUncommon').get('length'))))
                                    var.put('maOutput', (Js(', ')+var.get('magicUncommon').get(var.get('y'))), '+')
                                    if (var.get('magicUncommon').get(var.get('y'))==Js("Keoghtom's Ointment")):
                                        var.put('maOutput', ((Js(' (')+(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(4.0)))+Js(2.0)))+Js(' doses)')), '+')
                                        (var.put('z',Js(var.get('z').to_number())-Js(1))+Js(1))
                                    else:
                                        if ((var.get('magicUncommon').get(var.get('y'))==Js('Boots of Striding and Springing')) and (var.get('maOutput').callprop('indexOf', Js('Striding and Springing'))==(-Js(1.0)))):
                                            var.put('bootsOfSS', Js(True))
                                            (var.put('z',Js(var.get('z').to_number())-Js(1))+Js(1))
                                        else:
                                            (var.put('z',Js(var.get('z').to_number())-Js(1))+Js(1))
    var.put('eqOutput', var.get('weOutput'), '+')
    if (var.get('maOutput').get('length')>Js(0.0)):
        var.put('eqOutput', Js('==EOF==<b>Magic Item'), '+')
        if ((var.get('maOutput').callprop('indexOf', Js(','))!=var.get('maOutput').callprop('lastIndexOf', Js(','))) or (var.get('maOutput').callprop('indexOf', Js('otions'))>(-Js(1.0)))):
            var.put('eqOutput', Js('s'), '+')
        var.put('maOutput', var.get('maOutput').callprop('slice', Js(1.0), var.get('maOutput').get('length')))
        var.put('eqOutput', (Js(':</b> ')+var.get('maOutput')), '+')
        var.get('console').callprop('log', var.get('maOutput'))
    if (var.get('companion')>(-Js(1.0))):
        if ((var.get('level')*Js(4.0))>var.get('companionshp').get(var.get('companion'))):
            var.get('companionshp').put(var.get('companion'), (var.get('level')*Js(4.0)))
        def PyJs_LONG_14_(var=var):
            return ((((((((Js("==EOF==<b>Ranger's Companion:</b>  ")+var.get('companions').get(var.get('companion')))+Js(' - '))+(var.get('companionshp').get(var.get('companion'))*Js(1.0)))+Js(' hit points, '))+((var.get('companionsAC').get(var.get('companion'))*Js(1.0))+(var.get('prof')*Js(1.0))))+Js(' AC, '))+var.get('companionsStats').get(var.get('companion')))+((var.get('companionsAttack1').get(var.get('companion'))*Js(1.0))+var.get('prof')))
        var.put('eqOutput', (((((((PyJs_LONG_14_()+Js(' to hit ('))+var.get('companionsDamage1').get(var.get('companion')))+Js('+'))+(var.get('companionsDamageBonus').get(var.get('companion'))+var.get('prof')))+Js(' dmg'))+var.get('companionsDamageExtra').get(var.get('companion')))+Js(')')), '+')
        if (var.get('companionsAttackText2').get(var.get('companion')).get('length')>Js(0.0)):
            var.put('eqOutput', ((((((((Js(', ')+var.get('companionsAttackText2').get(var.get('companion')))+Js(' +'))+((var.get('companionsAttack2').get(var.get('companion'))*Js(1.0))+var.get('prof')))+Js(' to hit ('))+var.get('companionsAttackDamage2').get(var.get('companion')))+Js('+'))+(var.get('companionsDamageBonus2').get(var.get('companion'))+var.get('prof')))+Js(' dmg)')), '+')
    if (var.get('familiar').get('length')>Js(0.0)):
        var.put('spOutput', (Js('==EOF==<b>Pact of the Chain Familiar:</b>  ')+var.get('familiar')), '+')
    if ((var.get('familiar').get('length')==Js(0.0)) and ((var.get('mySpells').callprop('indexOf', Js('Find Familiar'))>(-Js(1.0))) or (var.get('waTomeRituals').callprop('indexOf', Js('Find Familiar'))>(-Js(1.0))))):
        var.put('x', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('familiars').get('length'))))
        var.put('spOutput', (Js('==EOF==<b>Familiar:</b> ')+var.get('familiars').get(var.get('x'))), '+')
    #for JS loop
    var.put('x', Js(0.0))
    while (var.get('x')<var.get('myWp').get('length')):
        try:
            var.put('i', var.get('weapons').callprop('indexOf', var.get('myWp').get(var.get('x'))))
            var.put('temp', Js(0.0))
            if (var.get('wpRange').get(var.get('i'))!=Js(2.0)):
                if (((var.get('wpRange').get(var.get('i'))==Js(1.0)) or (var.get('wpRange').get(var.get('i'))==Js(4.0))) and (var.get('mod').get('1')>var.get('mod').get('0'))):
                    var.put('temp', Js(1.0))
                else:
                    var.put('temp', Js(0.0))
                if (var.get('cl')==Js(8.0)):
                    var.put('temp', Js(1.0))
                var.put('wpOutput', Js(''), '+')
                var.put('tempTxt', Js(''))
                var.put('y', Js(0.0))
                if (var.get('x')==var.get('whichMagic')):
                    var.put('y', var.get('magicWeapon'))
                    var.put('wpOutput', ((Js(' +')+var.get('y'))+Js(' ')), '+')
                if (var.get('wpNum').get(var.get('i'))>Js(0.0)):
                    var.put('wpOutput', (var.get('wpNum').get(var.get('i'))+Js(' ')), '+')
                var.put('wpOutput', var.get('myWp').get(var.get('x')), '+')
                if (var.get('wpNum').get(var.get('i'))>Js(0.0)):
                    var.put('wpOutput', Js('s'), '+')
                if ((var.get('i')==Js(23.0)) and (var.get('level')>Js(4.0))):
                    var.get('wpDam').put(var.get('i'), Js('1d6'))
                var.put('z', Js(0.0))
                if (((((var.get('fiStyle')==Js(2.0)) and (var.get('i')!=Js(12.0))) and (var.get('i')!=Js(13.0))) and (var.get('i')!=Js(20.0))) and (var.get('wpNum').get(var.get('i'))<Js(1.0))):
                    var.put('z', Js(2.0))
                var.put('wpOutput', (((((((Js(' (')+var.get('showPlus')(((var.get('mod').get(var.get('temp'))+var.get('prof'))+var.get('y'))))+Js(' to hit) '))+var.get('wpDam').get(var.get('i')))+var.get('showPlus')(((var.get('mod').get(var.get('temp'))+var.get('z'))+var.get('y'))))+Js(' '))+var.get('wpType').get(var.get('i')))+Js(' damage==EOF==')), '+')
            if (var.get('wpRange').get(var.get('i'))>Js(1.0)):
                var.put('wrOutput', Js(''), '+')
                var.put('q', Js(0.0))
                if (var.get('x')==var.get('whichMagic')):
                    var.put('q', var.get('magicWeapon'))
                    var.put('wrOutput', ((Js(' +')+var.get('q'))+Js(' ')), '+')
                if (var.get('wpNum').get(var.get('i'))>Js(0.0)):
                    var.put('wrOutput', (var.get('wpNum').get(var.get('i'))+Js(' ')), '+')
                var.put('wrOutput', var.get('myWp').get(var.get('x')), '+')
                if (var.get('wpNum').get(var.get('i'))>Js(0.0)):
                    var.put('wrOutput', Js('s'), '+')
                var.put('z', Js(0.0))
                if ((var.get('fiStyle')==Js(0.0)) or (var.get('fiStyle2')==Js(0.0))):
                    var.put('z', Js(2.0))
                var.put('y', var.get('mod').get('1'))
                if ((var.get('wpRange').get(var.get('i'))==Js(4.0)) and (var.get('mod').get('0')>var.get('mod').get('1'))):
                    var.put('y', var.get('mod').get('0'))
                if (var.get('wpRange').get(var.get('i'))==Js(3.0)):
                    var.put('y', var.get('mod').get('0'))
                if ((var.get('i')==Js(21.0)) and (var.get('mod').get('0')>var.get('mod').get('1'))):
                    var.put('y', var.get('mod').get('0'))
                if (var.get('i')==Js(6.0)):
                    var.put('tempTxt', var.get('wpDam').get(var.get('i')).callprop('slice', Js(0.0), Js(4.0)))
                else:
                    var.put('tempTxt', var.get('wpDam').get(var.get('i')).callprop('slice', Js(0.0), Js(3.0)))
                var.put('wrOutput', (((((((((Js(' (')+var.get('showPlus')((((var.get('y')+var.get('z'))+var.get('prof'))+var.get('q'))))+Js(' to hit) '))+var.get('tempTxt'))+var.get('showPlus')((var.get('y')+var.get('q'))))+Js(' '))+var.get('wpType').get(var.get('i')))+Js(' damage   Range: '))+var.get('wpDistance').get(var.get('i')))+Js('')), '+')
                if (((var.get('i')==Js(5.0)) or (var.get('i')==Js(6.0))) or (var.get('i')==Js(7.0))):
                    if ((var.get('fiStyle')==Js(0.0)) or (var.get('cl')==Js(10.0))):
                        var.put('wrOutput', Js('   40 bolts==EOF=='), '+')
                    else:
                        var.put('wrOutput', Js('   20 bolts==EOF=='), '+')
                    if (((var.get('magicArrowPlus')>Js(0.0)) and (var.get('magicArrowType').callprop('indexOf', Js('olt'))>(-Js(1.0)))) and (var.get('magicArrowDisplay')==Js(False))):
                        def PyJs_LONG_15_(var=var):
                            return (((((((((((((Js('+')+var.get('magicArrowPlus'))+Js(' '))+var.get('magicArrowType'))+Js(' ('))+var.get('magicArrows'))+Js(') ('))+var.get('showPlus')(((((var.get('y')+var.get('z'))+var.get('prof'))+var.get('q'))+var.get('magicArrowPlus'))))+Js(' to hit) '))+var.get('tempTxt'))+var.get('showPlus')(((var.get('y')+var.get('q'))+var.get('magicArrowPlus'))))+Js(' '))+var.get('wpType').get(var.get('i')))+Js(' damage'))
                        var.put('wrOutput', PyJs_LONG_15_(), '+')
                        var.put('magicArrowDisplay', Js(True))
                if ((var.get('i')==Js(8.0)) or (var.get('i')==Js(9.0))):
                    if ((var.get('fiStyle')==Js(0.0)) or (var.get('cl')==Js(10.0))):
                        var.put('wrOutput', Js('   40 arrows==EOF=='), '+')
                    else:
                        var.put('wrOutput', Js('   20 arrows==EOF=='), '+')
                    if (((var.get('magicArrowPlus')>Js(0.0)) and (var.get('magicArrowType').callprop('indexOf', Js('rrow'))>(-Js(1.0)))) and (var.get('magicArrowDisplay')==Js(False))):
                        def PyJs_LONG_16_(var=var):
                            return (((((((((((((Js('+')+var.get('magicArrowPlus'))+Js(' '))+var.get('magicArrowType'))+Js(' ('))+var.get('magicArrows'))+Js(') ('))+var.get('showPlus')(((((var.get('y')+var.get('z'))+var.get('prof'))+var.get('q'))+var.get('magicArrowPlus'))))+Js(' to hit) '))+var.get('tempTxt'))+var.get('showPlus')(((var.get('y')+var.get('q'))+var.get('magicArrowPlus'))))+Js(' '))+var.get('wpType').get(var.get('i')))+Js(' damage'))
                        var.put('wrOutput', PyJs_LONG_16_(), '+')
                        var.put('magicArrowDisplay', Js(True))
                if (var.get('i')==Js(24.0)):
                    var.put('wrOutput', Js('   20 bullets==EOF=='), '+')
                    if (((var.get('magicArrowPlus')>Js(0.0)) and (var.get('magicArrowType').callprop('indexOf', Js('ullet'))>(-Js(1.0)))) and (var.get('magicArrowDisplay')==Js(False))):
                        def PyJs_LONG_17_(var=var):
                            return (((((((((((((Js('+')+var.get('magicArrowPlus'))+Js(' '))+var.get('magicArrowType'))+Js(' ('))+var.get('magicArrows'))+Js(') ('))+var.get('showPlus')(((((var.get('y')+var.get('z'))+var.get('prof'))+var.get('q'))+var.get('magicArrowPlus'))))+Js(' to hit) '))+var.get('tempTxt'))+var.get('showPlus')(((var.get('y')+var.get('q'))+var.get('magicArrowPlus'))))+Js(' '))+var.get('wpType').get(var.get('i')))+Js(' damage'))
                        var.put('wrOutput', PyJs_LONG_17_(), '+')
                        var.put('magicArrowDisplay', Js(True))
        finally:
                (var.put('x',Js(var.get('x').to_number())+Js(1))-Js(1))
    if (var.get('wrOutput').get('length')>Js(0.0)):
        var.put('wpOutput', (Js('<b>Ranged weapons:</b>  ==EOF==')+var.get('wrOutput')), '+')
    var.put('ac', Js(10.0))
    var.put('z', Js(0.0))
    var.get('console').callprop('log', var.get('myAr'))
    #for JS loop
    var.put('x', Js(0.0))
    while (var.get('x')<var.get('myAr').get('length')):
        try:
            var.put('i', var.get('armors').callprop('indexOf', var.get('myAr').get(var.get('x'))))
            if (var.get('i')==Js(0.0)):
                var.put('hasShield', Js(True))
            else:
                if (var.get('i')>Js(0.0)):
                    var.put('hasArmor', Js(1.0))
                if (var.get('i')>Js(3.0)):
                    var.put('hasArmor', Js(2.0))
                if (var.get('i')>Js(8.0)):
                    var.put('hasArmor', Js(3.0))
                var.put('z', var.get('i'))
        finally:
                (var.put('x',Js(var.get('x').to_number())+Js(1))-Js(1))
    if (var.get('hasArmor')<Js(0.0)):
        var.put('hasArmor', Js(0.0))
    while 1:
        SWITCHED = False
        CONDITION = (var.get('hasArmor'))
        if SWITCHED or PyJsStrictEq(CONDITION, Js(0.0)):
            SWITCHED = True
            if (var.get('soOrigin')==Js(0.0)):
                var.put('ac', Js(13.0))
            if (var.get('mod').get('1')>Js(0.0)):
                var.put('ac', var.get('mod').get('1'), '+')
            if ((var.get('cl')==Js(1.0)) and (var.get('mod').get('2')>Js(0.0))):
                var.put('ac', var.get('mod').get('2'), '+')
            if ((var.get('cl')==Js(8.0)) and (var.get('mod').get('4')>Js(0.0))):
                var.put('ac', var.get('mod').get('4'), '+')
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
            SWITCHED = True
            var.put('ac', var.get('armorAC').get(var.get('z')))
            if (var.get('mod').get('1')>Js(0.0)):
                var.put('ac', var.get('mod').get('1'), '+')
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
            SWITCHED = True
            var.put('ac', var.get('armorAC').get(var.get('z')))
            var.put('x', Js(0.0))
            if (var.get('mod').get('1')>Js(1.0)):
                var.put('x', Js(2.0))
            if (var.get('mod').get('1')==Js(1.0)):
                var.put('x', Js(1.0))
            var.put('ac', var.get('x'), '+')
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(3.0)):
            SWITCHED = True
            var.put('ac', var.get('armorAC').get(var.get('z')))
            break
        SWITCHED = True
        break
    if (var.get('hasShield')==Js(True)):
        var.put('ac', Js(2.0), '+')
    if (var.get('ringProtection')>Js(0.0)):
        var.put('ac', var.get('ringProtection'), '+')
    if ((var.get('hasArmor')>Js(0.0)) and (var.get('fiStyle')==Js(1.0))):
        var.put('ac', Js(1.0), '+')
    if (var.get('magicArmor')>Js(0.0)):
        var.put('ac', var.get('magicArmor'), '+')
    if ((var.get('myAr').get('0')==Js('Shield')) and (var.get('myAr').get('length')>Js(1.0))):
        var.get('myAr').callprop('reverse')
        if (var.get('magicArmor')>Js(0.0)):
            if (var.get('whichMagicArmor')==Js(0.0)):
                var.put('whichMagicArmor', Js(1.0))
            else:
                var.put('whichMagicArmor', Js(0.0))
    var.put('arOutput', ((((((Js('<b>Hit points:</b> ')+var.get('hp'))+Js('   <b>Hit dice:</b>  '))+var.get('level'))+Js('d'))+var.get('hd'))+Js('==EOF==<b>Armor:</b>  ')), '+')
    if (var.get('myAr').get('length')==Js(0.0)):
        var.put('arOutput', Js('None'), '+')
    if (var.get('myAr').get('length')>Js(1.0)):
        if (var.get('whichMagicArmor')==Js(0.0)):
            var.put('arOutput', ((Js('+')+var.get('magicArmor'))+Js(' ')), '+')
        var.put('arOutput', (var.get('myAr').get('0')+Js(' and ')), '+')
        if (var.get('whichMagicArmor')==Js(1.0)):
            var.put('arOutput', ((Js('+')+var.get('magicArmor'))+Js(' ')), '+')
        var.put('arOutput', var.get('myAr').get('1'), '+')
    if (var.get('myAr').get('length')==Js(1.0)):
        if (var.get('magicArmor')>Js(0.0)):
            var.put('arOutput', ((Js('+')+var.get('magicArmor'))+Js(' ')), '+')
        var.put('arOutput', var.get('myAr'), '+')
    var.put('arOutput', ((Js('==EOF==<b>AC:</b>  ')+var.get('ac'))+Js('==EOF==')), '+')
    if (var.get('abOutput').callprop('charAt', Js(0.0))==Js(',')):
        var.put('abOutput', var.get('abOutput').callprop('slice', Js(1.0), var.get('abOutput').get('length')))
    if (var.get('eqOutput')!=Js('')):
        if (var.get('eqOutput').callprop('charAt', Js(0.0))==Js(',')):
            var.put('eqOutput', var.get('eqOutput').callprop('slice', Js(1.0), var.get('eqOutput').get('length')))
    if (var.get('toOutput')!=Js('')):
        if (var.get('toOutput').callprop('charAt', Js(0.0))==Js(',')):
            var.put('toOutput', var.get('toOutput').callprop('slice', Js(1.0), var.get('toOutput').get('length')))
        var.put('abOutput', (((Js('==EOF==<b>Other proficiencies:</b>')+var.get('toOutput'))+Js('==EOF=='))+var.get('abOutput')))
    else:
        var.put('abOutput', (Js('==EOF==')+var.get('abOutput')))
    var.put('x', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(4.0))))
    if (var.get('x')==Js(0.0)):
        var.put('myFaction', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(5.0))))
    else:
        if ((var.get('cl')==Js(2.0)) or (var.get('cl')==Js(15.0))):
            var.put('myFaction', Js(0.0))
        if (((var.get('cl')==Js(3.0)) or (var.get('cl')==Js(8.0))) or (var.get('cl')==Js(9.0))):
            var.put('myFaction', Js(1.0))
        if (((var.get('cl')==Js(1.0)) or (var.get('cl')==Js(4.0))) or (var.get('cl')==Js(10.0))):
            var.put('myFaction', Js(2.0))
        if ((((var.get('cl')==Js(13.0)) or (var.get('cl')==Js(5.0))) or (var.get('cl')==Js(6.0))) or (var.get('cl')==Js(7.0))):
            var.put('myFaction', Js(3.0))
        if (((var.get('cl')==Js(14.0)) or (var.get('cl')==Js(11.0))) or (var.get('cl')==Js(12.0))):
            var.put('myFaction', Js(4.0))
    #for JS loop
    var.put('x', Js(0.0))
    while (var.get('x')<Js(6.0)):
        try:
            var.get('saves').put(var.get('x'), var.get('mod').get(var.get('x')))
            if (var.get('ringProtection')>Js(0.0)):
                var.get('saves').put(var.get('x'), var.get('ringProtection'), '+')
            if ((var.get('level')>Js(5.0)) and (var.get('cl')==Js(9.0))):
                var.put('z', var.get('mod').get('5'))
                if (var.get('z')<Js(1.0)):
                    var.put('z', Js(1.0))
                var.get('saves').put(var.get('x'), var.get('z'), '+')
        finally:
                (var.put('x',Js(var.get('x').to_number())+Js(1))-Js(1))
    #for JS loop
    var.put('x', Js(0.0))
    while (var.get('x')<Js(2.0)):
        try:
            var.put('i', var.get('st').get(var.get('x')))
            var.get('saves').put(var.get('i'), var.get('prof'), '+')
        finally:
                (var.put('x',Js(var.get('x').to_number())+Js(1))-Js(1))
    if ((var.get('spOutput').get('length')==Js(0.0)) and (var.get('raceSpells').get('length')==Js(0.0))):
        var.get('magicGet')(Js('spellspot'), var.get('possibile')).get('style').put('display', Js('none'))
    else:
        var.get('magicGet')(Js('spellspot'), var.get('possibile')).get('style').put('display', Js('block'))
    var.put('initiative', var.get('mod').get('1'))
    if (var.get('abOutput').callprop('indexOf', Js('Jack of all'))>(-Js(1.0))):
        var.put('initiative', var.get('Math').callprop('floor', (var.get('prof')/Js(2.0))), '+')
    if (var.get('abOutput').callprop('indexOf', Js('Remarkable Athlete'))>(-Js(1.0))):
        var.put('initiative', var.get('Math').callprop('ceil', (var.get('prof')/Js(2.0))), '+')
    var.get('showAbil')()
    if (var.get('al')==Js(True)):
        var.put('output', (((Js('Faction:  ')+var.get('factions').get(var.get('myFaction')))+Js('   Lifestyle:  '))+var.get('lifestyles').get(var.get('myLifestyle'))), '+')
    var.put('GRECHINA', Js('<pre>------</pre>'))
    var.put('res', Js(''))
    var.put('res', (Js('')+var.get('output')), '+')
    var.put('res', (var.get('GRECHINA')+Js('==EOF==')), '+')
    var.put('res', (Js('')+var.get('rollOutput')), '+')
    var.put('res', (Js('')+var.get('skOutput')), '+')
    var.put('res', (Js('')+var.get('abOutput')), '+')
    var.put('res', (Js('')+var.get('wpOutput')), '+')
    if (var.get('wpOutput').callprop('slice', (-Js(7.0)))!=Js('==EOF==')):
        var.put('res', Js('==EOF=='), '+')
    var.put('res', (Js('')+var.get('arOutput')), '+')
    var.put('res', ((Js('<b>Language:</b> ')+var.get('languageOutput'))+Js('==EOF==')), '+')
    var.put('res', (var.get('GRECHINA')+Js('==EOF==')), '+')
    var.put('res', (Js('')+var.get('bgOutput')), '+')
    var.put('res', ((Js('==EOF==')+var.get('GRECHINA'))+Js('==EOF==<b>Items:</b>==EOF==')), '+')
    var.put('res', (Js('')+var.get('eqOutput')), '+')
    var.put('res', (Js('')+var.get('spOutput')), '+')
    return var.get('res')
PyJsHoisted_run_.func_name = 'run'
var.put('run', PyJsHoisted_run_)
pass
pass
pass
pass


# Add lib to the module scope
runchar = var.to_python()