#!/bin/bash

# Create a Dockerfile for our custom image
cat > Dockerfile << 'EOF'
FROM manimcommunity/manim:stable

# Install Xvfb and additional LaTeX packages as root
USER root
RUN apt-get update && \
    apt-get install -y \
    xvfb \
    texlive-latex-extra \
    texlive-fonts-extra \
    texlive-science

# Create the wrapper script
RUN echo '#!/bin/bash\nxvfb-run -a "$@"' > /usr/local/bin/with-xvfb && \
    chmod +x /usr/local/bin/with-xvfb

# Switch back to default user
USER 1000:1000
EOF

# Build the custom image
docker build -t manim-xvfb .

# Remove old container if it exists
docker rm -f manim-container 2>/dev/null

# Change to your manimations directory
cd ~/Repos/manimations

# Run the container with the custom image
docker run -it --name manim-container \
    -v "$(pwd):/manim" \
    --user="$(id -u):$(id -g)" \
    manim-xvfb \
    bash
