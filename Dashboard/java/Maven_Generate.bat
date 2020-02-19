cd C:\CodeRepos\gitlab
@echo -DgroupId=com.company -DartifactId=project -Dversion= -Dpackage=com.company.project
@echo "project                                     "          
@echo "|-- pom.xml                                 "
@echo "`-- src                                     "
@echo "    |-- main                                "
@echo "    |   `-- java                            "
@echo "    |       `-- com                         "
@echo "    |           `-- company                 "
@echo "    |               `-- project             "
@echo "    |                   `-- App.java        "
@echo "    `-- test                                "
@echo "        `-- java                            "
@echo "            `-- com                         "
@echo "                `-- company                 "
@echo "                    `-- project   	       "
@echo "                        `-- AppTest.java    "
@echo "enter q for quickstart j for j2ee-simple w for webapp"
@SET /P x=[archetype]
@echo %x%
@REM IF %x%==quickstart C:\JAVA\apache-maven-3.6.0\bin\mvn -s C:\JAVA\apache-maven-3.6.0\conf\settings.xml archetype:generate -DarchetypeArtifactId=maven-archetype-quickstart -Dversion=1.0-SNAPSHOT -DinteractiveMode=true
@REM IF %x%==j2ee-simple C:\JAVA\apache-maven-3.6.0\bin\mvn -s C:\JAVA\apache-maven-3.6.0\conf\settings.xml archetype:generate -DarchetypeArtifactId=maven-archetype-j2ee-simple -Dversion=1.0-SNAPSHOT -DinteractiveMode=true 
@REM IF %x%==webapp C:\JAVA\apache-maven-3.6.0\bin\mvn -s C:\JAVA\apache-maven-3.6.0\conf\settings.xml archetype:generate -DarchetypeArtifactId=maven-archetype-webapp -Dversion=1.0-SNAPSHOT -DinteractiveMode=true
IF %x%==q mvn -s "C:\Users\CY59857\.m2\settings_isbank.xml" archetype:generate -DarchetypeArtifactId=maven-archetype-quickstart -Dversion=1.0-SNAPSHOT -DinteractiveMode=true
IF %x%==j mvn archetype:generate -DarchetypeArtifactId=maven-archetype-j2ee-simple -Dversion=1.0-SNAPSHOT -DinteractiveMode=true 
IF %x%==w mvn archetype:generate -DarchetypeArtifactId=maven-archetype-webapp -Dversion=1.0-SNAPSHOT -DinteractiveMode=true
IF %x%==s mvn -s "C:\Users\CY59857\.m2\settings_isbank.xml" archetype:generate -DarchetypeArtifactId=maven-archetype-simple -Dversion=1.0-SNAPSHOT -DinteractiveMode=false
@REM Archetype ArtifactIds 	Description
@REM maven-archetype-archetype 	An archetype to generate a sample archetype project.
@REM maven-archetype-j2ee-simple 	An archetype to generate a simplifed sample J2EE application.
@REM maven-archetype-mojo 	An archetype to generate a sample a sample Maven plugin.
@REM maven-archetype-plugin 	An archetype to generate a sample Maven plugin.
@REM maven-archetype-plugin-site 	An archetype to generate a sample Maven plugin site.
@REM maven-archetype-portlet 	An archetype to generate a sample JSR-268 Portlet.
@REM maven-archetype-quickstart 	An archetype to generate a sample Maven project.
@REM maven-archetype-simple 	An archetype to generate a simple Maven project.
@REM maven-archetype-site 	An archetype to generate a sample Maven site which demonstrates some of the supported document types like APT, XDoc, and FML and demonstrates how to i18n your site.
@REM maven-archetype-site-simple 	An archetype to generate a sample Maven site.
@REM maven-archetype-webapp 	An archetype to generate a sample Maven Webapp project.