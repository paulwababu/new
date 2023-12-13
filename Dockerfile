# Stage 1: init
FROM python:3.11 as init

ARG API_URL

WORKDIR /app
COPY . .

ENV VIRTUAL_ENV=/app/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN python3.11 -m venv $VIRTUAL_ENV
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Install Node.js and Unzip
RUN apt-get update && apt-get install -y curl unzip
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash -
RUN apt-get install -y nodejs

# Test Node.js installation
RUN node --version

# Deploy templates and prepare app
RUN reflex init
RUN reflex export --frontend-only --no-zip

# Copy static files out of /app to save space in backend image
RUN mv .web/_static /tmp/_static
RUN rm -rf .web && mkdir .web
RUN mv /tmp/_static .web/_static

# Stage 2: copy artifacts into slim image 
FROM python:3.11-slim
ARG API_URL
WORKDIR /app
RUN adduser --disabled-password --home /app reflex

# Install Node.js in the slim image
RUN apt-get update && apt-get install -y curl unzip
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash -
RUN apt-get install -y nodejs

# Copy over the application
COPY --chown=reflex --from=init /app /app
RUN chown -R reflex:reflex /app

# Create necessary directories with proper permissions
RUN mkdir -p /app/.local && chown -R reflex:reflex /app/.local

USER reflex

# Set the PATH for reflex user
ENV PATH="/app/.venv/bin:/usr/local/bin:$PATH" API_URL=$API_URL

# Test Node.js availability for reflex user
RUN node --version

CMD reflex init && reflex db makemigrations && reflex db migrate && reflex run
