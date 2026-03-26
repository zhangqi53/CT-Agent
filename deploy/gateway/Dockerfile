# CT-Agent MCP Gateway
# Port: 35679
# Routes MCP tool calls to GPU/CPU backends + cloud APIs

FROM node:20-slim

WORKDIR /app

COPY ../mcp-server/package.json ../mcp-server/tsconfig.json ./
COPY ../mcp-server/src ./src

RUN npm install && npm run build 2>&1 | tee /app/build.log \
    && echo "BUILD_SUCCESS" >> /app/build.log \
    || (echo "BUILD_FAILED" >> /app/build.log && exit 1)

HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
    CMD node -e "fetch('http://localhost:35679/health').then(r=>process.exit(r.ok?0:1)).catch(()=>process.exit(1))"

EXPOSE 35679

CMD ["node", "dist/index.js"]
