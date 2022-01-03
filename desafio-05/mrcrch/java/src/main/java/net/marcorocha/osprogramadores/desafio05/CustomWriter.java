package net.marcorocha.osprogramadores.desafio05;

import java.io.BufferedWriter;
import java.io.FileDescriptor;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStreamWriter;

/**
 * @see http://www.rgagnon.com/javadetails/java-0603.html
 */
public class CustomWriter extends BufferedWriter {

    private static final int BUFFER_SIZE = 512;
    private static final String LINE_SEPARATOR = System.lineSeparator();

    public CustomWriter() throws IOException {
        super(new OutputStreamWriter(new FileOutputStream(FileDescriptor.out)), BUFFER_SIZE);
    }

    public void writeln(String s) throws IOException {
        write(s + LINE_SEPARATOR);
    }

    @Override
    public void close() throws IOException {
        flush();
        super.close();
    }

}
