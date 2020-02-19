

The artifact maven-archetype-simple does exist on Maven Central, but it isn't a valid archetype since it doesn't containt the right metadata files. A valid archetype must have in its JAR file:

    either a META-INF/maven/archetype-metadata.xml (this is the new format);
    or a META-INF/maven/archetype.xml or even a META-INF/archetype.xml (this is the old format).

And that specific artifact, as it is present on Central, doesn't have those files. As such, it isn't considered a valid archetype for the plugin. Those files store the required parameters for the archetype, their possible default values, the files that it should use, etc. so they really are required.

I'm not sure there exists an archetype that would generate just a lone pom.xml with the given Maven coordinates. This is effectively what using the maven-archetype-quickstart, without generating the App.java and AppTest.java would do. Keep in mind that an archetype is really intended at creating a project from a pre-defined template, like a sample Java EE application, or a sample Maven project; all of those would require more set-up than just writing a POM file.

If you really, really, do not want those files, you can either
Create your own archetype

Create a new Maven project, for example my-simple-archetype, with the following directory structure:

pom.xml
src
\---main
    \---resources
        +---archetype-resources
        |       pom.xml
        |
        \---META-INF
            \---maven
                    archetype-metadata.xml

Content of pom.xml at the root:

<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <groupId>eric</groupId>
  <artifactId>my-simple-archetype</artifactId>
  <version>0.1</version>
  <packaging>maven-archetype</packaging>
  <build>
    <extensions>
      <extension>
        <groupId>org.apache.maven.archetype</groupId>
        <artifactId>archetype-packaging</artifactId>
        <version>2.4</version>
      </extension>
    </extensions>
    <pluginManagement>
      <plugins>
        <plugin>
          <groupId>org.apache.maven.plugins</groupId>
          <artifactId>maven-archetype-plugin</artifactId>
          <version>2.4</version>
        </plugin>
      </plugins>
    </pluginManagement>
  </build>
</project>

Content of the src/main/resources/archetype-resources/pom.xml:

<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <groupId>${groupId}</groupId>
  <artifactId>${artifactId}</artifactId>
  <version>${version}</version>
</project>

And finally, content of the src/main/resources/META-INF/maven/archetype-metadata.xml:

<archetype>
  <id>my-simple-archetype</id>
</archetype>

Now you can build this project and install it:

cd my-simple-archetype
mvn clean install

This will update your local catalog so that this new archetype is available. You can finally use it! In a new directory, do

mvn archetype:generate -DgroupId=eric -DartifactId=hello -Dversion=0.1 -DarchetypeArtifactId=my-simple-archetype -DarchetypeGroupId=eric -DinteractiveMode=false

And you will have as result your wanted project... which consists of the lone pom.xml. So, of course, you can now customize this archetype of yours.
Remove the files

Or you decide that it is not worth the effort, and it is a lot simpler to remove the files after their creation:

mvn archetype:generate -DgroupId=eric -DartifactId=hello -Dversion=0.1 -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
rmdir /S /Q hello\src

Or rm -rf hello/src if you're on a Linux machine.
shareimprove this answer
answered Oct 16 '16 at 22:15
Tunaki
98.8k2424 gold badges231231 silver badges317317 bronze badges

    1
    Great to see the example on creating a customized archetype. – Eric Wang Oct 17 '16 at 6:03
    Had the same issue today. Providing an archetype you can't use out of the box sounds really frigging stupid. – Floating Sunfish Nov 26 '18 at 6:16 

add a comment