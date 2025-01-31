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
