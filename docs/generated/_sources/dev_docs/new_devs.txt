New Developments
================

This sections documents the latest developments in the core functionality. None of this affects the user experience. These functionalities simply make it easier to continue the further development of `eppy`.

The plan is to write all the documentation here as a place holder. Then later find more logical location in the overall developer developer documentation.

EpBunch -> new functions & fields
---------------------------------

Most of these are helper fields and functions act as syntactic sugar and make it easier to get to some data points of the EpBunch. Just to remind ourself of of EpBunch::

    zones = idf.idfobjects['ZONE']
    zone = zones[0]
    print type(zone)
    
    <class 'eppy.bunch_subclass.EpBunch'>
    
We can access the fields of `zone`::

    print zone.Name, zone.Ceiling_Height
    
    PLENUM-1 0.609600067
    
The following descrines the new functions and fields of zone. In effect it is the functions and fields of any EpBunch object

idfobj.theidf
~~~~~~~~~~~~~

Sometimes we need to access other objects in the idf file. For instance, we have a construction object and want to acces the materials that make up the construction object. To do that we need to access the idf file that the construction object belongs to. We can do this by::

    construction.theidf

to make this more explicit::        

    constructions = idf.idfobjects['construction'.upper()]
    construction = constructions[0]
    print construction
    
    Construction,             
        ROOF-1,                   !- Name
        RG01,                     !- Outside Layer
        BR01,                     !- Layer 2
        IN46,                     !- Layer 3
        WD01;                     !- Layer 4
    
Let us try to get the material in `Layer 2`::

    objects_idf = construction.theidf
    material = objects_idf.getobject('material'.upper(), construction.Layer_2)
    print material
    
    Material,                 
        BR01,                     !- Name
        VeryRough,                !- Roughness
        0.0094999997,             !- Thickness
        0.162,                    !- Conductivity
        1121.0,                   !- Density
        1464.0,                   !- Specific Heat
        0.9,                      !- Thermal Absorptance
        0.7,                      !- Solar Absorptance
        0.7;                      !- Visible Absorptance

If the idfobject does not belong to an idf file then it will respond None::

    print idfobject.theidf
    
    None
    
idfobj.objidd
~~~~~~~~~~~~~

To get the idd of the object do the following::

    version = idf.idfobjects['version'.upper()][0]
    objidd = version.objidd
    print objidd
    
    [{u'format': [u'singleLine'],
      u'group': u'Simulation Parameters',
      u'idfobj': u'Version',
      u'unique-object': [u'']},
     {u'default': [u'7.0'],
      u'field': [u'Version Identifier'],
      u'required-field': [u'']}]

idfobj.getfieldidd
~~~~~~~~~~~~~~~~~~

`getfieldidd` gets the idd of a specific field. Let us work ourselves towards `getfieldidd`::

    version = idf.idfobjects['version'.upper()][0]
    print version
    
    Version,                  
        7.0;                      !- Version Identifier
    
    print version.objls
    
    [u'key', u'Version_Identifier']
    
    print version.getfieldidd("key")
    
    {u'format': [u'singleLine'],
     u'group': u'Simulation Parameters',
     u'idfobj': u'Version',
     u'unique-object': [u'']}
     
     print version.getfieldidd("Version_Identifier")
     
     {u'default': [u'7.0'],
      u'field': [u'Version Identifier'],
      u'required-field': [u'']}
      
Indexing the IDD
----------------

Eppy stores the information from the IDD file in IDF.idd_info. This information is pulled into eppy as soon as the first idf file is read.       
      
      