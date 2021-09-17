#!/bin/bash

pushd deployment
sed -i "s/apps/${USER}/g" classified.service
sed -i "s/apps/${USER}/g" nginx.site
popd