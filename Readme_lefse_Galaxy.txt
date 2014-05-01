Installation instructions for lefse in a galaxy environment.
These instructions require the Mercurial versioning system, galaxy, and an internet connection.

1. In the  "galaxy-dist/tools" directory install lefse by cloning the repository: 

		bitbucket.org/biobakery/lefse_galaxy

2.  Rename the galaxy_lefse  directory thus created to "lefse"
	
3. Update member tool_conf.xml  in the galaxy directory adding the following: 

  <section name="LEfSe" id="lefse">
   <tool file="lefse/format_input.xml" />
   <tool file="lefse/run_lefse.xml" />
   <tool file="lefse/plot_res.xml" />
   <tool file="lefse/plot_cladogram.xml" />
   <tool file="lefse/plot_single_feature.xml" />
   <tool file="lefse/plot_features.xml" />
  </section>
 

4. Update member datatypes_conf.xml  in the galaxy directory adding the following:
	<datatype extension="lefse" type="galaxy.datatypes.data:Lefse" display_in_upload="true"/>
    <datatype extension="lefse_res" type="galaxy.datatypes.tabular:LefseRes" display_in_upload="true"/>

5. Copy the *.png members to galaxy-dist/static/images

6. Recycle galaxy

