#!/bin/bash
# ng commands
# create a new application
cd "C:/Users/Candan Yuksel/Desktop"
ng new ecommerce-frontend
# ng new app-name
# ng new app-name --style=scss --routing=true

# ng serve (Build the app and start it as a webserver.)
# ng serve -o (Build your app and open it in the webbrowser)
# ng serve --port=4444 (Serve your app on a different port 
# ng serve --base-href="/my-app/"  (http://localhost:4200/my-app/)
# ng serve --aot  (ahead of time compilation.) 

# ng build --prod (Production build)
# ng build --base-href="/my-app/"  (Productie build for a app with a base url: /my-app/)
# ng build --prod --aot --output-hashing=none --base-href=/rocksteady/  --build-optimizer=true
# ng build --output-path C:\temp\myapp (Provide an output path for the compiled code. Useful when automating your workflow.)

# Generate a component
# ng g c name-component
# Generate a interface
# Generate a module
# ng g m my-module
# ng g m my-module --routing (Generate a module with a routing module)
# ng g i my-interface
# Generate an interface with a “type”
# ng g i my-interface -t=green
# Generate a service
# ng g s my-service

# Steps to delete a component in Angular
# Remove the import line reference from Angular app.module.ts file.
# Remove the component declaration from @NgModule declaration array in app.module.ts file
# And then manually delete the component folder from Angular project.
# Finally Delete all the references of component manually from the Angular project.

read -p "Press [Enter] key to go on."