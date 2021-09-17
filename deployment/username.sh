#!/bin/bash

pushd deployment
cp classified.service classified.service.new
sed -i "s/apps/${USER}/g" classified.service.new
cp nginx.site nginx.site.new
sed -i "s/apps/${USER}/g" nginx.site.new
popd