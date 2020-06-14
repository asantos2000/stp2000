# Voltage
echo "Voltage"
for id in core sdram_c sdram_i sdram_p ; do \
    echo -e "$id:\t$(vcgencmd measure_volts $id)" ; \
done

# Temp
echo Temperature
/opt/vc/bin/vcgencmd measure_temp

# Clock speed
echo "Clock speed"
vcgencmd measure_clock arm