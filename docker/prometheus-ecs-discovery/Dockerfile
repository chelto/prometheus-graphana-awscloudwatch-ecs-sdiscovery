FROM golang:1.15-alpine
RUN apk --no-cache add git
RUN git clone https://github.com/teralytics/prometheus-ecs-discovery.git
WORKDIR prometheus-ecs-discovery
RUN go get
RUN CGO_ENABLED=0 GOOS=linux go build -o /bin/prometheus-ecs-discovery .

FROM alpine:latest
RUN apk --no-cache add ca-certificates
COPY --from=0 /bin/prometheus-ecs-discovery /bin/
ENTRYPOINT ["prometheus-ecs-discovery"]
